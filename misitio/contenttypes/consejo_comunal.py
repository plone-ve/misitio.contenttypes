# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from five import grok

from zope import schema
from plone.directives import form

from Products.CMFCore.utils import getToolByName

from misitio.contenttypes.miembro import IMiembro

class IConsejoComunal(form.Schema):    
    """Tipo de contenido Consejo comunal.
    """
    
    ubicacion = schema.TextLine(
        title = u"Ubicación",
        description = u"Dirección física del consejo comunal",
        required = True
    )
    
    contacto = schema.TextLine(
        title = u"Contacto",
        description = u"Persona de contacto",
        required = True
    )
    
    telefono = schema.Int(
        title = u"Teléfono",
        description = u"Teléfono de contacto",
        required = True
    )
    
    correo = schema.TextLine(
        title = u"Correo",
        description = u"Correo electrónico de contacto",
        required = False
    )
    
grok.templatedir('consejo_comunal_templates')
    
class View(grok.View):
    """Clase vista para el esquema consejo_comunal.
    """
    
    grok.context(IConsejoComunal)
    grok.require('zope2.View')
    grok.template("view")
    
    def miembros_consejo_comunal(self):
        """Retorna un resultado de busqueda en el catalog de los tipos miembros de un consejo_comunal
        """
        
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        
        return catalog(object_provides=IMiembro.__identifier__,
                       path='/'.join(context.getPhysicalPath()),
                       sort_on='sortable_title')
        
