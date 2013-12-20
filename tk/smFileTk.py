#coding: gb2312
import os
from os.path import walk, join, normpath
from os import getcwd
import string
import re
import time

import wx

#����Ҫ�õ����ļ������ļ����Ҽ��������ܷŵ�����
#ע�⣺�����õ���������ʽ��ͨ���������Windows��ͨ���
#���磺Ҫ�����ļ����У�������Ŀ¼�У����е�.tif�ļ���ͨ����������ģ�".*\.tif"
#ƥ���ַ���������/Z�����磺r'.*\.tif/Z'
#���ﲻ���ִ�Сд��ƥ����������һ��������re.I�������������ȥ�������ִ�Сд
class Folder:
    def __init__(self, path = ''):
        self.path = path
        self.reMatch = ''
        self.FileLists = []

    #visit�ǻص���������Ҫֱ�ӵ���
    def visit(self, arg, dirname, names):
        for file in names:
            files=normpath(join(dirname, file))
            if re.match(self.reMatch,file,re.I):
                self.FileLists.append(files)

    #����ͨ������ļ����з���Ҫ����ļ������ҳ�������䵽FileLists��
    def GetFileLists(self):
        self.FileLists = []
        os.path.walk(self.path, self.visit,0)

    #�����ļ���ѡ�����ѡ���ļ���
    #��Ҫ���Ȱ�װ��wxPython
    #���ô˺���֮ǰ��Ҫ����wx.App�������磺app = wx.App(False)��ֻҪ����һ�У��Ϳ��Ե����������
    def Choose(self):
        dialog = wx.DirDialog(None, 'ѡ���ļ���',style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        dialog.SetPath(os.getcwd())

        if dialog.ShowModal() == wx.ID_OK:
            self.path = dialog.GetPath()
        
        dialog.Destroy()
        return self.path

class File:
    #mode������������
    #r = ֻ����
    #rb = �Զ����Ʒ�ʽֻ����
    #w = ��д��ʽ��
    #wb = �Զ����ƿ�д��ʽ��
    #w+ = ��׷�ӷ�ʽ��
    def __init__(self, fileName = '', mode = 'r'):
        self.fileName = fileName
        self.mode = mode
        self.file = None
        self.bOpen = 0

    #��������
    def __del__(self):
        if self.bOpen:
            self.file.close()
            self.file = None
            self.bOpen = 0

    def Choose(self):
        dlg = wx.FileDialog(None, 
                            message="���ļ�",
                            wildcard="PNG(*.png)|*.png" ,
                            style=wx.OPEN
                            )
        if dlg.ShowModal() == wx.ID_OK:
            self.fileName = dlg.GetPath()
            
        dlg.Destroy()
        return self.fileName



    #���ļ�
    def Open(self):
         self.file = open(self.fileName, self.mode)
         self.bOpen = 1

    #��ȡ�ı��ļ��е�������
    def ReadLines(self):
        if not self.bOpen:
            return []
        else:
            return self.file.readlines()

    #���ı��ļ��ж�ȡһ��
    def ReadLine(self):
        if not self.bOpen:
            return ''
        else:
            return self.file.readline()

    #���ı��ļ���д��һ��
    def WriteLine(self, str):
        if self.bOpen:
            return self.file.write(str+'\n')

    def Write(self, str):
        if self.bOpen:
            return self.file.write(str)

    def WriteLines(self, str):
        if self.bOpen:
            return self.file.writelines(str)

    #�ر��ļ�
    def Close(self):
        if self.bOpen:
            self.file.close()
            self.file = None
            self.bOpen = 0

    #�������ļ�
    def Rename(self, newName):
        if self.bOpen:
            self.file.close()
            os.rename()


def ChooseFolder(strTitle):
    dialog = wx.DirDialog(None, strTitle,style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    dialog.SetPath(os.getcwd())
    path = ''
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
        
    dialog.Destroy()
    return path

def ChooseOpenFile(strTitle, wc = '�����ļ�(*.*)|*.*'):
    dlg = wx.FileDialog(None, 
                        message=strTitle,
                        wildcard=wc ,
                        style=wx.OPEN
                        )
    if dlg.ShowModal() == wx.ID_OK:
        fileName = dlg.GetPath()
            
    dlg.Destroy()
    return fileName

def ChooseSaveFile(strTitle, wc = '�����ļ�(*.*)|*.*'):
    dlg = wx.FileDialog(None, 
                        message=strTitle,
                        wildcard=wc ,
                        style=wx.SAVE
                        )
    if dlg.ShowModal() == wx.ID_OK:
        fileName = dlg.GetPath()
            
    dlg.Destroy()
    return fileName