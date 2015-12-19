# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2014 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('Dialogues: setuphandlers')
from Products.Dialogues.config import PROJECTNAME
from Products.Dialogues.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
##/code-section HEAD

def isNotDialoguesProfile(context):
    return context.readDataFile("Dialogues_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotDialoguesProfile(context): return
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()


def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotDialoguesProfile(context): return 
    site = context.getSite()


##code-section FOOT
##/code-section FOOT
