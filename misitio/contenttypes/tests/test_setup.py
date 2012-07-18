# -*- coding: utf-8 -*-

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from plone.i18n.normalizer import idnormalizer

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from misitio.contenttypes.config import PROJECTNAME
from misitio.contenttypes.testing import INTEGRATION_TESTING

from AccessControl import Unauthorized

class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')
        self.types = getToolByName(self.portal, 'portal_types')

    def test_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        'package appears not to have been installed')
    
    def test_contenttypes_are_registred(self):
        """ Validate that our contenttypes are registred
        """
        existing = self.types.objectIds()
        self.assertTrue('consejo_comunal' in existing)
        self.assertTrue('miembro' in existing)

    def test_consejo_comunal_allowed_content_types(self):

        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        cc_title = 'Las piedritas'
        oid = idnormalizer.normalize(cc_title, 'es')
        #self.cc = createConcejoComunal(self.portal, cc_title)
        self.portal.invokeFactory('consejo_comunal', id=oid, title=cc_title)
        self.cc = self.portal[oid]
        types = ['File', 'Image', 'Link', 'miembro',]
        allowed_types = [t.getId() for t in self.cc.allowedContentTypes()]
        for t in types:
            self.assertTrue(t in allowed_types)
        
        # trying to add any other content type raises an error
        self.assertRaises(ValueError,
                          self.cc.invokeFactory, 'Document', 'Registro legal')
        try:
            miembro_title = 'Leonardo J. Caballero G.'
            self.cc.invokeFactory('miembro', miembro_title)
        except Unauthorized:
            self.fail()

class UninstallTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

