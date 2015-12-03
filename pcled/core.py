import numpy as np

try:
    from pynvml import nvmlDeviceGetTemperature
except ImportError:
    nvmlDeviceGetTemperature = None

try:
    from psutil import cpu_percent
except:
    cpu_percent = None

try:
    import matplotlib.pyplot as plt
except:
    mpl = None


try:
    from PIL import ImageGrab
except:
    ImageGrab = None

__modules__ = [
                'gpu_temp',
                'cpu_usage',
                'screen_glow',
                'random_glow'
                ]


def gpu_temp(handle=None, deviceID=0, cmap='cool', **kwargs):
    temp = nvmlDeviceGetTemperature(handle, deviceID)
    norm = min(max(temp - 30., 0.), 25.)/25.
    return plt.get_cmap(cmap)(norm, bytes=True)[:3]


def cpu_usage(cmap='cool', **kwargs):
    usage = cpu_percent()/100.
    return plt.get_cmap(cmap)(usage, bytes=True)[:3]


def screen_glow(**kwargs):
    img = ImageGrab.grab()
    return np.mean(img, (0, 1))


def random_glow(**kwargs):
    return np.random.randint(0, 255, 3)
