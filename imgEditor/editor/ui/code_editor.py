import wx.richtext
import weakref
import wx

from editor.constants import *


class Panel(wx.Panel):

    def __init__(self, parent, fileName):
        wx.Panel.__init__(self, parent, -1)

        self.fileName = os.path.join(PROCESSING_DIR, fileName)

        sizer = wx.BoxSizer(wx.VERTICAL)

        codeEditor = wx.richtext.RichTextCtrl(self, style=wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER)
        self.codeEditor = weakref.ref(codeEditor)
        codeEditor.LoadFile(self.fileName, type=wx.richtext.RICHTEXT_TYPE_TEXT)
        sizer.Add(codeEditor, proportion=2, flag=wx.EXPAND)
        sizer.Add((0,10), proportion=0)  # spacer

        stdOut = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.TE_READONLY)
        self.stdOut = weakref.ref(stdOut)
        sizer.Add(stdOut, proportion=1, flag=wx.EXPAND)

        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        sizer.Fit(self)


    def saveCode(self):
        self.codeEditor().SaveFile(self.fileName, type=wx.richtext.RICHTEXT_TYPE_TEXT)


    def clearOutput(self):
        self.stdOut().Clear()


    def grabOutput(self):
        sys.stdout = self.stdOut()
        sys.stderr = self.stdOut()
