"""
tkSidViewer class implements a graphical user interface for SID based on tkinter
"""
from __future__ import print_function
import matplotlib
# matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

# handle both Python 2 and 3
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

import supersid_plot as SSP
from config import FILTERED, RAW

class tkSidViewer(tk.Frame):
    '''
    Create the Tkinter GUI
    '''
    def __init__(self, controller):
        """SuperSID Viewer using Tkinter GUI for standalone and client.
        Creation of the Frame with menu and graph display using matplotlib
        """
        matplotlib.use('TkAgg')
        self.version = "1.3.1 20130817"
        self.controller = controller  # previously referred as 'parent'
        self.tk_root = tk.Tk()
        tk.Frame.__init__(self, self.tk_root, background="white")
        self.tk_root.title("supersid @ " + self.controller.config['site_name'])

        # All Menus creation

        # Frame
        self.pack(fill=tk.BOTH, expand=1)

        # FigureCanvas
        self.psd_figure = Figure(facecolor='beige')
        self.canvas = FigureCanvas(self.psd_figure, self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2TkAgg( self.canvas, self )
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.axes = self.psd_figure.add_subplot(111)
        self.axes.hold(True)

        # StatusBar


        # Default View

    def run(self):
        self.tk_root.mainloop()

    def close(self):
        self.tk_root.quit()

    def updateDisplay(self, msg=None):
        """
        Receives data from thread and updates the display (graph and statusbar)
        """
        print("in updateDisplay")
        try:
            self.canvas.draw()
            if msg:
                self.status_display(msg.data)
        except:
            pass

    def clear(self):
        try:
            self.axes.cla()
        except:
            pass

    def status_display(self, message, level=0, field=0):
        pass


    def get_psd(self, data, NFFT, FS):
        """By calling 'psd' within axes, it both calculates and plots the spectrum"""
        print("in get_psd")
        #try:
        self.clear()
        Pxx, freqs = self.axes.psd(data, NFFT = NFFT, Fs = FS)
        #except wx.PyDeadObjectError:
        #    exit(3)
        self.updateDisplay()
        return Pxx, freqs