# -*- coding: utf-8 -*-
#
# File: Block.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from Products.CMFCore import permissions
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from archetypes.referencebrowserwidget import ReferenceBrowserWidget
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName
from interfaces import IBlock
import interfaces
from BlockishSchema import BlockishSchema

from Products.Five.browser import BrowserView

import json


##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ReferenceField(
        name='containers',
        widget=InAndOutWidget(
            label='Containers',
            label_msgid='Newspaper_label_containers',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Container','YouCanBox','CreditsBox','Puzzle','Company','Cartoon','House','Advertizement','Dialogue','Recipe',),
        multiValued=1,
        relationship='containerLocation',
	keepReferencesOnCopy=1,
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Block_schema = OrderedBaseFolderSchema.copy() + \
	BlockishSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BlockJSON(BrowserView):
    """ JSON Encoded Issue """
    def __init__(self,context,request):
        """ Initialize context and request as view multiadaption parameters.

        Note that the BrowserView constructor does this for you.
        This step here is just to show how view receives its context and
        request parameter. You do not need to write __init__() for your
        views.
        """
        self.context = context
        self.request = request

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    def __call__(self):
   	self.request.response.setHeader("Content-type","application/json")
	json_item = {}
	title = self.context.getId()
	blocks = self.context.getContainers()
	top = self.context.getTop()
	left = self.context.getLeft()
	for block in blocks:
	    json_item['Block']=block.getJSON(top,left)
	pretty = json.dumps(json_item)    
	return pretty 

class SnapshotView(BrowserView):
    """ A View of the Widget """
    def __init__(self, context, request):
        """ Initialize context and request as view multiadaption parameters.

        Note that the BrowserView constructor does this for you.
        This step here is just to show how view receives its context and
        request parameter. You do not need to write __init__() for your
        views.
        """
        self.context = context
        self.request = request

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    #def __call__():
    #

class Block(OrderedBaseFolder,  BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBlock)

    meta_type = 'Block'
    _at_rename_after_creation = True

    schema = Block_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    security.declarePublic(permissions.View,'web')
    def web(self): 
	    """
	    Test
	    """
	    return self.getContainers()[0].web()

    def getJSON(self):
	    """
	    Test
	    """
	    json_items={}
	    json_item={}
	    blocks = self.getContainers();
	    top = self.getTop()
	    left = self.getLeft()
	    for block in blocks:
		blockname=block.getId()
		json_item[blockname]=blockname
	    json_items['Block']=json_item
	    return json_items

    def toggleDivTagsOn(self):
	    """
            return true if Div Tags are on.
	    """
	    return self.getToggleDivTagsOn() 

    def just(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    justTemplate=skin.justBlock
	    return justTemplate()
    
    def getLines(self,columnid):
	    return self['columnid'].getLines()
	    
    def listColumns(self):
	    """
	    hey!
	    """
	    return self.returnInput()

    def returnInput(self):
	    """
	    Test
	    """
	    stringValue = ""
	    items = self.listFolderContents(contentFilter={"portal_type":"Column"})
	    #items = self.contentItems()
	    #for item in items:
	    #    stringValue += item[1].just()
	    #return stringValue
	    #urls=[]
	    #for item in items:
	#	if item.getHeadline() == True:
	#            urls.append(item)
	#    for item in items:
	#	if item.getHeadline() == False:
	#            urls.append(item)
	    return items

    def getImage(self):
	   """
	   Test
	   """
	   items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
	   return items[0].getPicture()


    def callPDTBySameName(self,REQUEST,parent,top='0',left='0',width='0',height='0',start="",end=""):
	    """
	    Test
	    """
	    #print "Block"
	    #print self.Title()
            style3="'"
	    containercontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()+'.pd'
	    result = PDFPageTemplate(self.Title(),containercontainer)
	    theDiv = self.getDivid()
            theClass = self.getClass()


	    style2="'"
            theLeft = self.getLeft()
            if theLeft is not None:
		style2 += "left:"
                style2 += str(theLeft)
		style2 += "px"
                style2 += ";"
		style3 += "left:"
                style3 += str(theLeft)
		style3 += "px"
                style3 += ";"
                left = theLeft
            else:
                left = 0
            style2 += "position:relative;"
	    output = "<div style='position:absolute;left:0px;top:"
	    output += str(top)
	    output += "px'><div id='"
	    output += self.getId()
            output += "' class='"
            output += "container'"

	    start = "<div class='"
	    start += "name"
	    start += "' onmouseover="
	    start += '"'
	    start += "this.style.cursor='hand'"
	    start += '"'
	    style3 += "display:none;position:relative;background-color:rgba(0,255,0,0.5);color:red;'"
	    start += " style="
	    start += style3
	    start += ">"
	    start += self.getId()
	    start += "</div>"
            start = "<div style='clear:both;'></div>"


            
	    output2 = result.continueWEB(REQUEST,parent,containercontainer,start)
	    style2 += "top:"
	    style2 += str(2*int(output2[1]))
   	    style2 += "px;"
	    style2 += "'"
            output += "style="
	    output += style2
            output += ">"
	    output += output2[0]
	    output += "</div><br/>"


            height = 0
	    return (output,top,left,width,height)

    def getBlockWidthHeight(self):
	    """
	    Test
 	    """
	    width=0
	    height=0
	    item = self.getContainers()[0]
	    width = item.getWidth()
	    for section in self.getContainers():
		height += section.getHeight()
	    height = 5 * height
	    return (width,height)

    def getHeight(self):
	"""
	TEST
	"""
	print "Block getHeight"
	height = 0
	item = self.getContainers()
	print item
	height = item[0].getHeight()
	print height
	return height


    def getWidth(self):
	"""
	test
	"""
	(width,height) = self.getBlockWidthHeight()
	return width

    security.declarePublic(permissions.View,'snapshot')
    def snapshot(self):
        """
	Test
	"""
	width = self.getWidth()
	height = self.getHeight()
	return self.getSnapshot(width,height)

    security.declarePublic(permissions.View,'getSnapContent')
    def getSnapContent(self):
        """
	Test
	"""
	(width,height) = self.getBlockWidthHeight()
	snapcontent = self.getSnapshot(width,height)
	return snapcontent


    security.declarePublic(permissions.View,'getSnapLink')
    def getSnapLink(self):
	"""
	TEST
	"""
	retval = "<a href='"
	item = self.getContainers()[0]
	retval += item.theLinky()
	retval += "'>"
	retval += "Read More ..."
	retval += "</a>"
	return retval

    security.declarePublic(permissions.View,'getInformationStyle')
    def getInformationStyle(self):
	    """
	    Test
	    """
	    red = 0x90;
	    green = 0x90;
	    blue = 0x0;
	    (width,height) = self.getBlockWidthHeight()
	    width *= .2
	    height *= .05 
	    rgb = format((blue<<16)|(green<<8)|red, '06x')
	    snapstyle = "background-color:#"+rgb+";"
	    snapstyle += "position:relative;valign:top;float:right;"
	    snapstyle += "width:"+str(width)+"px;"
	    snapstyle += "height:"+str(height)+"px;"
	    snapstyle += "top:0px";
	    snapstyle += "left:0px;"
	    snapstyle += "z-index:30;"
	    snapstyle += "border-style:solid;border-width:1px;"
	    return snapstyle

    security.declarePublic(permissions.View,'getSnapStyle')
    def getSnapStyle(self):
	    """
	    Test
	    """
	    red = 0x80;
	    green = 0x80;
	    blue = 0x80;
            top=self.getTop()
	    orig_top = top
	    left=self.getLeft()
	    (width,height) = self.getBlockWidthHeight()
	    width *= 1.2 
	    height *= 0.45
	    top *= 1.2 
	    left *= 1.55
	    rgb = format((blue<<16)|(green<<8)|red, '06x')
	    snapstyle = "background-color:#"+rgb+";"
	    snapstyle += "position:absolute;"
	    snapstyle += "top:"+str(orig_top)+"px;"
	    snapstyle += "left:"+str(left)+"px;"
	    snapstyle += "width:"+str(width)+"px;"
	    snapstyle += "height:"+str(height)+"px;"
	    snapstyle += "z-index:20;"
	    snapstyle += "border-style:solid;border-width:1px;"
	    return snapstyle

    security.declarePublic(permissions.View,'getEditsnap')
    def getEditsnap(self,width,height):
	    """
	    snapshot
	    """
	    result = ""
	    snap = ""
	    obj = self.getContainers()
	    for item in obj:
		try:
		    snap = item.getEditsnap(width,height)
	        except AttributeError:
		    snap = item.getSnapshot(width,height)
	        result += snap
	    return result

    security.declarePublic(permissions.View,'getSnapshot')
    def getSnapshot(self,width,height):
	    """
	    snapshot
	    """
	    result = ""
	    obj = self.getContainers()
	    for item in obj:
		snapshot = item.getSnapshot(width,height)
		if snapshot is not None:
	            result += item.getSnapshot(width,height)
	    return result

    def getDivInfo(self):
            """
            test
            """
            return "INFORMATION"

#    def getBlockWidthHeight(self):
#	    """
#	    Test
# 	    """
#	    width=0
#	    height=0
#	    obj = self.getContainers()
#	    for item in obj:
#	        id = item._objects[0]['id']
#		object = obj[0][id]
#		print object
#	        width+=object.getWidth()
#	        height+=object.getHeight()
#	    return (width,height)

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber,outline):
	    """
	    Test
	    """
	    showLink = self.getShowLink()
	    obj = self.getContainers()
	    ll = self.getLeft()
            tt = self.getTop()
	    offset = tt
	    for item in obj:
		#print item.__dict__
		#print item.id
		#print item.title_or_id
		item.callPDFPDTBySameName(c,ll,offset,REQUEST,item,top,pagenumber)
		if outline == True:
		    fRed = 1
		    fGreen = 0
		    fBlue = 1
		    left = ll
		    top = tt
		    width = 3
		    height = 3
		    c.setFillColorRGB(fRed,fGreen,fBlue)
		    c.rect(left,top,width,height,fill=1)
	    if showLink:
	        textobject=c.beginText()
	    	textobject.setFont("Times-Roman",11)
	    	textobject.setTextOrigin(ll,1155-tt)
	    	link = self.getId()
	    	parent = self.aq_inner.aq_parent
	    	prevlink = parent.getId()
	    	issuelink = parent.getIssueUrl()
	    	totallink = issuelink + '/'+link + '/'
	    	textobject.textLine(totallink)
	    	c.drawText(textobject)
	    return (x,y)

    def getXOffset(self):
            """
            Test
            """
            return 0

    def getYOffset(self):
            """
            Test
            """
            return 0

    def pdf(self):
            """
            PDF
            """
            return "PDF"

    security.declarePublic(permissions.View,'getNumberOfColumns')
    def getNumberOfColumns(self):
	    """
		Dummy
	    """
	    return 1

    def getBlockClass(self):
            """
            test
            """
            page = self.aq_inner.aq_parent
            pageid = page.getId()
	    return pageid

    def linky(self):
	    """
	    OK
	    """
	    theContainers = self.getContainers()
	    for container in theContainers:
           	 theName = container.title
	         theId = container.id
		 theId += "/show"
	    theLink = "<a href='http://newhollandpress.com/"
	    theLink += theId
	    theLink += "'>"
	    theLink += theName
	    theLink += "</a>"
	    return theLink

    security.declarePublic('getNumberOfColumns')
    def getNumberOfColumns(self):
	"""
	Return the number of Columns
	"""
	numberOfColumns = 1
	return numberOfColumns

registerType(Block, PROJECTNAME)
# end of class Block

##code-section module-footer #fill in your manual code here
##/code-section module-footer

