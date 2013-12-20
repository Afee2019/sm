#coding: gb2312

import os
import wx
import Toolkit.smFileTk as tk

app = wx.App(False)

folder = tk.ChooseSaveFile('保存文件')

print folder