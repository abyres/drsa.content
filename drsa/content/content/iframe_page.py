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

class IIFramePage(form.Schema, IImageScaleTraversable):
    """
    Embed IFrame as page
    """
    url = schema.TextLine(title=_(u"label_iframe_url", default=u"URL"),
            description=_(u"help_iframe_url", 
                default=u"URL to be embedded in IFrame")
    )

    height = schema.Int(title=_(u"label_height", default=u"Height"),
            description=_(u"help_height", default=u"IFrame height"),
            default=500)

alsoProvides(IIFramePage, IFormFieldProvider)
