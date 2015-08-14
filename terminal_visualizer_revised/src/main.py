from __future__ import division
import wx, initializer
import  wx.lib.anchors as anchors
from datetime import datetime, timedelta
from time import time
from parameter_function import frame_milsec, play_speed, play_x , container_hs, container_vs, total_num_bitt, total_num_qb, total_num_b, l_sx, find_target_evt, find_init_pos, update
from others_classes import Vessel, Drag_zoom_panel, Bitt
from storage_classes import QB, TP, Block
from vehicle_classes import  QC, YC, SC
Bitts = {}
QBs = {}
Blocks = {}
TPs = {}

SH = '02'
SMI = '14'
SS = '00'
#SH = '03'
#SMI = '06'
#SS = '55'

class Performance_dialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'Performance', pos=(1050, 150) , size=(200, 170))
        self.SetBackgroundColour(wx.Colour(236, 233, 216))
        bt = 8
        qc = wx.StaticText(self, -1, 'QC', (22, 16))
        px, py = qc.GetPosition()
        sx, sy = qc.GetSize()
        qc.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        gauge = wx.CheckBox(self, -1, "Gauge", (px + bt * 3, py + sy + bt), style=wx.NO_BORDER)
        gauge.SetValue(True)
        px, py = gauge.GetPosition()
        sx, sy = gauge.GetSize()
        a = wx.StaticText(self, -1, 'Allocation of Container', (px - bt * 3, py + sy + bt))
        a.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        px, py = a.GetPosition()
        sx, sy = a.GetSize()
        al = wx.CheckBox(self, -1, "Loading", (px + bt * 3, py + sy + bt), style=wx.NO_BORDER)
        px, py = al.GetPosition()
        sx, sy = al.GetSize()
        ad = wx.CheckBox(self, -1, "Discharging", (px, py + sy + bt), style=wx.NO_BORDER)
        
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, gauge)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, al)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, ad)
    
    def EvtCheckBox(self, event):
        ce = event.GetEventObject()
        st = ce.GetLabelText()
        print st
        if st == 'Gauge' :
            if ce.GetValue():
                self.Parent.is_gauge_show = True
            else:
                self.Parent.is_gauge_show = False
        elif st == 'Loading':
            if ce.GetValue():
                self.Parent.is_al_loading_show = True
            else:
                self.Parent.is_al_loading_show = False
        elif st == 'Discharging':
            if ce.GetValue():
                self.Parent.is_al_discharging_show = True
            else:
                self.Parent.is_al_discharging_show = False    
        
class Input_dialog(wx.Dialog):
    def __init__(self, parent, name, size=(800, 600), pos=(450, 170)):
        wx.Dialog.__init__(self, None, -1, 'Monitoring', pos , size)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        bg_img = wx.Image('pic/monitoring_bg.png', wx.BITMAP_TYPE_PNG)
        sx, sy = self.GetSize()
        bg = wx.StaticBitmap(self, -1, wx.BitmapFromImage(bg_img), style=wx.NO_BORDER)
        bg_end_px, bg_end_py = bg.GetSize()
        wx.StaticBox(self, -1, "", pos=(2, bg_end_py - 4), size=(bg_end_px - 10, 90))

        txt_font = wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.SetFont(txt_font)
        c_begin_py = bg_end_py + 20
        margin = 15
        vn_txt = wx.StaticText(self, -1, 'Vessel', (23, c_begin_py))
        vn_txt_px, vn_txt_py = vn_txt.GetPosition()
        vn_txt_sx, vn_txt_sy = vn_txt.GetSize()
        vy_txt = wx.StaticText(self, -1, 'Voyage', (20, c_begin_py + vn_txt_sy + margin))
        v_name, vo_name = ['HNVN', 'MCEN', 'WLTA', 'HUXA'], ['01', '02', '03', '04', '05', '06', '07']
        vy_txt_px, vy_txt_py = vy_txt.GetPosition()
        vy_txt_sx, vy_txt_sy = vy_txt.GetSize()
        
        self.v_name_ch = wx.Choice(self, -1, (vy_txt_px + vy_txt_sx + margin, vn_txt_py - 3), choices=v_name)
        vn_ch_sx, vn_ch_sy = self.v_name_ch.GetSize()
        vn_ch_px, vn_ch_py = self.v_name_ch.GetPosition()
        self.vo_name_ch = wx.Choice(self, -1, (vy_txt_px + vy_txt_sx + margin, vy_txt_py - 3), self.v_name_ch.GetSize(), choices=vo_name)
        self.v_name_ch.SetSelection(0), self.vo_name_ch.SetSelection(1)
        sd_txt = wx.StaticText(self, -1, 'Start', (vn_ch_sx + vn_ch_px + margin * 2, vn_ch_py))
        d_txt_px, d_txt_py = sd_txt.GetPosition()
        d_txt_sx, d_txt_sy = sd_txt.GetSize()
        ed_txt = wx.StaticText(self, -1, 'End', (d_txt_px + d_txt_sx + margin * 3, d_txt_py + d_txt_sy + margin * 1.5)) 
        year, month, day = [str(x) for x in xrange(2005, 2013)], [str(x) for x in xrange(1, 13)], [str(x) for x in xrange(1, 32)]
        
        txt_font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.SetFont(txt_font)
        self.sy_ch = wx.Choice(self, -1, (d_txt_px + d_txt_sx + margin, d_txt_py - 3), choices=year)
        px, py = self.sy_ch.GetPosition()
        sx, sy = self.sy_ch.GetSize()
        wx.StaticText(self, -1, "-", (px + sx + 5, py + 3), size=(25, -1))
        self.sm_ch = wx.Choice(self, -1, (px + sx + margin, py), choices=month)
        px, py = self.sm_ch.GetPosition()
        sx, sy = self.sm_ch.GetSize()
        wx.StaticText(self, -1, "-", (px + sx + 5, py + 3), size=(25, -1))
        self.sd_ch = wx.Choice(self, -1, (px + sx + margin, py), choices=day)
        px, py = self.sd_ch.GetPosition()
        sx, sy = self.sd_ch.GetSize()
        self.sh_txt = wx.TextCtrl(self, -1, SH, (px + sx + margin, py), size=(25, -1))
#        self.sh_txt = wx.TextCtrl(self, -1, "08", (px + sx + margin, py), size=(25, -1))
        px, py = self.sh_txt.GetPosition()
        sx, sy = self.sh_txt.GetSize()
        wx.StaticText(self, -1, ":", (px + sx + 5, py + 3), size=(10, -1))
        self.smi_txt = wx.TextCtrl(self, -1, SMI, (px + sx + margin, py), size=(25, -1))
#        self.smi_txt = wx.TextCtrl(self, -1, "19", (px + sx + margin, py), size=(25, -1))
        px, py = self.smi_txt.GetPosition()
        sx, sy = self.smi_txt.GetSize()
        wx.StaticText(self, -1, ":", (px + sx + 5, py + 3), size=(10, -1))
        self.ss_txt = wx.TextCtrl(self, -1, SS, (px + sx + margin, py), size=(25, -1))
#        self.ss_txt = wx.TextCtrl(self, -1, "18", (px + sx + margin, py), size=(25, -1))        
        self.sy_ch.SetSelection(7), self.sm_ch.SetSelection(2), self.sd_ch.SetSelection(18)
        
        sx, sy = ed_txt.GetSize()
        px, py = ed_txt.GetPosition()
        self.ey_ch = wx.Choice(self, -1, (px + sx + margin, py - 3), choices=year)
        px, py = self.ey_ch.GetPosition()
        sx, sy = self.ey_ch.GetSize()
        wx.StaticText(self, -1, "-", (px + sx + 5, py + 3), size=(25, -1))
        self.em_ch = wx.Choice(self, -1, (px + sx + margin, py), choices=month)
        px, py = self.em_ch.GetPosition()
        sx, sy = self.em_ch.GetSize()
        wx.StaticText(self, -1, "-", (px + sx + 5, py + 3), size=(25, -1))
        self.ed_ch = wx.Choice(self, -1, (px + sx + margin, py), choices=day)
        px, py = self.ed_ch.GetPosition()
        sx, sy = self.ed_ch.GetSize()
        self.eh_txt = wx.TextCtrl(self, -1, "14", (px + sx + margin, py), size=(25, -1))
        px, py = self.eh_txt.GetPosition()
        sx, sy = self.eh_txt.GetSize()
        wx.StaticText(self, -1, ":", (px + sx + 5, py + 3), size=(10, -1))
        self.emi_txt = wx.TextCtrl(self, -1, "30", (px + sx + margin, py), size=(25, -1))
        px, py = self.emi_txt.GetPosition()
        sx, sy = self.emi_txt.GetSize()
        wx.StaticText(self, -1, ":", (px + sx + 5, py + 3), size=(10, -1))
        self.es_txt = wx.TextCtrl(self, -1, "00", (px + sx + margin, py), size=(25, -1)) 
        px, py = self.es_txt.GetPosition()
        sx, sy = self.es_txt.GetSize()
        self.ey_ch.SetSelection(7), self.em_ch.SetSelection(2), self.ed_ch.SetSelection(18) 

        setting_btn = wx.Button(self, -1, "  Start  ", (px + sx + margin * 1.8, py - 1))
        
        self.Bind(wx.EVT_BUTTON, self.setting, setting_btn)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Show(True)
        
    def OnClose(self, event):
        self.Destroy()
        
    def setting(self, event):
        self.vn, self.vo = self.v_name_ch.GetString(self.v_name_ch.GetSelection()), self.vo_name_ch.GetString(self.vo_name_ch.GetSelection())

        self.sy, self.sm, self.sd = self.sy_ch.GetString(self.sy_ch.GetSelection()), self.sm_ch.GetString(self.sm_ch.GetSelection()), self.sd_ch.GetString(self.sd_ch.GetSelection())
        self.sh, self.smi, self.ss = self.sh_txt.GetValue(), self.smi_txt.GetValue(), self.ss_txt.GetValue()
        
        self.ey, self.em, self.ed = self.ey_ch.GetString(self.ey_ch.GetSelection()), self.em_ch.GetString(self.em_ch.GetSelection()), self.ed_ch.GetString(self.ed_ch.GetSelection())
        self.eh, self.emi, self.es = self.eh_txt.GetValue(), self.emi_txt.GetValue(), self.es_txt.GetValue()
        
        win = MainFrame(self)
        dl = Performance_dialog(win)
        dl.Show(True)
        win.Show(True)
        self.Show(False)
        
class MainFrame(wx.Frame):
    def __init__(self, input_info):
        wx.Frame.__init__(self, None, -1, 'Monitoring', size=(1024, 768), pos=(243, 80))
        self.input_info = input_info
        self.is_gauge_show = True
        self.is_al_loading_show = False
        self.is_al_discharging_show = False
        f_sx, f_sy = self.GetSize()
        self.SetBackgroundColour(wx.Colour(236, 233, 216))
        self.SetAutoLayout(True)
        
        sy, sm, sd, sh, smi, ss = int(input_info.sy), int(input_info.sm), int(input_info.sd), int(input_info.sh), int(input_info.smi), int(input_info.ss) 
        ey, em, ed, eh, emi, es = int(input_info.ey), int(input_info.em), int(input_info.ed), int(input_info.eh), int(input_info.emi), int(input_info.es)
        
        self.start_time, self.end_time = datetime(sy, sm, sd, sh, smi, ss), datetime(ey, em, ed, eh, emi, es)
        print 'start time : ', self.start_time 
        
        self.simul_clock = datetime(sy, sm, sd, sh, smi, ss)
        self.saved_time = time()
        self.simul_clock_saved = None

        self.timer = wx.Timer(self)
        self.timer.Start(frame_milsec)
        
        self.play_speed, self.isReverse_play = play_speed, False
        
        vessels, qcs, ycs, scs, containers = initializer.run()
        
        ip_py, ip_sy = 0 , 30
        vp_py, vp_sy = ip_py + ip_sy , 630
        cp_py, cp_sy = vp_py + vp_sy , f_sy - (vp_sy + ip_sy)
        
        Input_View_Panel(self , (0, ip_py), (f_sx, ip_sy), input_info.vn, input_info.vo, self.start_time, self.end_time)
        self.vp = Viewer_Panel(self, (7, vp_py), (f_sx - 21, vp_sy), vessels, qcs, ycs, scs, containers)
        self.cp = Control_Panel(self, (0, cp_py), (f_sx, cp_sy))        
        self.Show(True)
        
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
    def OnTimer(self, evt):
        if self.simul_clock_saved == None:
            cur_time = time()
            time_interval = cur_time - self.saved_time
            if not self.isReverse_play:
                self.simul_clock += timedelta(seconds=time_interval * self.play_speed)
            else:
                self.simul_clock -= timedelta(seconds=time_interval * self.play_speed)
            self.saved_time = cur_time
        else:
            self.simul_clock = self.simul_clock_saved
            self.simul_clock_saved = None
            self.saved_time = time()
        self.vp.update_picture(self.simul_clock)
        self.cp.Update_control_time(self.simul_clock)
        
    def OnClose(self, event):
        self.input_info.Destroy()
        self.Destroy()        

class Input_View_Panel(wx.Panel):
    def __init__(self, parent, pos, size, v_name, v_voyage, start_time, end_time):
        wx.Panel.__init__(self, parent, -1, pos, size)
        self.SetConstraints(anchors.LayoutAnchors(self, True, True, True, False))
        margin = 30
        v_t = wx.StaticText(self, -1, 'Vessel', (60, 6))
        px, py = v_t.GetPosition()
        sx, sy = v_t.GetSize()
        v_n = wx.StaticText(self, -1, v_name, (px + sx + margin * 0.9, py))
        px, py = v_n.GetPosition()
        sx, sy = v_n.GetSize()
        v_v = wx.StaticText(self, -1, 'Voyage', (px + sx + margin * 1.2, py))
        px, py = v_v.GetPosition()
        sx, sy = v_v.GetSize()
        v_vo = wx.StaticText(self, -1, v_voyage, (px + sx + margin * 0.9, py))
        px, py = v_vo.GetPosition()
        sx, sy = v_vo.GetSize()
        d = wx.StaticText(self, -1, 'Date', (px + sx + margin * 4, py))
        
        for x in [v_t, v_v, d]:
            x.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        for x in [v_n, v_vo]:
            x.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        #Date/Time
        y_name1_px = 450
        bt = 10
        ch_margin = 2
        sdt_edt_txt = []
        t = wx.StaticText(self, -1, str(start_time.year), (y_name1_px, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, '-', (px + sx + bt + ch_margin, py - ch_margin))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(start_time.month), (px + sx + bt + ch_margin * 2, py + ch_margin))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, '-', (px + sx + bt + ch_margin, py - ch_margin))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(start_time.day), (px + sx + bt + ch_margin, py + 2))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(start_time.hour), (px + sx + bt * 2, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, ':', (px + sx, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(start_time.minute), (px + sx + bt, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, ':', (px + sx + bt, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(start_time.second), (px + sx + bt * 2, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        
        t = wx.StaticText(self, -1, '~', (px + sx + 18, py - 2))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        
        y_name2_px = 700
        t = wx.StaticText(self, -1, str(end_time.year), (px + sx + 27, py + 2))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, '-', (px + sx + bt + ch_margin, py - ch_margin))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(end_time.month), (px + sx + bt * 2, py + ch_margin))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, '-', (px + sx + bt + ch_margin, py - ch_margin))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(end_time.day), (px + sx + bt + ch_margin, py + 2))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(end_time.hour), (px + sx + bt * 2, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, ':', (px + sx + 4, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(end_time.minute), (px + sx + bt, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, ':', (px + sx + bt * 2, py))
        sdt_edt_txt.append(t)
        px, py = t.GetPosition()
        sx, sy = t.GetSize()
        t = wx.StaticText(self, -1, str(end_time.second), (px + sx + bt * 2, py))
        sdt_edt_txt.append(t)
        
        for x in sdt_edt_txt:
            x.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        
        for x in sdt_edt_txt + [v_t, v_v, d] + [v_n, v_vo]:
            x.SetConstraints(anchors.LayoutAnchors(x, False, True, False, False))

class Control_Panel(wx.Panel):
    def __init__(self, parent, pos, size):
        wx.Panel.__init__(self, parent, -1, pos, size)
        self.SetConstraints(anchors.LayoutAnchors(self, True, False, True, True))
        
        self.timer, self.simul_clock, self.saved_time, self.play_speed = parent.timer, parent.simul_clock, time(), parent.play_speed
        self.start_time, end_time = parent.start_time, parent.end_time
        total_time_interval = end_time - self.start_time 
        total_sec = total_time_interval.total_seconds()

        self.time_flow = wx.Slider(self, -1, 0, 0, total_sec, (10, 10), (995, -1), wx.SL_HORIZONTAL)
        self.time_flow.SetConstraints(anchors.LayoutAnchors(self.time_flow, True, False, True, False))
        
        self.simul_st, self.paly_speed = wx.StaticText(self, -1, self.simul_clock.ctime(), (410, 40)), wx.StaticText(self, -1, str(self.play_speed) + 'x', (825, 40))
        for x in [self.simul_st, self.paly_speed]:
            x.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
#            x.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.simul_st.SetConstraints(anchors.LayoutAnchors(self.simul_st, True, False, True, False))
        self.paly_speed.SetConstraints(anchors.LayoutAnchors(self.paly_speed, True, False, True, False))
        s_img, r_img, pa_img, pl_img = wx.Image('pic/stop.bmp', wx.BITMAP_TYPE_BMP), wx.Image("pic/reverse.bmp", wx.BITMAP_TYPE_BMP), wx.Image("pic/pause.bmp", wx.BITMAP_TYPE_BMP), wx.Image("pic/play.bmp", wx.BITMAP_TYPE_BMP) 
        s_bmp, r_bmp, pa_bmp, pl_bmp = s_img.Scale(30, 30), r_img.Scale(30, 30), pa_img.Scale(30, 30), pl_img.Scale(30, 30)
        py = 875
        bt = 30
        s_btn, r_btn , pa_btn, pl_btn = wx.BitmapButton(self, -1, wx.BitmapFromImage(s_bmp), (py, 35), (s_bmp.GetWidth() + 2, s_bmp.GetHeight() + 2)), wx.BitmapButton(self, -1, wx.BitmapFromImage(r_bmp), (py + bt, 35), (r_bmp.GetWidth() + 2, r_bmp.GetHeight() + 2)), wx.BitmapButton(self, -1, wx.BitmapFromImage(pa_bmp), (py + bt * 2, 35), (pa_bmp.GetWidth() + 2, pa_bmp.GetHeight() + 2)), wx.BitmapButton(self, -1, wx.BitmapFromImage(pl_bmp), (py + bt * 3, 35), (pl_bmp.GetWidth() + 2, pl_bmp.GetHeight() + 2))        
        for x in [s_btn, r_btn, pa_btn, pl_btn]:
            x.SetConstraints(anchors.LayoutAnchors(x, False, False, True, True))
        self.Bind(wx.EVT_BUTTON, self.time_flow_stop, s_btn)
        self.Bind(wx.EVT_BUTTON, self.time_flow_reverse, r_btn)
        self.Bind(wx.EVT_BUTTON, self.time_flow_pause, pa_btn)
        self.Bind(wx.EVT_BUTTON, self.time_flow_play, pl_btn)
        self.time_flow.Bind(wx.EVT_SCROLL_CHANGED, self.onChanged)
    def onChanged(self, evt):
        self.timer.Stop()
        print evt.EventObject.GetMin(), evt.EventObject.GetMax() 
        print evt.EventObject.GetRange()
        print 'changed: %d' % evt.EventObject.GetValue()  
    def time_flow_stop(self, evt):
        self.time_flow.SetValue(0)
        self.Parent.simul_clock = self.start_time
        self.simul_st.SetLabel(self.Parent.simul_clock.ctime())
        self.timer.Stop() 
        
    def time_flow_reverse(self, evt):
        if not self.timer.IsRunning():
            self.timer.Start(frame_milsec)
        if self.Parent.play_speed > 0:
            play_x = None
            if self.Parent.play_speed < 10:
                play_x = 1
            elif self.Parent.play_speed >= 10:
                play_x = 10
            self.Parent.play_speed -= play_x
            self.paly_speed.SetLabel(str(self.Parent.play_speed) + 'x')
        else:
            self.Parent.isReverse_play = True
        
    def time_flow_pause(self, evt):
        self.Parent.simul_clock_saved = self.Parent.simul_clock
        #################
#        self.Parent.play_speed = 0.5
#        self.paly_speed.SetLabel(str(self.Parent.play_speed) + 'x')
        #################
        self.timer.Stop()
    
    def time_flow_play(self, evt):
        self.Parent.isReverse_play = False
        if self.timer.IsRunning():
            play_x = None
            if self.Parent.play_speed < 10:
                play_x = 1
            elif self.Parent.play_speed >= 10:
                play_x = 10    
            self.Parent.play_speed += play_x
            self.paly_speed.SetLabel(str(self.Parent.play_speed) + 'x')
        else: 
            self.timer.Start(frame_milsec)

    def Update_control_time(self, simul_clock):
        cur_sec = time()
        if abs(self.saved_time - cur_sec) >= 1 :
            self.simul_st.SetLabel(simul_clock.ctime())
            self.saved_time = cur_sec
        flow_time = (simul_clock - self.start_time).total_seconds()
        self.time_flow.SetValue(flow_time)

class Viewer_Panel(Drag_zoom_panel):
    def __init__(self, parent, pos, size, vessels, qcs, ycs, scs, containers):
        Drag_zoom_panel.__init__(self, parent, pos, size)
        self.id_show = False
        self.SetConstraints(anchors.LayoutAnchors(self, True, True, True, True))
        self.vessels, self.qcs, self.ycs, self.scs, self.containers = vessels, qcs, ycs, scs, containers
        simul_clock = parent.simul_clock
        self.sx, self.sy = self.GetSize()
        l3_py = self.set_deco_pos()
        self.make_storage(l3_py)
        self.set_vehicle_pos(self.vessels, self.qcs, self.ycs, self.scs, self.containers, simul_clock)
        self.set_container_pos(self.vessels, self.qcs, self.scs, self.ycs, self.containers, simul_clock)
        
        mg = 20
        l_mg = 2
        
        p0, p1, p2 = (l_sx + mg * 2, 1400), (l_sx + mg * 2, self.lines_py[0] - l_mg + mg), (l_sx + mg, self.lines_py[0] - l_mg)
        p3, p4, p5 = (0, self.lines_py[0] - l_mg), (-mg, self.lines_py[0] + mg - l_mg), (-mg, 1400) 
        self.l_bg_ps = [p0, p1, p2, p3, p4, p5]
        
        dp0, dp1, dp2 = (-mg + l_mg, 1400), (-mg + l_mg, self.lines_py[0] + mg - l_mg), (0, self.lines_py[0]) 
        self.deco_l1 = [dp0, dp1, dp2]
        
        dp0, dp1 = (l_sx, self.lines_py[0]), (l_sx + mg - l_mg, self.lines_py[0])
        dp2, dp3 = (l_sx + mg * 2 - l_mg, self.lines_py[0] - l_mg + mg), (l_sx + mg * 2, 1400)
        self.deco_l2 = [dp0, dp1, dp2, dp3]
        
        self.InitBuffer()

    def set_vehicle_pos(self, vessels, qcs, ycs, scs, containers, simul_clock):
        for v in vessels + qcs + ycs + scs:
            v.target_evt_id, v.evt_end = find_target_evt(v.target_evt_id, v.evt_seq, simul_clock)
            if isinstance(v, Vessel):
                Vessel.Bitts = Bitts
                v.set_evt_data(v.target_evt_id, simul_clock)
            elif isinstance(v, QC):
                c_dic = {}
                for c in containers:
                    c_dic[c.c_id] = c
                QC.Vessels, QC.QBs, QC.TPs, QC.Containers = vessels, QBs, TPs, c_dic
                last_QB_id = 0
                for qb_id in QBs.keys():
                    if qb_id > last_QB_id : last_QB_id = qb_id
                v.py = QBs[last_QB_id].py + QBs[last_QB_id].sy
                v.set_evt_data(v.target_evt_id, simul_clock)
            elif isinstance(v, YC):
                YC.TPs, YC.Blocks = TPs, Blocks
                start_evt = v.evt_seq[v.target_evt_id] 
                b_or_tp_id = None 
                if start_evt.pos[:2] == 'LM':
                    b_or_tp_id = start_evt.pos[3:5]
                else:
                    b_or_tp_id = start_evt.pos[:2]
                v.px = YC.Blocks[b_or_tp_id].px + YC.sy / 2
                v.set_evt_data(v.target_evt_id, simul_clock)
            elif isinstance(v, SC):
                SC.Vessels, SC.QBs, SC.TPs, SC.QCs = vessels, QBs, TPs, qcs
                start_evt = v.evt_seq[v.target_evt_id]
                v.set_evt_data(v.target_evt_id, simul_clock)
            else:
                assert False, 'not suitable vehicle'
                
    def set_container_pos(self, vessels, qcs, scs, ycs, containers, simul_clock):
        ### set container position
        for c in containers:
            c.target_evt_id, c.evt_end = find_init_pos(c.target_evt_id, c.evt_seq, simul_clock)
            if c.target_evt_id == -1:
                tg_evt = c.evt_seq[c.target_evt_id + 1]
            else:
                tg_evt = c.evt_seq[c.target_evt_id]
            vehicle = tg_evt.vehicle
            work_type = tg_evt.work_type
            operation = tg_evt.operation
            pos = tg_evt.pos
#            print c.target_evt_id, vehicle, '    ', tg_evt
            if vehicle[:3] == 'STS' and work_type == 'TwistLock' and operation == 'DISCHARGING':
                if c.target_evt_id == -1: 
                    # container from Vessel
                    vessel_info = tg_evt.v_info
                    target_v_name, target_v_voyage_txt, _ = vessel_info.split('/')
                    target_v = None
                    for v in vessels:
                        if v.name == target_v_name and v.voyage == int(target_v_voyage_txt):
                            target_v = v
                            break
                    else:
                        assert False , 'there is no target_v'
                    c.hs, c.vs = container_hs, container_vs
                    cur_pos = tg_evt.pos
                    bay_id, stack_id = int(cur_pos[2:4]), int(cur_pos[5:7]) 
                    if bay_id % 2 == 0 :
                        c.hs, c.vs = container_hs, container_vs
                    else:
                        c.hs, c.vs = container_hs / 2, container_vs
                    c.px, c.py = target_v.bay_pos_info[bay_id] , target_v.stack_pos_info[stack_id]
                    target_v.holding_containers[tg_evt.c_id] = c
                else:
                    target_qc = None
                    qc_id = int(vehicle[3:])
                    for qc in qcs:
                        if qc.veh_id == qc_id:
                            target_qc = qc
                            break
                    else:
                        assert False , 'there is no target_qc'
                    c.hs, c.vs = container_hs, container_vs
                    c.px, c.py = 0, 0
                    target_qc.holding_containers[tg_evt.c_id] = c
                    
            elif vehicle[:3] == 'STS' and work_type == 'TwistUnlock' and operation == 'DISCHARGING':
                target_qc, target_qb = None , None
                qc_id , qb_id = int(pos[3:6]) , int(pos[-1:])
                for qc in qcs:
                    if qc.veh_id == qc_id:
                        target_qc = qc
                        break
                target_qb = QBs[qb_id]
                c.hs, c.vs = container_hs, container_vs
                c.px, c.py = target_qc.px, target_qb.v_c_pos_info
                target_qb.holding_containers[tg_evt.c_id] = c
                
            elif vehicle[:2] == 'SH' and work_type == 'TwistLock' and operation == 'DISCHARGING':
                if c.target_evt_id == -1:
                    target_qc, target_qb = None , None
                    qc_id , qb_id = int(pos[3:6]) , int(pos[-1:])
                    for qc in qcs:
                        if qc.veh_id == qc_id:
                            target_qc = qc
                            break
                    target_qb = QBs[qb_id]
                    c.hs, c.vs = container_hs, container_vs
                    c.px, c.py = target_qc.px, target_qb.v_c_pos_info
                    target_qb.holding_containers[tg_evt.c_id] = c
                else:
                    target_sc = None
                    sc_id = int(vehicle[-2:])
                    for sc in scs:
                        if sc.veh_id == sc_id:
                            target_sc = sc
                            break
                    else:
                        assert False , 'there is no target_sc'
                    c.hs, c.vs = container_hs, container_vs
                    c.px, c.py = 0, 0
                    target_sc.holding_containers[tg_evt.c_id] = c
                    
            elif vehicle[:2] == 'SH' and work_type == 'TwistUnlock' and operation == 'DISCHARGING':
                pos = tg_evt.pos
                tp_id, stack_id = pos[3:5], int(pos[8:])
                target_tp = SC.TPs[tp_id]
                c.hs, c.vs = container_vs, container_hs
                c.px, c.py = target_tp.stack_pos_info[stack_id], target_tp.bay_pos_info
                target_tp.holding_containers[tg_evt.c_id] = c
            
            elif vehicle[:3] == 'ASC' and work_type == 'TwistLock' and operation == 'DISCHARGING':
                if c.target_evt_id == -1: 
                    pos = tg_evt.pos
                    tp_id, stack_id = pos[3:5], int(pos[8:])
                    target_tp = SC.TPs[tp_id]
                    c.hs, c.vs = container_vs, container_hs
                    c.px, c.py = target_tp.stack_pos_info[stack_id], target_tp.bay_pos_info
                    target_tp.holding_containers[tg_evt.c_id] = c
                else:
                    target_yc = None
                    yc_id = int(vehicle[-3:])
                    for yc in ycs:
                        if yc.veh_id == yc_id:
                            target_yc = yc
                            break
                    else:
                        assert False , 'there is no target_qc'
                    c.hs, c.vs = container_vs, container_hs
                    c.px, c.py = 0, 0
                    target_yc.holding_containers[tg_evt.c_id] = c
            
            elif vehicle[:3] == 'ASC' and work_type == 'TwistUnlock' and operation == 'DISCHARGING':
                block_id, bay_id, stack_id = pos[:2], int(pos[3:5]), int(pos[6:7]) 
                assert bay_id <= Block.num_of_bays, 'exceed num of bay'
                assert stack_id <= Block.num_of_stacks, 'exceed num of stack'
                target_block = Blocks[block_id]
                c.px, c.py = target_block.stack_pos_info[stack_id], target_block.bay_pos_info[bay_id]
                if bay_id % 2 == 0:
                    c.hs, c.vs = container_vs, container_hs
                else:
                    c.hs, c.vs = container_vs, container_hs / 2
                target_block.holding_containers[tg_evt.c_id] = c
            
            elif vehicle[:3] == 'STS' and work_type == 'TwistLock' and operation == 'LOADING':
                target_qc = None
                qc_id = int(vehicle[3:])
                for qc in qcs:
                    if qc.veh_id == qc_id:
                        target_qc = qc
                        break
                else:
                    assert False , 'there is no target_qc'
                pe_pos = c.evt_seq[c.target_evt_id + 1].pos
                bay_id = int(pe_pos[2:4])
                if bay_id % 2 == 0:
                    c.hs, c.vs = container_hs, container_vs
                else:
                    c.hs, c.vs = container_hs / 2, container_vs
                c.px, c.py = 0, 0
                target_qc.holding_containers[tg_evt.c_id] = c
                
            elif vehicle[:3] == 'STS' and work_type == 'TwistUnlock' and operation == 'LOADING':
                bay_id, stack_id = int(pos[2:4]), int(pos[5:7]) 
                target_v = None
                v_name, v_voyage_txt, _ = tg_evt.v_info.split('/')
                for v in vessels:
                    if v.name == v_name and v.voyage == int(v_voyage_txt):
                        target_v = v
                        break
                else:
                    assert False, 'There is not target Vessel'
                    
                if bay_id % 2 == 0 :
                    c.hs, c.vs = container_hs, container_vs
                else:
                    c.hs, c.vs = container_hs / 2, container_vs
                c.px, c.py = target_v.bay_pos_info[bay_id] , target_v.stack_pos_info[stack_id]
                target_v.holding_containers[tg_evt.c_id] = c
            
            elif vehicle[:2] == 'SH' and work_type == 'TwistLock' and operation == 'LOADING':
                target_sc = None
                sc_id = int(vehicle[-2:])
                for sc in scs:
                    if sc.veh_id == sc_id:
                        target_sc = sc
                        break
                else:
                    assert False , 'there is no target_sc'
                pe_pe_pos = c.evt_seq[c.target_evt_id - 2].pos 
                bay_id = int(pe_pe_pos[3:5])
                if bay_id % 2 == 0:
                    c.hs, c.vs = container_hs, container_vs 
                else:
                    c.hs, c.vs = container_hs / 2, container_vs 
                c.px, c.py = 0, 0
                target_sc.holding_containers[tg_evt.c_id] = c
            
            elif vehicle[:2] == 'SH' and work_type == 'TwistUnlock' and operation == 'LOADING':
                target_qc, target_qb = None , None
                qc_id , qb_id = int(pos[3:6]) , int(pos[-2:])
                for qc in qcs:
                    if qc.veh_id == qc_id:
                        target_qc = qc
                        break
                target_qb = QBs[qb_id]
                ne_ne_evt = c.evt_seq[c.target_evt_id + 2]
                ne_pos = ne_ne_evt.pos
                bay_id, stack_id = int(ne_pos[2:4]), int(ne_pos[5:7])
                target_v = None
                v_name, v_voyage_txt, _ = tg_evt.v_info.split('/')
                for v in vessels:
                    if v.name == v_name and v.voyage == int(v_voyage_txt):
                        target_v = v
                        break
                else:
                    assert False, 'There is not target Vessel'
                    
                if bay_id % 2 == 0 :
                    c.hs, c.vs = container_hs, container_vs
                else:
                    c.hs, c.vs = container_hs / 2, container_vs
                c.px, c.py = target_v.px + target_v.bay_pos_info[bay_id], target_qb.v_c_pos_info
                target_qb.holding_containers[tg_evt.c_id] = c
                    
            elif vehicle[:3] == 'ASC' and work_type == 'TwistLock' and operation == 'LOADING':
                if c.target_evt_id == -1:
                    # container from Block
                    pos = tg_evt.pos
                    block_id, bay_id, stack_id = pos[:2], int(pos[3:5]), int(pos[6:7])
                    assert bay_id <= Block.num_of_bays, 'exceed num of bay'
                    assert stack_id <= Block.num_of_stacks, 'exceed num of stack'
                    target_block = Blocks[block_id]
                    c.px, c.py = target_block.stack_pos_info[stack_id], target_block.bay_pos_info[bay_id]
                    if bay_id % 2 == 0:
                        c.hs, c.vs = container_vs, container_hs
                    else:
                        c.hs, c.vs = container_vs, container_hs / 2
                    target_block.holding_containers[tg_evt.c_id] = c
                else:
                    target_yc = None
                    yc_id = int(vehicle[3:])
                    for yc in ycs:
                        if yc.veh_id == yc_id:
                            target_yc = yc
                            break
                    else:
                        assert False , 'there is no target_qc'
                    pos = tg_evt.pos
                    bay_id = int(pos[3:5])
                    if bay_id % 2 == 0:
                        c.hs, c.vs = container_vs, container_hs
                    else:
                        c.hs, c.vs = container_vs, container_hs / 2
                    c.px, c.py = 0, 0
                    target_yc.holding_containers[tg_evt.c_id] = c
                
            elif vehicle[:3] == 'ASC' and work_type == 'TwistUnlock' and operation == 'LOADING':
                pos = tg_evt.pos
                tp_id, stack_id = pos[3:5], int(pos[8:])
                target_tp = SC.TPs[tp_id]
                pe_pos = c.evt_seq[c.target_evt_id - 1].pos 
                bay_id = int(pe_pos[3:5])
                if bay_id % 2 == 0:
                    c.hs, c.vs = container_vs, container_hs
                else:
                    c.hs, c.vs = container_vs, container_hs / 2
                
                c.px, c.py = target_tp.stack_pos_info[stack_id], target_tp.bay_pos_info
                target_tp.holding_containers[tg_evt.c_id] = c
            else:
                assert False, vehicle
        
    def make_storage(self, l3_py):
        ### make QC Buffer
        for x in xrange(total_num_qb):
            if x == 0: QBs[x + 1] = QB(x + 1, 0, l3_py)
            else: QBs[x + 1] = QB(x + 1, 0, l3_py + container_vs * (8 + x * 2.2))
        ### make TP and Block
        block0_px, block0_py = Bitts[3].px, QBs[4].py + container_vs * 31
        for x in xrange(total_num_b):
            block_id = tp_id = None
            if x < 8:
                block_id = tp_id = 'A' + str(x + 1)
            else:
                block_id = tp_id = 'B' + str(x - 7)
            Blocks[block_id] = Block(block_id, block0_px + x * container_hs * 2.8, block0_py)
            TPs[tp_id] = TP(tp_id, block0_px + x * container_hs * 2.8 + container_vs * 0.5, block0_py - container_hs * 5.5 / 2)
            
    def set_deco_pos(self):
        ### set Lines deco position
        l0_py = container_vs * 31.2
        l1_py = l0_py + container_vs
        l2_py = l1_py + container_vs * 1
        self.lines_py = [eval('l%d_py' % x) for x in xrange(3)]
        ### set  bitts position
        bit0_px = container_hs * 0.7
        for x in xrange(total_num_bitt):
            Bitts[x + 1] = Bitt(x + 1, bit0_px + container_hs * 2.95 * x, l0_py)
        return l2_py
    
    def update_picture(self, simul_clock):
        for v in self.vessels + self.scs + self.qcs + self.ycs:
            if isinstance(v, Vessel):
                v.update(simul_clock)
            elif not v.evt_end:
                update(simul_clock, v)
        self.RefreshGC()
    
    def Draw(self, gc):
        gc.Translate(self.translate_x, self.translate_y)
        gc.Scale(self.scale, self.scale)
        if (self.scale > 2): 
            self.id_show = True
        else:
            self.id_show = False
        old_tr = gc.GetTransform()
        #brush sea
        bg_clr = wx.Colour(222, 242, 243)
        gc.SetBrush(wx.Brush(bg_clr))
        gc.SetPen(wx.Pen(bg_clr, 0))
        mg = 400 
        gc.DrawLines([(-mg, -mg), (self.sx + mg, -mg), (self.sx + mg, 1400), (-mg, 1400)])
        #brush land
        bg_clr = wx.Colour(241, 237, 220)
        gc.SetBrush(wx.Brush(bg_clr))
        gc.SetPen(wx.Pen(bg_clr, 0))
        gc.DrawLines(self.l_bg_ps)
        gc.SetPen(wx.Pen(wx.Colour(100, 100, 100), 0.5))
        for py in self.lines_py:
            gc.DrawLines([(0, py), (l_sx, py)])
        gc.DrawLines(self.deco_l1)
        gc.DrawLines(self.deco_l2)
            
        for x in Bitts.values() + QBs.values() + TPs.values() + Blocks.values():
            gc.Translate(x.px, x.py)
            x.draw(gc, self.id_show)
            gc.SetTransform(old_tr)
        #draw vehicle
        old_tr = gc.GetTransform()
        for x in self.vessels + self.qcs + self.ycs + self.scs:
#            print x, x.px, x.py
            gc.Translate(x.px, x.py)
            if isinstance(x, QC):
                x.draw(gc, self.id_show, self.Parent.is_gauge_show, self.Parent.is_al_loading_show, self.Parent.is_al_discharging_show)
            else:
                x.draw(gc, self.id_show)
            gc.SetTransform(old_tr)
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    Input_dialog(None, 'dialog test')
    app.MainLoop()
