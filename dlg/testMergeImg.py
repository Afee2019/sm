#coding: gb2312

import mergeImgs as frm
import wx
app = wx.App(False)

win = frm.mergeImgs(None, -1, "ƴ��Ӱ���ļ�", size=(600, 400),
                  style = wx.DEFAULT_FRAME_STYLE)
win.Show(True)
app.MainLoop()

