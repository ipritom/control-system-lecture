import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

class LivePlot:
    def __init__(self, pause=0.02) -> None:
        self.x = []
        self.y = []
        self.pause = pause
        
        self.LIVE = False
        
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('close_event', self.__on_close)
        
        self.TERMINATED = False

    def __on_close(self, event):
        # user terminate the program
        self.TERMINATED = True
        plt.close()

    def update_plot(self, x, y):
        # update plot data
        self.__update_plot_data(x, y)

        # if terminated keep it terminated
        if self.TERMINATED:
            return
        
        # generate plot
        if not self.LIVE:
            self.LIVE = True
            plt.plot(self.x, self.y)
            plt.le
            plt.ion()
            return

        # clear current figure
        plt.clf()
        # Update the plot.
        
        plt.plot(self.x, self.y)

        plt.draw()
        plt.pause(0.02)

    def __update_plot_data(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def keep_showing(self):
        self.LIVE = False
        self.TERMINATED = False
        plt.clf()
        plt.ioff()
        plt.plot(self.x, self.y)
        plt.show()


class Trace:
    def __init__(self) -> None:
        self.x = []
        self.y = []
    
    def update_trace(self, x, y):
        self.x.append(x)
        self.y.append(y)

class LiveTrace:
    def __init__(self, pause=0.02) -> None:
        self.trace_list:list[Trace] = []
        self.pause = pause
        
        self.LIVE = False
        
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('close_event', self.__on_close)
        
        self.TERMINATED = False

    def __on_close(self, event):
        # user terminate the program
        self.TERMINATED = True
        plt.close()

    def update_plot(self):
        # update plot data
        # self.__update_plot_data(x, y)

        # if terminated keep it terminated
        if self.TERMINATED:
            return
        
        # generate plot
        if not self.LIVE:
            self.LIVE = True
            for trace in self.trace_list:
                plt.plot(trace.x, trace.y)
            plt.ion()
            return

        # clear current figure
        plt.clf()
        # Update the plot.
        
        for trace in self.trace_list:
            plt.plot(trace.x, trace.y)

        plt.draw()
        plt.pause(0.02)

    def __update_plot_data(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def keep_showing(self):
        self.LIVE = False
        self.TERMINATED = False
        plt.clf()
        plt.ioff()
        for trace in self.trace_list:
            plt.plot(trace.x, trace.y)
        plt.show()


if __name__ == "__main__":
    import time
    # lv = LivePlot(pause=0)
    live = LiveTrace(pause=0)

    t1 = Trace()
    t2 = Trace()
    live.trace_list = [t1, t2]
    for i in range(100):
        a = i
        b = 2*i**0.5
        print(a, b)
        # lv.update_plot(a, b)
        # time.sleep(1)
        t1.update_trace(a,b)
        t2.update_trace(b,a)
        live.update_plot()
    
    live.keep_showing()
