from five import grok
from plone.directives import dexterity, form
from drsa.content.content.sas_dashboard import ISASDashboard
from drsa.content.providers import ISASIFrameProvider

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ISASDashboard)
    grok.require('zope2.View')
    grok.template('sas_dashboard_view')
    grok.name('view')

    def iframe_url(self):
        return ISASIFrameProvider(self.context).iframe_url()

    def iframe_style(self):
        return ISASIFrameProvider(self.context).iframe_style()
