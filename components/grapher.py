import matplotlib

class Grapher:
    def __init__(self, data, xAxisTitle="X-Axis", yAxisTitle="Y-Axis", xAxisInterval=1, yAxisInterval=1):
        self.data = data
        self.xAxisTitle = xAxisTitle
        self.yAxisTitle = yAxisTitle
        self.xAxisInterval = xAxisInterval
        self.yAxisInterval = yAxisInterval
    
    def plot(self):
        pass
    
    def export(self):
        pass