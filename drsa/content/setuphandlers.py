from collective.grok import gs
from drsa.content import MessageFactory as _

@gs.importstep(
    name=u'drsa.content', 
    title=_('drsa.content import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('drsa.content.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
