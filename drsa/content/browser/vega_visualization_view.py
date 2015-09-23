from five import grok
from plone.directives import dexterity, form
from drsa.content.content.vega_visualization import IVegaVisualization
import json

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IVegaVisualization)
    grok.require('zope2.View')
    grok.template('vega_visualization_view')
    grok.name('view')

    def iframe_style(self):
        data = json.loads(self.context.vega_json)
        height = data.get('height', 500) + 100
        width = data.get('width', 500) + 100
        return "height:%spx;width:%spx;margin:auto 0;" % (height, width)

class VegaRuntime(grok.View):
    grok.context(IVegaVisualization)
    grok.require('zope2.View')
    grok.template('vega_runtime')
    grok.name('vega_runtime')


    def script(self):
        return """
// parse a spec and create a visualization view
function parse(spec) {
  vg.parse.spec(spec, function(chart) { chart({el:"#vis"}).update(); });
}
parse("%(json_url)s");
        """ % {'json_url': "%s/vega.json" % self.context.absolute_url()}



class VegaJSON(grok.View):
    grok.context(IVegaVisualization)
    grok.require('zope2.View')
    grok.name('vega.json')

    def render(self):
        return self.context.vega_json
