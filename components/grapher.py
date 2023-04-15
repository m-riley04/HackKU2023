import matplotlib.pyplot as plt

class Grapher:
    def __init__(self, x:list, y:list, xAxisTitle="X-Axis", yAxisTitle="Y-Axis", yMax=10, xAxisInterval=1, yAxisInterval=1):
        self.x = x
        self.y = y
        self.xAxisTitle = xAxisTitle
        self.yAxisTitle = yAxisTitle
        self.xAxisInterval = xAxisInterval
        self.yAxisInterval = yAxisInterval
        self.graphType = None
        self.graph = None
    
    def set_graph_type(self, type):
        '''Sets the Graphers' graph type'''
        self.graphType = type
    
    def plot(self):
        '''Plots the Grapher's graph based on the graph type'''
        if self.graphType == None:
            raise TypeError("ERROR: Graph type cannot be None")
        
        if self.graphType == "bar":
            self.graph = plt.bar(x=self.x, height=self.y)
        elif self.graphType == "line":
            self.graph = plt.plot(x=self.x, y=self.y)
        elif self.graphType == "scatter":
            self.graph = plt.scatter(x=self.x, y=self.y)
        else:
            raise RuntimeError("ERROR: graph type not supported.")
        
        plt.show()
    
    def export(self):
        '''Exports the graph to an image file'''
        pass