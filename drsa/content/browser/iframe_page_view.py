from five import grok
from plone.directives import dexterity, form
from drsa.content.content.iframe_page import IIFramePage

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IIFramePage)
    grok.require('zope2.View')
    grok.template('iframe_page_view')
    grok.name('view')

    def iframe_url(self):
        return self.context.url

    def iframe_style(self):
        return "height:%spx;width:100%%" % self.context.height

