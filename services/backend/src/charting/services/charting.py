from abc import abstractmethod
from io import BytesIO

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



class ChartBuilder:

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def display_labels(self, title: str, xlabel: str, ylabel: str) -> None:
        pass

    @abstractmethod
    def display_legend(self, **kwargs) -> None:
        pass

    @abstractmethod
    def save(self, file_path: str) -> None:
        pass

    @abstractmethod
    def get_byte_chart(self) -> bytes:
        pass

    @abstractmethod
    def build_points(self, xdata: list, ydata: list, **kwargs) -> None:
        pass

    @abstractmethod
    def build_line(self, xdata: list, ydata: list, **kwargs) -> None:
        pass

    @abstractmethod
    def build_text(self, x: int|float, y: int|float, text: str, **kwargs) -> None:
        pass
    
    @abstractmethod
    def hline(self, y: int|float, xmin: int|float=0, xmax: int|float=1, **kwargs) -> None:
        pass
 
    @abstractmethod
    def vline(self, x: int|float, ymin: int|float=0, ymax: int|float=1, **kwargs) -> None:
        pass


class MatplotlibChartBuilder(ChartBuilder):

    def __init__(self, title: str, xlabel: str, ylabel: str, fontsize: int) -> None:
        self._title = title
        self._xlabel = xlabel
        self._ylabel = ylabel
        self._fontsize = fontsize

    @property
    def plt(self):
        return plt
    
    def reset(self) -> None:
        plt.clf()
        plt.rc('font', size=self._fontsize)
        self.display_labels(self._title, self._xlabel, self._ylabel)
    
    def display_labels(self, title: str, xlabel: str, ylabel: str) -> None:
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    
    def display_legend(self, **kwargs) -> None:
        kwargs['frameon'] = kwargs.get('frameon', False)
        kwargs['loc'] = kwargs.get('loc', 'upper right')
        plt.legend(**kwargs)
   
    def save(self, file_path: str) -> None:
        self.display_legend()
        plt.savefig(file_path)
    
    def get_byte_chart(self) -> bytes:
        self.display_legend()
        fig = plt.gcf()
        byte_buffer = BytesIO()
        fig.savefig(byte_buffer, format='png')
        byte_buffer.seek(0)
        return byte_buffer.getvalue()
    
    def build_points(self, xdata: list, ydata: list, **kwargs) -> None:
        plt.scatter(xdata, ydata, **kwargs)
    
    def build_line(self, xdata: list, ydata: list, **kwargs) -> None:
        plt.plot(xdata, ydata, **kwargs)
    
    def build_text(self, x: int | float, y: int | float, text: str, **kwargs) -> None:
        plt.text(x, y, text, **kwargs)

    def hline(self, y: int | float, xmin: int | float = 0, xmax: int | float = 1, **kwargs) -> None:
        plt.hlines(y=y, xmin=xmin, xmax=xmax, **kwargs)

    def vline(self, x: int | float, ymin: int | float = 0, ymax: int | float = 1, **kwargs) -> None:
        plt.vlines(x=x, ymin=ymin, ymax=ymax, **kwargs)
