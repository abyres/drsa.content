from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from collective import dexteritytextindexer

from drsa.content import MessageFactory as _


# Interface class; used to define content-type schema.

class ISASDashboard(form.Schema, IImageScaleTraversable):
    """
    Display SAS Dashboard
    """
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


alsoProvides(ISASDashboard, IFormFieldProvider)
