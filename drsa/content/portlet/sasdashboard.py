from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form

# XXX: Uncomment for z3cform

from z3c.form import field

#from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationList, RelationChoice

from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from drsa.content import MessageFactory as _

class ISASDashboard(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    name = schema.TextLine(
        title=_(u"label_dashboard_title", default=u"Title"),
        description=_(u"help_dashboard_title", 
            default=u"Title of this dashboard"
        ),
        default=u"",
        required=False
    )

    server = schema.TextLine(
        title=_(u"label_server_url", default=u"Server URL"),
        description=_(u"help_server_url", default=u"URL to the SAS VA Server"),
        default=u"",
        required=True
    )

    reportPath = schema.TextLine(
        title=_(u"label_report_path", default=u"Report Path"),
        description=_(u"help_report_path", 
            default=u"Directory path of the report"),
        default=u"",
        required=True,
    )

    reportName = schema.TextLine(
        title=_(u"label_report_name", default=u"Report Name"),
        description=_(u"help_report_name", 
            default=u"Name of the report"),
        default=u"",
        required=True
    )

    height = schema.Int(
        title=_(u"label_height", default=u"Height"),
        description=_(u"help_height", default=u"Height of the dashboard"),
        default=500,
        required=True
    )

class Assignment(base.Assignment):
    implements(ISASDashboard)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('SAS Dashboard')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/sasdashboard.pt')

    @property
    def available(self):
        return True

# XXX: z3cform
# class AddForm(z3cformhelper.AddForm):
class AddForm(base.AddForm):

#    XXX: z3cform
#    fields = field.Fields(ISASDashboard)

    form_fields = form.Fields(ISASDashboard)

    label = _(u"Add SAS Dashboard")
    description = _(u"Portlet for embedding SAS Dashboards")

    def create(self, data):
        return Assignment(**data)

# XXX: z3cform
# class EditForm(z3cformhelper.EditForm):
class EditForm(base.EditForm):

#    XXX: z3cform
#    fields = field.Fields(ISASDashboard)

    form_fields = form.Fields(ISASDashboard)

    label = _(u"Edit SAS Dashboard")
    description = _(u"Portlet for embedding SAS Dashboards")
