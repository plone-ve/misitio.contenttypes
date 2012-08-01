# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import implements

from five import grok

from plone.directives import form
from plone.namedfile.field import NamedBlobImage

from plone.app.content.interfaces import INameFromTitle
from plone.dexterity.content import Item

class IMiembro(form.Schema):    
    """Tipo de contenido miembro de un Consejo comunal.
    """
    
    cedula = schema.TextLine(
        title = u"Cédula",
        description = u"Cédula de identidad",
        required = True
    )
    
    nombres = schema.TextLine(
        title = u"Nombres",
        description = u"Nombres del miembro",
        required = True
    )
    
    apellidos = schema.TextLine(
        title = u"Apellidos",
        description = u"Apellidos del miembro",
        required = True
    )
    
    direccion_fisica = schema.TextLine(
        title = u"Dirección física",
        description = u"Dirección física del miembro",
        required = True
    )
    
    pagina_web = schema.TextLine(
        title = u"Pagina Web",
        description = u"Pagina Web del miembro",
        required = False
    )
    
    twitter = schema.TextLine(
        title = u"Twitter",
        description = u"Cuenta Twitter",
        required = False
    )
    
    fotografia = NamedBlobImage(
        title = u"Fotografía",
        description = u"Fotografía del miembro",
        required = False
    )
    
class Miembro(Item):
    """Customised Miembro content class"""
    
    @property
    def title(self):
        if hasattr(self, 'nombres') and hasattr(self, 'apellidos'):
            return self.nombres + ' ' + self.apellidos
        else:
            return ''
 
    def setTitle(self, value):
        return
        

class INameFromMiembroNames(INameFromTitle):
    
    def title():
        """Return a processed title"""

class NameFromMiembroNames(object):
    implements(INameFromMiembroNames)

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        return self.context.nombres + ' ' + self.context.apellidos
    
    
grok.templatedir('miembro_templates')
    
class View(grok.View):
    """Clase vista para el esquema Miembro.
    """
    
    grok.context(IMiembro)
    grok.require('zope2.View')
    grok.template("view")
    
