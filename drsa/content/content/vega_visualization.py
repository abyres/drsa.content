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

class IVegaVisualization(form.Schema, IImageScaleTraversable):
    """
    Visualization dashboard using Vega JSON
    """
    vega_json = schema.Text(
        title=_(u"label_vega_json", default=u"Vega JSON"),
        description=_(u"help_vega_json", 
            default=u"Enter your Vega JSON config here"),
        required=True
    )

alsoProvides(IVegaVisualization, IFormFieldProvider)
