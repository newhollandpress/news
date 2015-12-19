# -*- coding: utf-8 -*-
#
# File: RichColumn.py
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
from Products.Archetypes.Schema import Schema
from zope.interface import implements
import interfaces
import re
from richly import RichColumnar 
import htmlentitydefs as entity

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import  ReferenceBrowserWidget

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import inch

from Products.Newspaper.Element import Element
from Products.Newspaper.Element import Element_schema


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


    ReferenceField(
        name='article',
        widget=InAndOutWidget(
            label='Article',
            label_msgid='Newspaper_label_article',
            i18n_domain='Newspaper',
            ),
        allowed_types=('Wordage','Letter',),
        multiValued=1,
        relationship='containerLocation',
        ),
    IntegerField(
        name='startLine',
        widget=IntegerField._properties['widget'](
            label='StartLine',
            label_msgid='Newspaper_label_startLine',
            i18n_domain='Newspaper',
            ),
        ),
    IntegerField(
        name='endLine',
        widget=IntegerField._properties['widget'](
            label='EndLine',
            label_msgid='Newspaper_label_endLine',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='useRemainder',
        widget=BooleanField._properties['widget'](
            label='useRemainder',
            label_msgid='Newspaper_label_useRemainder',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='useContinuedOn',
        widget=BooleanField._properties['widget'](
            label='useContinuedOn',
            label_msgid='Newspaper_label_useContinuedOn',
            i18n_domain='Newspaper',
            ),
        ),
    StringField(
        name='continuedOn',
        default='Continued on Page Four',
        widget=StringField._properties['widget'](
            label='Continued On',
            label_msgid='Newspaper_label_continuedon',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='useContinuedFrom',
        widget=BooleanField._properties['widget'](
            label='useContinuedFrom',
            label_msgid='Newspaper_label_useContinuedFrom',
            i18n_domain='Newspaper',
            ),
        ),
    StringField(
        name='continuedFrom',
        default='Continued From Page One',
        widget=StringField._properties['widget'](
            label='Continued From',
            label_msgid='Newspaper_label_continuedfrom',
            i18n_domain='Newspaper',
            ),
        ),
    IntegerField(
        name='charsPerLine',
        default=48,
        widget=IntegerField._properties['widget'](
            label='Characters per Line',
            label_msgid='Newspaper_label_charsPerLine',
            i18n_domain='Newspaper',
            ),
        ),
    StringField(
        name='textclass',
        default='textclass',
        widget=StringField._properties['widget'](
            label='Text class',
            label_msgid='Newspaper_label_textclass',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='addLineHeight',
        widget=BooleanField._properties['widget'](
            label='addLineHeight',
            label_msgid='Newspaper_label_addLineHeight',
            i18n_domain='Newspaper',
            ),
        ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RichColumn_schema = Element_schema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class RichColumnMockFolder(BrowserView):
    """ A Tab for Plone that Says Folder Contents even though
    This is not a Folder """
    def __init__(self,context,request):
        """ Initialize context and request as view multiadaption parameters.

        Note that the BrowserView constructor does this for you,
        This step here is just to show how view  receives its context and  
        request parameter.  You do not need   to write __init__for your
        views.
        """
        self.context = context
        self.request = request

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    #def __call__(self):
    def parent_url(self):
        """
        Shortcut to provide Parent URL
        """
        return self.aq_inner.aq_parent

class RichColumnJSON(BrowserView):
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
        json_item['RichColumn']=title
        json_item['attributes']=self.context.getJSON()
        pretty = json.dumps(json_item)    
        return pretty 

class RichColumn(Element):
    """
    """
    added = False

    security = ClassSecurityInfo()

    numberOfColumns = 1

    implements(interfaces.IRichColumn)

    meta_type = 'RichColumn'
    _at_rename_after_creation = True

    schema = RichColumn_schema

    textContinued = False

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def displayValue(self,vocab,value,widget):
        """
        TEST
        """
        return "ferf"

    # Methods
    def contains(self): 
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.showColumn
        return showTemplate()

    def show(self): 
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        justTemplate=skin.justColumn
        return justTemplate()

    def getColumnWidth(self):
        """
        TEST
        """
        charsPerLine = self.getCharsPerLine()
        #print charsPerLine
        columnWidth=6*charsPerLine
        strColumnWidth=str(columnWidth)
        return strColumnWidth

    def getTheFontSize(self):
        """
        Test
        """
        theFontSize = self.getFontSize()
        if None == theFontSize:
            theFontSize = 11
        return str(theFontSize)+'pt'

    def getLinesVerbage(self):
        """
        Test
        """
        stringValue = ""
        #items = self.listFolderContents(contentFilter={"portal_type":"Line"})
        items = self.contentItems()
        #theLines = []
        for item in items:
            stringValue += item[1].getLineVerbage()
        return stringValue

    def getColumn(self):
        """
        Test
        """
        return self


    def listLines(self):
        """
        hey!
        """
        return self.returnInput()

    def returnInput(self):
        """
        Test
        """
        return self.returnLines()

    def pdf(self):
        """
        Test
        """
        items = self.listFolderContents(contentFilter={"portal_type":"Line"})
        skin = self.portal_skins.newspaper_templates
        pdfTemplate=skin.pdf
        c=canvas.Canvas("/tmp/hello.pdf")
        self.pdfOutput(c)
        c.showPage()
        c.save()
        return pdfTemplate()

    def pdfOutput(self,c,x,y):
        items = self.listFolderContents(contentFilter={"portal_type":"Line"})
        for item in items:
            theLine=item.getLineVerbage()
            c.drawString(100,y,theLine)
            y+=20

    def tripletOutput(self,x,y,l):
        triplets = []
        items = self.listFolderContents(contentFilter={"portal_type":"Line"})
        for item in items:
            theLine=item.getLineVerbage()
            triplet = (theLine,x,y)
            y+=l
            triplets.append(triplet)
        return triplets


    def callPDTBySameName(self,REQUEST,parent,top,left,width,height,start2="",end2=""):
        """
        Test
        """
        #print "Column"
        #print self.Title()
        pathcontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()+'.pd'
        #print pathcontainer
        result = PDFPageTemplate(self.Title(),pathcontainer)
        fontSize=self.getFontSize()
        fontName=self.getFontName()
        fontWeight=self.getFontWeight()
        fontClass=self.getFontClass()
        charsPerLine = self.getCharsPerLine()
        width=charsPerLine*6
        #style = "top:"
        #style += top
        #style += "0"
        #style += "px;"
        style = "font-size:11pt;position:relative;"
        style += "width:"
        style += str(width)
        style += "px;"
        #style += "left:"
        #style += str(left)
        #style += "px;"
        style += "text-justify:inter-word;text-align:justify;float:left;margin-right:20px;"
        #style += "border-color:yellow;border-style:solid;border-width:2px;position:relative;"
        #print style
        start = "<div id='"
        start += self.getId()
        start += "' class='"
        start += "column"
        start += "' style='"
        start += style
        start += "'>"
        end = "</div>"
        output = start
        output += start2
        output2 = result.continueWEB(REQUEST,parent,pathcontainer)
        output += output2[0]
        output += end
        height = 0
        left = str(int(width) + int(left))
        return (output,top,left,width,height)

    def web(self):
        """
        WEB
        """
        articles = self.getArticle()
        for article in articles:
            wordage = article.getWordage()
        return wordage.decode('utf-8')

    def setNumberOfColumns(self,numberOfColumns):
        """
        SET THE NUMBER OF COLUMNS
        FOR DISPLAY PURPOSES
        """
        self.numberOfColumns = numberOfColumns

    def getWidth(self):
        """
        Test
        """
        charsPerLine = self.getCharsPerLine()
        columnWidth=5*charsPerLine
        # need to divide by number of columns
        #columnWidth /= self.numberOfColumns
        return columnWidth

    def getHeight(self):
        """
        Return the Height in px that was requested by this RichColumn
        """
        y = 0
        width = self.getCharsPerLine() * 6
        articles = self.getArticle()
        output = []
        theParagraph = True 
        theCarrotStart = False
        theCarrotEnd = False
        theTagOpen = True
        theTag = ""
        theWordage = " "
        gotTheTag = False
        gotEndTag = False
        nasty = 'Â'
        totalLines = 0
        for article in articles:
            #print article
            verbage = article.getWordage()
            #print verbage
            verblen = len(verbage)
            #print verblen
            m = -1
            # while within a paragraph
            total = self.getStartLine()
            i = 0
            indent = False
            gotEndTag = False
            theWordage = verbage 
            moreChars = int(self.getCharsPerLine()*2)
            indent = True
            just = RichColumnar(theWordage,self.getCharsPerLine())
            lines = just.getLines()
            #print lines
            totalLines = just.countLines()
            p = 0 
            i = 0
            while p <= totalLines and i<self.getEndLine():
                if i >= self.getStartLine():
                    theLine = just.returnLine(p)
                    #print theLine
                    if  theLine[:4]=="----":
                        indent=True
                    else:
                        indent=False
                    if indent:
                        indent=False
                        #self.drawALine(c,x+8,y,theLine[4:],True)
                        y += 12 
                    else:
                        y += 12 
                p += 1
                i += 1
            theWordage = " "
            total += i
        y = totalLines * 8
        return y

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber,outline):
        """
        Test
        """
        #print "I AM HERE"
        #print self.Title()
        #xleft = parent.getLeft()
        #ytop = parent.getTop()
        (x,y) = self.getPosition()
        y = 1185 - y
	yorig = y
	xorig = x
	ox = xorig
	oy = yorig
	nx = ox
	ny = oy
        columncontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()
        obj=PDFPageTemplate(self.Title(),columncontainer)
        containerLeft = parent.getLeft()
        width = self.getCharsPerLine() * 6
        #result=obj.continuePDF(c,x,y+30,REQUEST,parent)
        articles = self.getArticle()
        output = []
        theParagraph = True 
        theCarrotStart = False
        theCarrotEnd = False
        theTagOpen = True
        theTag = ""
        theWordage = " "
        gotTheTag = False
        gotEndTag = False
        nasty = 'Â'
        for article in articles:
            #print article
            verbage = article.getWordage()
            print verbage
            verblen = len(verbage)
            #print verblen
            m = -1
            # while within a paragraph
            total = self.getStartLine()
            i = 0
            indent = False
            gotEndTag = False
            theWordage = verbage 
            moreChars = int(self.getCharsPerLine()*2)
            indent = True
            just = RichColumnar(theWordage,self.getCharsPerLine())
            lines = just.getLines()
            #print lines
            totalLines = just.countLines()
            p = 0 
            i = 0
            isHyperlink=False
            nextLineBold = False
            breakOccurred = False
            afterBreak = ""
	    isNewParagraph = False
            # if a Break Occurred special processing
            while p <= totalLines and i<self.getEndLine():
                if i >= self.getStartLine():
                    theLine = afterBreak
                    theLine += just.returnLine(p)
                    afterBreak = ""
                    if theLine.find('http') > -1:
                        hyperlink = theLine.split("/");
                        hyperLine = ""
                        for link in hyperlink:
                            hyperLine += link
                            hyperLine += "/"
                        hyperLine = hyperLine[:-4]
                        if len(hyperLine) > self.getCharsPerLine()-12:
                            httpPosition = hyperLine.find('http')
                            beginning = hyperLine[0:httpPosition]
                            firstLine = hyperLine[httpPosition:self.getCharsPerLine()-12]
                            secondLine = hyperLine[self.getCharsPerLine()-11:]	
                            savex = x
            		    (nx,ny) = self.drawALine(c,x,y,theLine,False,True)
	    	 	    if ox < nx:
	        	        ox = nx
	    		    if oy < ny:
				oy = ny
                            #x += httpPosition * 4.5
                            self.drawBold(c,x,y,firstLine,False,True)
                            x = savex
                            #y -= 12
                            self.drawBold(c,x,y,secondLine,False,True)
                        else:
                            self.drawBold(c,x,y,hyperLine,False,True)
                    elif theLine=="BREAK":
                        #self.drawALine(c,x,y,"",False,True)
                        y += 12
                        #breakOccurred = True
			isNewParagraph = True
			print "break Occurred"
                    elif theLine=="BOLD":
                        nextLineBold = True
                    else:
			if isNewParagraph:
			    isNewParagraph = False
			    (nx,ny) = self.drawALine(c,x,y,theLine,True,False)
			else:
			    (nx,ny) = self.drawALine(c,x,y,theLine,False,False)				
			if ox < nx:
			    ox = nx
			if oy < ny:
			    oy = ny
                    y -= 12 
                p += 1
                i += 1
            theWordage = " "
            total += i
        useContinuedOn = self.getUseContinuedOn()
        if useContinuedOn:
            theLine = self.getContinuedOn()
            (nx,ny) = self.drawALine(c,x,y,theLine,False)
	    if ox < nx:
		ox = nx
	    if oy < ny:
		oy = ny
        #newx = x + containerLeft
        newx = x + containerLeft
        if outline == True:
            sRed = 0
            sGreen = 1
            sBlue = 1            
            width = 7
            height = 7
            c.setFillColorRGB(sRed,sGreen,sBlue)
            c.setStrokeColorRGB(sRed,sGreen,sBlue)
            #c.rect(xorig,yorig,width,height,fill=1)
            #c.rect(ox,ny,width,height,fill=1)
	    c.rect(xorig,ny,abs(xorig-ox),abs(yorig-ny),fill=0)
            sRed = 1
            sGreen = 0
            sBlue = 0            
            c.setFillColorRGB(sRed,sGreen,sBlue)
            c.setStrokeColorRGB(sRed,sGreen,sBlue)
        return (x,y)

    def getJSON(self):
        """
        Test
        """
        json_items={}	
        json_items['charsPerLine']=self.getCharsPerLine()
        width = self.getCharsPerLine() * 6
        articles = self.getArticle()
        title = self.getId()
        theParagraph = True 
        theCarrotStart = False
        theCarrotEnd = False
        theTagOpen = True
        theTag = ""
        theWordage = " "
        gotTheTag = False
        gotEndTag = False
        nasty = 'Â'
        for article in articles:
            #print article
            verbage = article.getWordage()
            #print verbage
            verblen = len(verbage)
            #print verblen
            m = -1
            # while within a paragraph
            total = self.getStartLine()
            i = 0
            indent = False
            gotEndTag = False
            theWordage = verbage 
            moreChars = int(self.getCharsPerLine()*2)
            indent = True
            just = RichColumnar(theWordage,self.getCharsPerLine())
            lines = just.getLines()
            #print lines
            totalLines = just.countLines()
            json_items['totalLines']=just.countLines()
            p = 0 
            i = 0
            json_lines = {}
            while p <= totalLines and i<self.getEndLine():
                if i >= self.getStartLine():
                    theLine = just.returnLine(p)
                    #print theLine
                    if  theLine[:4]=="----":
                        indent=True
                    else:
                        indent=False
                    if indent:
                        indent=False
                        s = theLine[4:]
                        s = s.decode('utf-8')
                        t = u""
                        for ii in s:
                            if ord(ii) in entity.codepoint2name:
                                name = entity.codepoint2name.get(ord(ii))
                                it = "&" + name + ';'
                                t += it	
                            else:
                                t += ii
                        json_lines[i]=t
                    else:
                        s=theLine.decode('utf-8')
                        t = u""
                        for ii in s:
                            if ord(ii) in entity.codepoint2name:
                                name = entity.codepoint2name.get(ord(ii))
                                it = "&" + name + ';'
                                t += it	
                            else:
                                t += ii
                        json_lines[i]=t
                p += 1
                i += 1
            theWordage = " "
            total += i
        useContinuedOn = self.getUseContinuedOn()
        if useContinuedOn:
            theLine = self.getContinuedOn()
            json_lines[i]=theLine
        #newx = x + containerLeft
        json_items['type']='RichColumn'
        json_items['name']=title
        json_items['lines']=json_lines
        json_items['article']=self.getArticle()[0].getId()
        json_items['startLine']=self.getStartLine()
        json_items['endLine']=self.getEndLine()
        json_items['useRemainder']=self.getUseRemainder()
        json_items['useContinuedOn']=self.getUseContinuedOn()
        json_items['continuedOn']=self.getContinuedOn()
        json_items['useContinuedFrom']=self.getUseContinuedFrom()
        json_items['continuedFrom']=self.getContinuedFrom()
        json_items['charsPerLine']=self.getCharsPerLine()
        json_items['textclass']=self.getTextclass()
        json_items['addLineHeight']=self.getAddLineHeight()
        json_items['elements']=super(RichColumn,self).getJSON()
        return json_items

    def drawBold(self,c,x,y,theLine,indent=False,space=True):
        words = theLine.split()
        totalWordLength = 0
        allwords=[]
        for word in words:
            allwords.append(word)
        for word in allwords:
            #print "error"
            #print word
            theWord = ""
            nasty = '\xC0\x82'
            #for letter in word:
            #    if letter <  nasty:
            #        theWord += letter
            #theWord = theWord.decode('latin-1')
            #theWord = unicode(word,'latin-1')
            totalWordLength += c.stringWidth(word,"DejaVu",11)
            lineLength = 3.8 * self.getCharsPerLine()
        if len(allwords) > 3:
            whiteSpace = (lineLength - totalWordLength) / (len(allwords)-1)
            #whiteSpace = (lineLength - totalWordLength) / (len(allwords) - 1)
        else:
            whiteSpace = 10
        textobject = c.beginText()
        textobject.setFont("Bold",10)
        for word in allwords:
            theWord = ""
            nasty = '\xC0\x82'
            for letter in word:
                theWord += letter
            #theWord = theWord.decode('latin-1')
            #theWord = unicode(word,'latin-1')
            stringWidth = c.stringWidth(word,"Times-Roman",11)
            textobject.setTextOrigin(x,y)
            textobject.textLine(word)
            x += stringWidth
            if space==True:
                x += 2
            else:
                x += whiteSpace 
        c.drawText(textobject)
        #print "drawText"
        #print textobject
        y+=4
        return (x,y)

    def drawALine(self,c,x,y,theLine,indent=False,space=True,outline=False):
        if outline == True:
            sRed = 0
            sGreen = 1
            sBlue = 0            
            left = x
            top = y
            width = 3
            height = 3
            c.setFillColorRGB(sRed,sGreen,sBlue)
            c.setStrokeColorRGB(sRed,sGreen,sBlue)
            c.rect(left,top,width,height,fill=0)
            sRed = 1
            sGreen = 0
            sBlue = 0            
            c.setFillColorRGB(sRed,sGreen,sBlue)
            c.setStrokeColorRGB(sRed,sGreen,sBlue)
        words = theLine.split()
        totalWordLength = 0
        allwords=[]
        for word in words:
            allwords.append(word)
        for word in allwords:
            #print "error"
            #print word
            theWord = ""
            nasty = '\xC0\x82'
            #for letter in word:
            #    if letter <  nasty:
            #        theWord += letter
            #theWord = theWord.decode('latin-1')
            #theWord = unicode(word,'latin-1')
            totalWordLength += c.stringWidth(word,"Times-Roman",11)
	adjust = 0
        #if indent:
        #    lineLength = (3.8 * (self.getCharsPerLine()-adjust))-8 
        #else:
        #    lineLength = 3.8 * (self.getCharsPerLine()-adjust )
	lineLength = 3.8 * self.getCharsPerLine()
	addIndent = False
	closeLine = False
	if len(allwords) > 1:
	#whiteSpace = (lineLength - totalWordLength) / (len(allwords))
	    whiteSpace = (lineLength - totalWordLength) / (len(allwords) - 1)
	    #if whiteSpace > 20:
	    #	lineLength -= 30
	    #	whiteSpace = (lineLength - totalWordLength) / (len(allwords) - 1)
	    #	addIndent = True
	    if indent == True:
		x += 30
		lineLength -= 30
		whiteSpace = (lineLength - totalWordLength) / (len(allwords) - 1)
	    elif whiteSpace > 20:
		closeLine = True
		whiteSpace = 5
        else:
            whiteSpace = 10
        sRed = 0
        sGreen = 0
        sBlue = 0            
        c.setFillColorRGB(sRed,sGreen,sBlue)
        c.setStrokeColorRGB(sRed,sGreen,sBlue)
        textobject = c.beginText()
        textobject.setFont("Times-Roman",11)
	#if whiteSpace > 10:
	#    x += 10
	#if addIndent == True:
	#    x += 30
        for word in allwords:
            theWord = ""
            nasty = '\xC0\x82'
            for letter in word:
                theWord += letter
            #theWord = theWord.decode('latin-1')
            #theWord = unicode(word,'latin-1')
            stringWidth = c.stringWidth(word,"Times-Roman",11)
            textobject.setTextOrigin(x,y)
            textobject.textLine(word)
            x += stringWidth
            if space==True:
                x += 2
            else:
                x += whiteSpace 
        c.drawText(textobject)
        #print "drawText"
        print textobject
        #y+=4
        nx = x - whiteSpace
        ny = y
        if outline == True:
            sRed = 0
            sGreen = 1
            sBlue = 0            
            left = nx
            top = ny
            width = 3
            height = 3
            c.setFillColorRGB(sRed,sGreen,sBlue)
            c.setStrokeColorRGB(sRed,sGreen,sBlue)
            c.rect(left,top,width,height,fill=0)
            sRed = 1
            sGreen = 0
            sBlue = 0            
            c.setFillColorRGB(sRed,sGreen,sBlue)
            c.setStrokeColorRGB(sRed,sGreen,sBlue)
        return (nx,ny)

    def drawALineold(self,c,x,y,theLine,indent=False,space=True,adjust=0):
        words = theLine.split()
        totalWordLength = 0
        allwords=[]
        for word in words:
            allwords.append(word)
        for word in allwords:
            #print "error"
            #print word
            theWord = ""
            nasty = '\xC0\x82'
            #for letter in word:
            #    if letter <  nasty:
            #        theWord += letter
            #theWord = theWord.decode('latin-1')
            #theWord = unicode(word,'latin-1')
            totalWordLength += c.stringWidth(word,"Times-Roman",11)
        if indent:
            lineLength = (3.8 * (self.getCharsPerLine()-adjust))-8 
        else:
            lineLength = 3.8 * (self.getCharsPerLine()-adjust )
        if len(allwords) > 3:
            whiteSpace = (lineLength - totalWordLength) / (len(allwords)-1)
            #whiteSpace = (lineLength - totalWordLength) / (len(allwords) - 1)
        else:
            whiteSpace = 10
        textobject = c.beginText()
        textobject.setFont("Times-Roman",11)
        for word in allwords:
            theWord = ""
            nasty = '\xC0\x82'
            for letter in word:
                theWord += letter
            #theWord = theWord.decode('latin-1')
            #theWord = unicode(word,'latin-1')
            stringWidth = c.stringWidth(word,"Times-Roman",11)
            textobject.setTextOrigin(x,y)
            textobject.textLine(word)
            x += stringWidth
            if space==True:
                x += 2
            else:
                x += whiteSpace 
        c.drawText(textobject)
        #print "drawText"
        #print textobject
        #y+=4
        return (x,y)

    def getSkinName(self):
        """
        TEST
        """
        return "showColumn"

    def getAuthor(self):
        """
        Return Link
        """
        articles = self.getArticle()
        for article in articles:
            author = article.getAuthor()
            return author 

    def getArticleId(self):
        """
        Return Link
        """
        articles = self.getArticle()
        for article in articles:
            article = article.getArticleId()
            return article

    def getSnapshot(self,width,height,numberOfColumns=1):
        """
        Test
        """
        diagnostic = "<div>RichColumn: getSnapshot</div>"
        diagnostic += "<div>    height: %i px</div>" % height
        diagnostic += "<div>    12pt is 16px</div>"
        numberOfLines = int(height / 16)
        displayHeight = int((height * 1.7))
        diagnostic += "<div>    number of lines: %i</div>" % numberOfLines
        rich = "<div class='richcolumn'>"
        articles = self.getArticle()
        theWordage = ""
        for article in articles:
            theWordage = article.getWordage()
        # get rid of tags
        theVerbage = re.sub("<.>","",theWordage)
        theVerbage2 = re.sub("<\/.>","",theVerbage)
        wordlen = len(theVerbage2)
        m = -1
        linitr = 1
        columnWidth = 50 * numberOfColumns
        just = RichColumnar(theVerbage2,columnWidth)
        lines = just.getLines()
        #print lines
        totalLines = just.countLines()
        p = 0 
        verbage = ""
        #width *= numberOfColumns
        #theStyle='width:'+str(width)+'px;height:'+str(displayHeight)+'px;background-color:white;text-align:justify;font-size:12pt'
        theStyle='text-align:justify;font-size:12pt'
        rich = ""
        rich += "<div style='"+theStyle+"' class='richline'>"
        #totalLines *= 4
        while p <= totalLines:
            verbage=just.returnLine(p)
            #rich += verbage
            #rich += diagnostic 
            rich += verbage.decode('utf-8')
            #deduct from height
            deduction = 32 * 4 / (3 * width / 320)
            height -= deduction
            if height <= 0:
                break
            p+=1
        rich += "</div>"
        return (rich,0,0)

    def alltext(self,width,height):
        """
        Test
        """
        rich = "<div class='richcolumn'>"
        articles = self.getArticle()
        for article in articles:
            theWordage = article.getWordage()
        # get rid of tags
        theVerbage = re.sub("<.>","",theWordage)
        theVerbage2 = re.sub("<\/.>","",theVerbage)
        wordlen = len(theVerbage2)
        m = -1
        linitr = 1
        columnWidth = 50
        just = RichColumnar(theVerbage2,columnWidth)
        lines = just.getLines()
        #print lines
        totalLines = just.countLines()
        p = 0 
        verbage = ""
        linewidth = width * 1.2
        theStyle='width:'+str(linewidth)+'px;text-align:justify;font-size:12pt'
        rich += "<div style='"+theStyle+"' class='richline'>"
        while p <= totalLines:
            verbage=just.returnLine(p)
            rich += verbage.decode('utf-8')
            p += 1
        rich += "</div>"
        rich += "</div>"
        return rich

    def getType(self):
        """
        Test
        """
        return "RichColumn"

    def returnTextClass(self):
        """
        TEST
        """
        return self.getTextclass()

    def returnLines(self):
        """
        Test
        """
        articles = self.getArticle()
        output = []
        theParagraph = True 
        theCarrotStart = False
        theCarrotEnd = False
        theTagOpen = True
        theTag = ""
        theWordage = " "
        gotTheTag = False
        theLine = ""
        #nasty = 'Â'
        for article in articles:
            verbage = article.getWordage()
            verblen = len(verbage)
            m = -1
            theString = ""
            # while within a paragraph
            print verbage
            while m < verblen-1:
                m += 1
                theChar = verbage[m]
                theString += theChar
                if theChar == '<':
                    theTag = ""
                    theCarrotStart = True
                    gotTheTag = True
                    gotTheTag = False 
                    theWordage += '\t'
                elif theChar == '/':
                    theTagOpen = False
                    theCarrotStart = False
                    gotTheTag = True
                    gotTheTag = False 
                    theWordage += '\t'
                elif theChar == '>':
                    theCarrotEnd = True
                    theCarrotStart = False
                    #print "the tag %s" % theTag
                    gotTheTag = False 
                    theWordage += '\t'
                elif theCarrotStart and theChar != "<":
                    theTag += theChar
                    gotTheTag = True
                elif not gotTheTag:
                    #if theChar != nasty:
                    theWordage += theChar
                elif theCarrotEnd == True and theTagOpen == False:
                    #print "wordage %s" % theWordage
                    useWordage = '\t'
                    useWordage += theWordage
                    theCarrotEnd = False
                    theTagOpen = True
                    moreChars = int(self.getCharsPerLine * 0.5)
                    #just = RichColumnar(theWordage,self.getCharsPerLine())
                    just = RichColumnar(useWordage,moreChars)
                    lines = just.getLines()
                    totalLines = just.countLines()
                    i = self.getStartLine()
                    while i<=totalLines and i<self.getEndLine():
                        theLine = just.returnLine(i)
                        output.append(theLine)
                        i += 1
                    #theWordage = " "
                useContinuedOn = self.getUseContinuedOn()
                if useContinuedOn:
                    theLine = self.getContinuedOn()
            output.append(theLine)
            print theString
        return output


registerType(RichColumn, PROJECTNAME)
# end of class Column

##code-section module-footer #fill in your manual code here
##/code-section module-footer
