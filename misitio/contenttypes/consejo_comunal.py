# -*- coding: utf-8 -*-

from zope import schema
from plone.directives import form

class IConsejoComunal(form.Schema):    
    """Tipo de contenido Consejo comunal.
    """
    
    ubicacion = schema.TextLine(
        title = u"Ubicacion",
        description = u"Direccion fisica del consejo comunal",
        required = True
    )
    
    contacto = schema.TextLine(
        title = u"Contacto",
        description = u"Persona de contacto",
        required = True
    )
    
    telefono = schema.Int(
        title = u"Telefono",
        description = u"Telefono de contacto",
        required = True
    )
    
    correo = schema.TextLine(
        title = u"Correo",
        description = u"Correo electronico de contacto",
        required = False
    )
