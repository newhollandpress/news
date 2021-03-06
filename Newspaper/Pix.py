# -*- coding: utf-8 -*-
#
# File: Pix.py
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
from plone.app.blob.field import BlobField, ImageField
from zope.interface import implements
import interfaces
import string 
from StringIO import StringIO
import reportlab.pdfgen.canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import *

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter


from reportlab.lib.colors import yellow,red,black,white
from reportlab.lib.units import inch

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *

from Products.Newspaper.Element import Element
from Products.Newspaper.Element import Element_schema


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='caption',
        widget=StringField._properties['widget'](
            label='Caption',
            label_msgid='Newspaper_label_caption',
            i18n_domain='Newspaper',
            ),
        ),
    StringField(
        name='credit',
        widget=StringField._properties['widget'](
            label='Credit',
            label_msgid='Newspaper_label_caption',
            i18n_domain='Newspaper',
            ),
        ),
    StringField(
        name='pixclass',
        default='pixclass',
        widget=StringField._properties['widget'](
            label='Pix class',
            label_msgid='Newspaper_label_pixclass',
            i18n_domain='Newspaper',
            ),
        ),
    ImageField(
        name='picture',
        widget=ImageField._properties['widget'](
            label='Pix',
            label_msgid='Newspaper_label_picture',
            i18n_domain='Newspaper',
            ),
        storage=AttributeStorage(),
        ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Pix_schema = Element_schema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class PixJSON(BrowserView):
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
        json_item['Pix']=title
        attributes={}
        attributes['caption']=self.context.getCaption()
        attributes['credit']=self.context.getCredit()
        attributes['pixclass']=self.context.getPixclass()
        attributes['width']=self.context.getWidth()
        attributes['height']=self.context.getHeight()
        pixpath = self.context.absolute_url() + '/picture'
        attributes['pixpath']=pixpath
        json_item['attributes']=attributes
        pretty = json.dumps(json_item)    
        return pretty 

class Pix(Element):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPix)

    meta_type = 'Pix'
    _at_rename_after_creation = True

    schema = Pix_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def returnPix(self):
        """
        Test
        """
        theImage = self.getId()
        theDiv = "<div id='"
        theDiv += theImage
        theClass = self.getPixclass()
        theDiv += "' class='"
        theDiv += theClass
        theDiv += "' style='margin:10px;'"
        theDiv += ">"
        theTag = "<img width='"+str(self.getWidth())+"' height='"+str(self.getHeight())+"' src='"+self.absolute_url()+"/picture'/>"
        theDiv += theTag
        theDiv += "</div>"
        return theDiv

    def web(self):
        """
        Test
        """
        theImage = self.getId()
        theDiv = "<div id='"
        theDiv += theImage
        theClass = self.getPixclass()
        theDiv += "' class='"
        theDiv += theClass
        theDiv += "' style='margin:10px;'"
        theDiv += ">"
        theDiv += self.pixHTML()
        theDiv += "</div>"
        return theDiv


    def pixHTML(self):
        """
        Test
        """
        theImage = self.getId()
        theDiv = "<div id='"
        theDiv += theImage
        theDiv += "' class='pix' style='margin-left:30px;position:absolute;top:"
        theDiv += str(self.getTop())
        theDiv += "px;left:0"
        theDiv += "px;'"
        #theDiv += "style='border-color:blue;border-width:2px;border-style:solid;top:"
        left = self.getLeft()
        top = self.getTop()
        width = self.getWidth()
        height = self.getHeight()
        theDiv += ">"
        theTag = "<img width='"+str(self.getWidth())+"' height='"+str(self.getHeight())+"' src='"+self.absolute_url()+"/picture'/>"
        theDiv += theTag
        theDiv += "</div>"
        left += width
        return theDiv

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber,outline):
        """
        Test
        """
        xorig = x
        yorig = y
        height = self.getHeight()
        (x,y) = self.getPosition()
        y = 1200 - height - y
        theImage=self.getPicture()
        theBlob = theImage.getBlob()
        theString = theBlob.open().read()
        theStringIO=StringIO(str(theString))
        im = Image.open(theStringIO)
        im2 = im.transpose(1)
        theStringIO2=StringIO(str(im2.tostring()))		
        parent = self.aq_inner.aq_parent
        width = self.getWidth()
        height = self.getHeight()
        c.drawImage(ImageReader(StringIO(theString)),x,y,width,height)
        caption = self.getCaption()
        if caption is not None:
            textobject = c.beginText()
            textobject.setFillColorRGB(0,0,0)
            h = self.getHeight()
            if h is None:
                h = 400
            textobject.setTextOrigin(x,y-10)
            fontsize = 12
            textobject.setFont("Times-Roman", fontsize)
            textobject.textLine(caption)
            c.drawText(textobject)
        credit = self.getCredit()
        #if credit is not None:
        #    textobject = c.beginText()
        #    h = self.getHeight()
        #    w = self.getWidth()
        #    w = w - 100
        #    if h is None:
        #        h = 400
        #    textobject.setTextOrigin(x+30,y-15)
        #    fontsize = 11
        #    textobject.setFont("Times-Roman", fontsize)
        #    textobject.textLine(credit)
        #    c.drawText(textobject)
        return (x,y)

    def getSkinName(self):
        """
        TEST
        """
        return "showPix"

    def pdf(self,REQUEST): 
        """
        Test
        """
        skin = self.portal_skins.invoicing_templates
        showTemplate=skin.showIssue
        output = StringIO()
        c = canvas.Canvas(output,pagesize=letter,bottomup=0)
        x=35
        y=50
        theImage=self.getPicture()
        theImageData = StringIO()
        theImageUsage = theImage.file._read_data(theImageData)
        theImageReader = ImageReader(theImageUsage)
        (width,height) = theImageReader.getSize()
        parent = self.aq_inner.aq_parent
        width = self.getWidth()
        height = self.getHeight()
        if self.getTopMargin():
            y+=15
        c.drawImage(theImageReader,x,y,width,height,anchor='ne')
        caption = self.getCaption()
        credit = self.getCredit()
        pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
        pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
        if caption is not None:
            textobject = c.beginText()
            h = self.getHeight()
            if h is None:
                h = 400
            textobject.setTextOrigin(x,y+h+30)
            fontsize = 14
            textobject.setFont("FilosReg", fontsize)
            textobject.textLine(caption)
            c.drawText(textobject)
        if credit is not None:
            textobject = c.beginText()
            h = self.getHeight()
            if h is None:
                h = 400
            w = self.getWidth()
            w = w - 100
            textobject.setTextOrigin(x-w,y+h+15)
            fontsize = 11
            textobject.setFont("FilosReg",fontsize)
            textobject.textLine(credit)
            c.drawText(textobject)
        c.showPage()
        c.save()
        result = output.getvalue()
        output.close()
        response = REQUEST.RESPONSE
        response.setHeader('Content-type','application/pdf')
        return result 

    def publish(self,REQUEST):
        """
        Publish
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.publishPix
        return showTemplate()

    def getSnapshot(self,width,height):
        """
        Snapshot
        """
        retcode = "<div id='pix'>"
        actualWidth = width
        actualHeight = height
        tag = self.getField('picture').tag(self,height=actualHeight,width=actualWidth)
        caption = self.getCaption()
        retcode += tag
        retcode += "<div style='color:white;top:-30px;position:relative;'>"
        retcode += caption
        retcode += "</div>"	
        retcode += "</div>"	
        return (retcode,width,height)

    def getType(self):
        """
        Test
        """
        return "Pix"

    def getJSON(self):
        """
        Test
        """
        json_item = {}
        title = self.getId()
        json_item['type']='Pix'
        json_item['name']=title
        attributes={}
        attributes['caption']=self.getCaption()
        attributes['credit']=self.getCredit()
        attributes['pixclass']=self.getPixclass()
        attributes['width']=self.getWidth()
        attributes['height']=self.getHeight()
        pixpath = self.absolute_url() + '/picture'
        attributes['pixpath']=pixpath
        json_item['attributes']=attributes
        json_item['elements']=super(Pix,self).getJSON()
        return json_item 

registerType(Pix, PROJECTNAME)
# end of class Image

##code-section module-footer #fill in your manual code here
##/code-section module-footer

