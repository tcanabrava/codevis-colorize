import types
import pyLksPlugin

def recoulourize(actionHandler):
    pigmentRed = pyLksPlugin.Color(237, 27, 36, 255)
    viewedEntities = actionHandler.getAllEntitiesInCurrentView()
    for viewedEntity in viewedEntities:
        viewedEntity.setColor(pigmentRed)

def hookGraphicsViewContextMenu(menuHandler):
    menuHandler.registerContextMenu("Color lala the Things", recoulourize)
