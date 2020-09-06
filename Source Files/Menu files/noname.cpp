///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	m_mgr.SetManagedWindow(this);
	m_mgr.SetFlags(wxAUI_MGR_DEFAULT);
	
	m_textCtrl2 = new wxTextCtrl( this, wxID_ANY, wxT("fffff"), wxDefaultPosition, wxDefaultSize, 0 );
	m_mgr.AddPane( m_textCtrl2, wxAuiPaneInfo() .Top() .CaptionVisible( false ).CloseButton( false ).PaneBorder( false ).Movable( false ).Dock().Resizable().FloatingSize( wxSize( 240,82 ) ).LeftDockable( false ).RightDockable( false ).Floatable( false ).Position( 10 ) );
	
	m_button1 = new wxButton( this, wxID_ANY, wxT("Search"), wxDefaultPosition, wxDefaultSize, 0 );
	m_mgr.AddPane( m_button1, wxAuiPaneInfo() .Bottom() .CloseButton( false ).Movable( false ).Dock().Resizable().FloatingSize( wxDefaultSize ).TopDockable( false ).LeftDockable( false ).RightDockable( false ).Floatable( false ) );
	
	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("Enter A Search Term"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTRE );
	m_staticText1->Wrap( -1 );
	m_mgr.AddPane( m_staticText1, wxAuiPaneInfo() .Top() .CaptionVisible( false ).CloseButton( false ).PinButton( true ).Dock().Resizable().FloatingSize( wxDefaultSize ) );
	
	
	m_mgr.Update();
	this->Centre( wxBOTH );
}

MyFrame1::~MyFrame1()
{
	m_mgr.UnInit();
	
}
