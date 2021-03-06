import wx

class Path(object):
    def paint(self,gc):
        print "Path Drawn"
        gc.SetPen(wx.Pen("#000000",1))
        path=gc.CreatePath()
        path.MoveToPoint(wx.Point2D(10,10))
        path.AddCurveToPoint(wx.Point2D(10,50),
                             wx.Point2D(10,150),
                             wx.Point2D(100,100))
#         gc.DrawPath(path)
        gc.SetPen(wx.Pen("red",1))
#         path=gc.CreatePath()
        path.MoveToPoint(wx.Point2D(10,10))
        #path.AddLineToPoint(wx.Point2D(100,100))
        path.AddRoundedRectangle(100.0,100.0,10.0,10.0,5.0)
        gc.DrawPath(path)


class TestPane(wx.Panel):
    def __init__(self,parent=None,id=-1):
        wx.Panel.__init__(self,parent,id,style=wx.TAB_TRAVERSAL)
        self.SetBackgroundColour("#FFFFFF")
        self.Bind(wx.EVT_PAINT,self.onPaint)
        #self.SetDoubleBuffered(True)
        self.path=Path()
		
    def onPaint(self, event):
        event.Skip()

        dc=wx.PaintDC(self)
        dc.BeginDrawing()
        gc = wx.GraphicsContext.Create(dc)

        gc.PushState()
        self.path.paint(gc)
        gc.PopState()
        dc.EndDrawing()

    def drawTestRects(self,dc):
        dc.SetBrush(wx.Brush("#000000",style=wx.SOLID))
        dc.DrawRectangle(50,50,50,50)
        dc.DrawRectangle(100,100,100,100)

class TestFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(640,480))
        self.mainPanel=TestPane(self,-1)

        self.Show(True)


app = wx.App(False)
frame = TestFrame(None,"Test App")
app.MainLoop()
