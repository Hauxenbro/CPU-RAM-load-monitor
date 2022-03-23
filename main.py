import tkinter as tk
import sys, cpu_work, configurates_widg
from tkinter import ttk

class CPU_App(tk.Tk, configurates_widg.Configurate_widgets):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.cpu = cpu_work.CPU_info()
        self.starting_ui()
    def starting_ui(self):
        self.set_ui()
        self.make_powerbar()

    def set_ui(self):
        exit_btt = tk.Button(self, text = 'EXIT', command = self.exit_app)
        exit_btt.pack(fill = tk.X)

        menu_fr = ttk.LabelFrame(self, text = 'MANUAL')
        menu_fr.pack(fill = tk.X)
        self.variant_box = ttk.Combobox(menu_fr, values = ['hide', 'non-hide', 'min'], width = 9)
        self.variant_box.current(1)
        self.variant_box.pack(side = tk.LEFT)
        self.move_btt = tk.Button(menu_fr, text = 'MOVE', command = self.move_window)
        self.move_btt.pack(side = tk.LEFT)
        arrows_btt = tk.Button(menu_fr, text = '>>>', command = '')
        arrows_btt.pack(side = tk.LEFT)

        self.power_fr = ttk.LabelFrame(self, text = 'POWER')
        self.power_fr.pack(fill = tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.variant_box.bind('<<ComboboxSelected>>', self.check_min)

    def make_powerbar(self):
        self.cpu_lbls = []
        self.cpu_bars = []
        self.cpu_info_lbl = tk.Label(self.power_fr, text=f'Physical cores: {self.cpu.cpu_cores},'
                                                    f' logical cores: {self.cpu.cpu_cores_logical}')
        self.cpu_info_lbl.pack(fill = tk.X)
        for i in range(self.cpu.cpu_cores_logical):
            self.cpu_lbl = tk.Label(self.power_fr, anchor=tk.CENTER)
            self.cpu_bar = ttk.Progressbar(self.power_fr, length=100)
            self.cpu_lbls.append(self.cpu_lbl)
            self.cpu_bars.append(self.cpu_bar)
            self.cpu_lbl.pack(fill=tk.X)
            self.cpu_bar.pack(fill=tk.X)

        self.ram_lbl = tk.Label(self.power_fr)
        self.ram_lbl.pack(fill = tk.X)
        self.ram_bar = ttk.Progressbar(self.power_fr, length = 100)
        self.ram_bar.pack(fill = tk.X)
        self.configurate_powerbar()

    def clear_widg(self):
        for i in self.winfo_children():
            i.destroy()
        self.update()


    def check_min(self, event):
        if self.variant_box.current() == 2:
            self.enter_mouse('')
            self.unbind_class('Tk', '<Enter>')
            self.unbind_class('Tk', '<Leave>')
            self.variant_box.unbind('<<ComboboxSelected>>')
            self.after_cancel(self.wheel)
            self.clear_widg()
            self.make_minimal()
    def make_minimal(self):
        self.cpu_bar_min = ttk.Progressbar(length = 100)
        self.cpu_bar_min.pack(side = tk.LEFT)
        self.ram_bar_min = ttk.Progressbar(length = 100)
        self.ram_bar_min.pack(side = tk.LEFT)
        self.full_btt = tk.Button(text = 'FULL', command = self.make_full)
        self.full_btt.pack(side = tk.RIGHT)
        self.move_btt = tk.Button(text='MOVE', command=self.move_window)
        self.move_btt.pack(side=tk.RIGHT)
        self.update()
        self.configurate_min_powerbar()

    def make_full(self):
        self.after_cancel(self.wheel_min)
        self.clear_widg()
        self.starting_ui()
        self.variant_box.current(1)
        self.enter_mouse('')

    def enter_mouse(self, event):
        if self.variant_box.current() == 0 or 1:
            self.geometry('')
    def leave_mouse(self, event):
        if self.variant_box.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def exit_app(self):
        self.destroy()
        sys.exit()

if __name__ == '__main__':
    root = CPU_App()
    root.mainloop()