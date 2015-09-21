from five import grok
from zope.interface import Interface
from drsa.content.portlet.sasdashboard import ISASDashboard as PortletIface
from drsa.content.content.sas_dashboard import ISASDashboard as ContentIface
import urllib

class ISASIFrameProvider(Interface):
    pass

class SASIFrameProvider(grok.Adapter):
    grok.baseclass()
    grok.implements(ISASIFrameProvider)
   
    def __init__(self, context):
        self.context = context

    def iframe_url(self):
        server_url = self.context.server.strip().split("/")
        va_path = [
            "SASVisualAnalyticsViewer",
            "VisualAnalyticsViewer_guest.jsp"
        ]
        reportPath = self.context.reportPath.strip().replace(" ","+")
        reportName = self.context.reportName.strip().replace(" ","+")

        url = '/'.join(server_url + va_path)
        param = {
            "reportPath": reportPath,
            "reportName": reportName,
            "appSwitcherDisabled": "true",
            "reportViewOnly": "true"
        }

        return url + "?" + urllib.urlencode(param)

    def iframe_style(self):
        return "height:%spx;width:100%%" % self.context.height

class PortletProvider(SASIFrameProvider):
    grok.context(PortletIface)

class ContentProvider(SASIFrameProvider):
    grok.context(ContentIface)
