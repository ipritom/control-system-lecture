import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

class Plot:
    def __init__(self, title=None) -> None:
        self.x = []
        self.y = []
        self.title = title
    
    def update_plot(self, y=None, x=None):
        if x is None:
            if len(self.x)==0:
                x = 0
            else:
                x = self.x[-1]+1

        # update plot data
        self.x.append(x)
        self.y.append(y)

class LiveMonitor:
    def __init__(self, pause=0.02, sns_active=False) -> None:
        if sns_active:
            sns.set_theme()

        self.plot_list:list[Plot] = []
        self.pause = pause
        
        self.LIVE = False
        
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('close_event', self.__on_close)
        
        self.TERMINATED = False

    def __on_close(self, event):
        # user terminate the program
        self.TERMINATED = True
        plt.close()

    def __update_plots(self):
        # clear current figure
        plt.clf()
        # Update the plot.
        for plot in self.plot_list:
            plt.plot(plot.x, plot.y)
        
        plt.legend([p.title for p in self.plot_list])

    def update(self):
        # if terminated keep it terminated
        if self.TERMINATED:
            return
        
        # generate plot
        if not self.LIVE:
            self.LIVE = True
            self.__update_plots()
            plt.ion()
            return
        
        self.__update_plots()
        plt.draw()
        plt.pause(0.02)

    def keep_showing(self):
        # reset parameters
        self.LIVE = False
        self.TERMINATED = False
        # show plot
        plt.ioff()
        self.__update_plots()
        plt.show()


if __name__ == "__main__":
    import time
    # lv = LivePlot(pause=0)
    live = LiveMonitor(pause=0)

    t1 = Plot(title="A")
    t2 = Plot(title="B")
    live.plot_list = [t1, t2]
    for i in range(100):
        a = i
        b = 2*i**0.5
        print(a, b)
        # lv.update_plot(a, b)
        # time.sleep(1)
        t1.update_plot(a,b)
        t2.update_plot(b,a)
        live.update()
    
    live.keep_showing()