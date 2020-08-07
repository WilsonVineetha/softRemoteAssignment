#!/usr/bin/python

import xml.dom.minidom

from Tkinter import Frame, Label,Entry,Button
from Tkinter import Tk, StringVar, BOTH, W, E
#import TkinterMessageBox 

import sys

def printf (format, *args):
        sys.stdout.write (format % args)

def fprintf (fp, format, *args):
        fp.write (format % args)

# get an XML element with specified name
def getElement (parent,name):
    nodeList = []
    if parent.childNodes:
       for node in parent.childNodes:
          if node.nodeType == node.ELEMENT_NODE:
             if node.tagName == name:
                nodeList.append (node) 
    return nodeList[0]

# get value of an XML element with specified name
def getElementValue (parent,name):
    if parent.childNodes:
       for node in parent.childNodes:
          if node.nodeType == node.ELEMENT_NODE:
             if node.tagName == name:
                if node.hasChildNodes:
                   child = node.firstChild
                   return child.nodeValue
    return None

# set value of an XML element with specified name
def setElementValue (parent,name,value):
    if parent.childNodes:
       for node in parent.childNodes:
          if node.nodeType == node.ELEMENT_NODE:
             if node.tagName == name:
                if node.hasChildNodes:
                   child = node.firstChild
                   child.nodeValue = value
    return None

class Application (Frame):

  def __init__(self, parent):

      # initialize frame
      Frame.__init__(self,parent)

      # set root as parent
      self.parent = parent

      # read and parse XML document
      DOMTree = xml.dom.minidom.parse ("config.xml")

      # create attribute for XML document
      self.xmlDocument = DOMTree.documentElement

      # get value of "RemoteCompany" element
      self.RemoteCompany = StringVar()
      self.RemoteCompany.set (getElementValue (self.xmlDocument,"RemoteCompany"))

      # get value of "RemoteType" element
      self.RemoteType = StringVar()
      self.RemoteType.set (getElementValue (self.xmlDocument,"UNIVERSAL"))

      # create attribute for "FALCON" element
      self.xmlFALCON = getElement (self.xmlDocument,"FALCON")
     
      # create attribute for "BUTTONS" element 
      self.xmlBUTTONS = getElement (self.xmlFALCON,"BUTTONS")

      # get value of "KEY1" element
      self.KEY1 = StringVar()
      self.KEY1.set (getElementValue (self.xmlBUTTONS,"KEY1"))

      # get value of "KEY2" element
      self.KEY2 = StringVar()
      self.KEY2.set (getElementValue (self.xmlBUTTONS,"KEY2"))

      # get value of "service_name" element
      self.POWER = StringVar()
      self.POWER.set (getElementValue (self.xmlBUTTONS,"POWER"))

      # initialize UI
      self.initUI()

  def initUI(self):
      # set frame title
      self.parent.title ("Softremote")

      # pack frame
      self.pack (fill=BOTH, expand=1)

      # configure grid columns
      self.columnconfigure (0, pad=3)
      self.columnconfigure (1, pad=3)

      # configure grid rows
      self.rowconfigure (0, pad=3)
      self.rowconfigure (1, pad=3)
      self.rowconfigure (2, pad=3)
      self.rowconfigure (3, pad=3)
      self.rowconfigure (4, pad=3)
      self.rowconfigure (6, pad=3)

      # remote company
      label1 = Label (self,text = "Remote company: ")
      label1.grid (row=0,column=0,sticky=W)

      entry1 = Entry (self,width=30,textvariable = self.RemoteCompany)
      entry1.grid (row=0,column=1)

      # Remote Type
      label2 = Label (self,text = "Remote Type : ")
      label2.grid (row=1,column=0,sticky=W)

      entry2 = Entry (self,width=30,textvariable = self.RemoteType)
      entry2.grid (row=1,column=1)

      # KEY1
      label3 = Label (self,text = "KEY1 : ")
      label3.grid (row=3,column=0,sticky=W)

      entry3 = Entry (self,width=30,textvariable = self.KEY1)
      entry3.grid (row=3,column=1)

      # KEY2
      label4 = Label (self,text = "KEY2 : ")
      label4.grid (row=4,column=0,sticky=W)

      entry4 = Entry (self,width=30,textvariable = self.KEY2)
      entry4.grid (row=4,column=1)

      # POWER
      label4 = Label (self,text = "POWER : ")
      label4.grid (row=5,column=0,sticky=W)

      entry4 = Entry (self,width=30,textvariable = self.POWER)
      entry4.grid (row=5,column=1)

      # blank line
      label6 = Label (self,text = "")
      label6.grid (row=5,column=0,sticky=E+W)

      # create OK button 
      button1 = Button (self, text="OK", command=self.onOK)
      button1.grid (row=6,column=0,sticky=E)

      # create Cancel button
      button2 = Button (self, text="Cancel", command=self.onCancel)
      button2.grid (row=6,column=1,sticky=E)

  def onOK(self): 

      # set values in xml document
      setElementValue (self.xmlDocument,"RemoteCompany",self.RemoteCompany.get())
      setElementValue (self.xmlDocument,"RemoteType",self.RemoteType.get())
      setElementValue (self.xmlService,"KEY1",self.KEY1.get())
      setElementValue (self.xmlService,"KEY2",self.KEY2.get())
      setElementValue (self.xmlService,"POWER",self.POWER.get())

      # open XML file
      f = open ("config.xml","w")

      # set xml header
      fprintf (f,'<?xml version="1.0" encoding="utf-8"?>\n')

      # write XML document to XML file
      self.xmlDocument.writexml (f)

      # close XML file
      f.close ()

      # show confirmation message
      tkMessageBox.showerror ("Message","Configuration updated successfully")

      # exit program
      self.quit();

  def onCancel(self): 

      # exit program
      self.quit();

def main():

   # initialize root object
   root = Tk()

   # set size of frame
   root.geometry ("410x160+300+300")

   # call object
   app = Application (root)

   # enter main loop
   root.mainloop()

# if this is the main thread then call main() function
if __name__ == '__main__':
   main ()
