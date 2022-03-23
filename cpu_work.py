import psutil as pst

class CPU_info:

    def __init__(self):
        self.cpu_cores = pst.cpu_count(logical = False)
        self.cpu_cores_logical = pst.cpu_count(True)

    def cpu_loading(self):
        return pst.cpu_percent(percpu=True)
    def cpu_loading_ov(self):
        return pst.cpu_percent(False)
    def memory_load(self):
        return pst.virtual_memory()