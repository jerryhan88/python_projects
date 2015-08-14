from __future__ import division
from parameter_function import container_hs, container_vs, l_sx, change_b_color
import wx
class Storage(object):
    def __init__(self):
        self.id, self.name = None, None
        self.px, self.py = None, None
        self.holding_containers = {}
    def __repr__(self):
        return self.name + str(self.id)
    def draw(self, gc):
        pass
    
class QB(Storage):
    sy = container_vs * 2.2
    v_c_pos_info = sy / 2
    def __init__(self, id, px, py):
        Storage.__init__(self)
        self.name, self.id = 'QC Buffer', id
        self.px, self.py = px, py
    def draw(self, gc, id_show):
        gc.SetPen(wx.Pen(wx.Colour(251, 194, 0), 0.5))
        gc.DrawLines([(0, 0), (l_sx, 0)])
        gc.DrawLines([(0, QB.sy), (l_sx, QB.sy)])
        for c in self.holding_containers.values():
            old_tr = gc.GetTransform()
            gc.Translate(c.px, c.py)
            c.draw(gc)
            gc.SetTransform(old_tr)
        if id_show:
            gc.SetFont(wx.Font(5, wx.SWISS, wx.NORMAL, wx.NORMAL))
            gc.DrawText(str(self.name + '-' + str(self.id)), -container_hs, -container_hs)
class TP(Storage):
    num_of_stacks = 8
    sx, sy = container_vs * 1.2, container_hs * 1.2
    bay_pos_info = sy / 2
    stack_pos_info = {}
    for x in xrange(num_of_stacks):
        if x < 4:
            stack_pos_info[x + 1] = sx / 2 + container_vs * x * 2
        else:
            stack_pos_info[x + 1] = sx / 2 + container_vs * (x - 4) * 2
    def __init__(self, id, px, py):
        Storage.__init__(self)
        self.name, self.id = 'TP', id
        self.px, self.py = px, py
        mg = 2
        self.bg_ps = [(-mg, -mg),
                      (container_vs * TP.num_of_stacks / 2 + TP.sx * 2.6 + mg, -mg),
                      (container_vs * TP.num_of_stacks / 2 + TP.sx * 2.6 + mg, TP.sy + mg + container_hs * 1.2),
                      (-mg, TP.sy + mg + container_hs * 1.2)
                      ]
        
    def draw(self, gc, id_show):
        gc.SetPen(wx.Pen(wx.Colour(210, 209, 208), 0))
        gc.SetBrush(wx.Brush(wx.Colour(210, 209, 208)))
        gc.DrawLines(self.bg_ps)
        gc.SetPen(wx.Pen(wx.Colour(100, 100, 100), 0.5))
        for s_px in TP.stack_pos_info.values() :
            gc.DrawLines([(s_px - TP.sx / 2, 0), (s_px + TP.sx / 2, 0)])
            gc.DrawLines([(s_px - TP.sx / 2, TP.sy), (s_px + TP.sx / 2, TP.sy)])
            gc.DrawLines([(s_px - TP.sx / 2, 0), (s_px - TP.sx / 2, TP.sy)])
            gc.DrawLines([(s_px + TP.sx / 2, 0), (s_px + TP.sx / 2, TP.sy)])
            
            gc.DrawLines([(s_px - TP.sx / 2, container_hs * 1.2), (s_px + TP.sx / 2, container_hs * 1.2)])
            gc.DrawLines([(s_px - TP.sx / 2, TP.sy + container_hs * 1.2), (s_px + TP.sx / 2, TP.sy + container_hs * 1.2)])
            gc.DrawLines([(s_px - TP.sx / 2, container_hs * 1.2), (s_px - TP.sx / 2, TP.sy + container_hs * 1.2)])
            gc.DrawLines([(s_px + TP.sx / 2, container_hs * 1.2), (s_px + TP.sx / 2, TP.sy + container_hs * 1.2)])
#            gc.DrawRectangle(s_px - TP.sx / 2, 0, TP.sx, TP.sy)
        for c in self.holding_containers.values():
            old_tr = gc.GetTransform()
            gc.Translate(c.px, c.py)
            c.draw(gc)
            gc.SetTransform(old_tr)
        if id_show:
            gc.SetFont(wx.Font(5, wx.SWISS, wx.NORMAL, wx.NORMAL))
            gc.DrawText(str(self.name + '-' + str(self.id)), -container_hs * 0.6, -container_vs * 1.6)
class Block(Storage):
    num_of_bays = 97
    num_of_stacks = 8
    bay_pos_info = {}
    stack_pos_info = {}
    for x in xrange(num_of_bays):
        bay_id = x + 1
        if bay_id % 4 == 0: py = container_hs * ((bay_id // 4 - 1) + 1 / 2) + container_hs / 2
        elif bay_id % 4 == 1: py = container_hs * (bay_id // 4) + container_hs / 4
        elif bay_id % 4 == 2: py = container_hs * (bay_id // 4) + container_hs / 2
        elif bay_id % 4 == 3: py = container_hs * ((bay_id // 4) + 1 / 2) + container_hs / 4
        else: assert False
        bay_pos_info[bay_id] = py
    for x in xrange(num_of_stacks):
        stack_pos_info[x + 1] = container_vs * x + container_vs / 2
        
    def __init__(self, id, px, py):
        Storage.__init__(self)
        self.name, self.id = 'Block', id
        self.px, self.py = px, py
        mg = 2
        self.bg_ps = [(-mg, -mg),
                      (container_vs * Block.num_of_stacks + mg, -mg),
                      (container_vs * Block.num_of_stacks + mg, Block.bay_pos_info[97]*1.96 + container_hs / 2 + mg),
                      (-mg, Block.bay_pos_info[97]*1.96 + container_hs / 2 + mg),
                      ]
    def draw(self, gc, id_show):
        gc.SetPen(wx.Pen(wx.Colour(210, 209, 208), 0))
        gc.SetBrush(wx.Brush(wx.Colour(210, 209, 208)))
        gc.DrawLines(self.bg_ps)
        
        gc.SetPen(wx.Pen(wx.Colour(100, 100, 100), 0.5))
        for x in xrange((Block.num_of_bays - 1) // 2 + 1):
            gc.DrawLines([(0, container_hs * x), (container_vs * Block.num_of_stacks , container_hs * x)])
            if id_show:
                if x * 4 < 8:
                    px = container_vs * Block.num_of_stacks + container_vs * 1.5
                else:
                    px = container_vs * Block.num_of_stacks + container_vs * 1.1
                gc.DrawText(str(x * 4 + 2), px , container_hs * x + container_hs * 0.4)
        for x in xrange(Block.num_of_stacks + 1):
            gc.DrawLines([(container_vs * x, 0), (container_vs * x , container_hs * (Block.num_of_bays - 1) // 2)])
        for c in self.holding_containers.values():
            old_tr = gc.GetTransform()
            gc.Translate(c.px, c.py)
            c.draw(gc)
            gc.SetTransform(old_tr)
        if id_show:
            gc.SetFont(wx.Font(5, wx.SWISS, wx.NORMAL, wx.NORMAL))
            gc.DrawText(str(self.name + '-' + str(self.id)), -container_hs * 0.4 , -container_vs * 1.5)
