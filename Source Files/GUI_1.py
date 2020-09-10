# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Image Search", pos = wx.DefaultPosition, size = wx.Size( 376,128 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Enter a Search Term", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_mgr.AddPane( self.m_staticText3, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.m_textCtrl3, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.m_button1, wx.aui.AuiPaneInfo() .Center() .CaptionVisible( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
		
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrl3.Bind( wx.EVT_TEXT, self.Search_Term_feild )
		self.m_button1.Bind( wx.EVT_BUTTON, self.Search_Site )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	
	
	# Virtual event handlers, overide them in your derived class
	def Search_Term_feild( self, event ):
		event.Skip()
	
	def Search_Site( self, event ):
		event.Skip()
	

