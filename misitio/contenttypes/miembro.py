# -*- coding: utf-8 -*-

from zope import schema
from plone.directives import form
from plone.namedfile.field import NamedBlobImage


class IMiembro(form.Schema):    
    """Tipo de contenido miembro de un Consejo comunal.
    """
    
    nombres = schema.TextLine(
        title = u"Nombres",
        description = u"Nombres del miembro",
        required = True
    )
    
    apellidos = schema.TextLine(
        title = u"Cedula",
        description = u"Cedula de identidad",
        required = True
    )
    
    direccion_fisica = schema.TextLine(
        title = u"Direccion fisica",
        description = u"Direccion fisica del miembro",
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
        title = u"Fotografia",
        description = u"Fotografia del miembro",
        required = False
    )
    
