# -*- coding: utf-8 -*-
#
# File: Invoicing.py
#
# Copyright (c) 2012 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "Invoicing"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
ADD_CONTENT_PERMISSIONS = {
    'AdGroup': 'Invoicing: Add AdGroup',
    'Company': 'Invoicing: Add Company',
    'Invoice': 'Invoicing: Add Invoice',
    'Letter': 'Invoicing: Add Letter',
    'Advertizement': 'Invoicing: Add Advertizement',
    'Insertion': 'Invoicing: Add Insertion',
    'LineItems': 'Invoicing: Add LineItems',
}

setDefaultRoles('Invoicing: Add AdGroup', ('Manager','Owner'))
setDefaultRoles('Invoicing: Add Company', ('Manager','Owner'))
setDefaultRoles('Invoicing: Add Invoice', ('Manager','Owner'))
setDefaultRoles('Invoicing: Add Letter', ('Manager','Owner'))
setDefaultRoles('Invoicing: Add Advertizement', ('Manager','Owner'))
setDefaultRoles('Invoicing: Add Insertion', ('Manager','Owner'))
setDefaultRoles('Invoicing: Add LineItems', ('Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from Products.Invoicing.AppConfig import *
except ImportError:
    pass
