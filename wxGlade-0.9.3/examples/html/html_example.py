#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0a9 on Mon Dec  4 21:53:58 2017
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import wx.html
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.button_back = wx.Button(self.panel_1, wx.ID_ANY, "<--")
        self.button_forward = wx.Button(self.panel_1, wx.ID_ANY, "-->")
        self.text_url = wx.TextCtrl(self.panel_1, wx.ID_ANY, "../../docs/html/index.html")
        self.button_go = wx.Button(self.panel_1, wx.ID_ANY, "Open")
        self.html = wx.html.HtmlWindow(self.panel_1, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, lambda event: self.html.HistoryCanBack() and self.html.HistoryBack(), self.button_back)
        self.Bind(wx.EVT_BUTTON, lambda event: self.html.HistoryCanForward() and self.html.HistoryForward(), self.button_forward)
        self.Bind(wx.EVT_BUTTON, lambda event:self.html.LoadPage( self.text_url.GetValue() ), self.button_go)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("html example")
        self.button_back.SetMinSize((30, -1))
        self.button_forward.SetMinSize((30, -1))
        self.button_go.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.button_back, 0, 0, 0)
        sizer_3.Add(self.button_forward, 0, 0, 0)
        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Location:")
        sizer_3.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        sizer_3.Add(self.text_url, 1, 0, 0)
        sizer_3.Add(self.button_go, 0, 0, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Note: HtmlWindow can only handle http, so most of the time you'll see a Moved Permanently")
        label_2.SetForegroundColour(wx.Colour(255, 0, 0))
        sizer_2.Add(label_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(self.html, 1, wx.ALL | wx.EXPAND, 3)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.SetSize((800, 600))
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()