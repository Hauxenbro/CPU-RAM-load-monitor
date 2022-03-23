class Configurate_widgets:

    def configurate_powerbar(self):
        self.info_cpu = self.cpu.cpu_loading()
        self.info_ram = self.cpu.memory_load()

        for i in range(self.cpu.cpu_cores_logical):
            self.cpu_lbls[i]['text'] = f'CORE: {i+1}, LOAD: {self.info_cpu[i]}%'
            self.cpu_bars[i]['value'] = self.info_cpu[i]

        self.ram_lbl['text'] = f'RAM TOTAL: {round(self.info_ram[1] / 1048576)} MB, LOAD: {self.info_ram[2]}%,' \
                               f' AVAILABLE: {round(self.info_ram[1] / 1048576)} MB'
        self.ram_bar['value'] = self.info_ram[2]

        self.wheel = self.after(1000, self.configurate_powerbar)

    def move_window(self):
        if self.overrideredirect() == True:
            self.overrideredirect(False)
            self.move_btt['text'] = 'PIN'
            self.update()
        else:
            self.overrideredirect(True)
            self.move_btt['text'] = 'MOVE'
            self.update()

    def configurate_min_powerbar(self):
        self.info_cpu = self.cpu.cpu_loading_ov()
        self.info_ram = self.cpu.memory_load()
        self.cpu_bar_min['value'] = self.info_cpu
        self.ram_bar_min['value'] = self.info_ram[2]

        self.wheel_min = self.after(1000, self.configurate_min_powerbar)