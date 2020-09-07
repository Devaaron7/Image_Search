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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 449,176 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.m_textCtrl2, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.Size( 240,82 ) ).LeftDockable( False ).RightDockable( False ).Floatable( False ).Position( 10 ) )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.m_button1, wx.aui.AuiPaneInfo() .Bottom() .CloseButton( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).TopDockable( False ).LeftDockable( False ).RightDockable( False ).Floatable( False ) )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enter A Search Term", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_mgr.AddPane( self.m_staticText1, wx.aui.AuiPaneInfo() .Top() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
		
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Start_Search )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	
	
	# Virtual event handlers, overide them in your derived class
	def Start_Search( self, event ):
		event.Skip()
	

