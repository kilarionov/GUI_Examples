// -*- C++ -*-
//
// generated by wxGlade
//
// Example for compiling a single file project under Linux using g++:
//  g++ MyApp.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp
//
// Example for compiling a multi file project under Linux using g++:
//  g++ main.cpp $(wx-config --libs) $(wx-config --cxxflags) -o MyApp Dialog1.cpp Frame1.cpp
//

#include "bug184.h"

// begin wxGlade: ::extracode
// end wxGlade



Bug184_Frame::Bug184_Frame(wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style):
    wxFrame(parent, id, title, pos, size, style)
{
    // begin wxGlade: Bug184_Frame::Bug184_Frame
    label_1 = new wxStaticText(this, wxID_ANY, _("Just a label"));

    set_properties();
    do_layout();
    // end wxGlade
}


void Bug184_Frame::set_properties()
{
    // begin wxGlade: Bug184_Frame::set_properties
    SetTitle(_("frame_1"));
    SetBackgroundColour(wxSystemSettings::GetColour(wxSYS_COLOUR_BACKGROUND));
    // end wxGlade
}


void Bug184_Frame::do_layout()
{
    // begin wxGlade: Bug184_Frame::do_layout
    wxBoxSizer* sizer_1 = new wxBoxSizer(wxVERTICAL);
    sizer_1->Add(label_1, 1, wxALIGN_CENTER|wxALL|wxEXPAND, 5);
    SetSizer(sizer_1);
    sizer_1->Fit(this);
    Layout();
    // end wxGlade
}


class MyApp: public wxApp {
public:
    bool OnInit();
protected:
    wxLocale m_locale;  // locale we'll be using
};

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
    m_locale.Init();
#ifdef APP_LOCALE_DIR
    m_locale.AddCatalogLookupPathPrefix(wxT(APP_LOCALE_DIR));
#endif
    m_locale.AddCatalog(wxT(APP_CATALOG));

    wxInitAllImageHandlers();
    Bug184_Frame* Frame184 = new Bug184_Frame(NULL, wxID_ANY, wxEmptyString);
    SetTopWindow(Frame184);
    Frame184->Show();
    return true;
}
