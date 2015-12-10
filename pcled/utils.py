from pcled import __author__
from pcled.core import __modules__

import serial
import argparse
import time


def assertion(obj, err):
    if obj is None:
        raise err


def check_stream(ser):
    return int.from_bytes(ser.read(), byteorder='little') == 1


def correct_intensity(val, maxBrightness=155):
    return (maxBrightness*v/255. for v in val)


def execute(func, delay=0.0, clock=10, maxBrightness=155, COM='COM3',
            PORT=9600, **kwargs):
    i = 0
    with serial.Serial(COM, PORT) as ser:
        if check_stream(ser):
            ser.write(b'%dc' % clock)
        while True:
            if check_stream(ser):
                r, g, b = correct_intensity(func(i=i, **kwargs), maxBrightness)
                ser.write(b'%dr%dg%db' % (r, g, b))
                if delay > 0.0:
                    time.sleep(delay)
                i = (i + 1) % 11


def get_args():
    parser = argparse.ArgumentParser(
        epilog="Written by %s" % __author__,
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p', '--program', dest='program',
                        help='Program to execute.',
                        choices=__modules__,
                        default='screen_glow')
    parser.add_argument('-s', '--serial-port', dest='COM',
                        help='Serial port device.', default='COM3', type=str)
    parser.add_argument('-a', '--port-address', dest='PORT',
                        help='Serial port address.', default=9600, type=int)
    parser.add_argument('-d', '--delay', dest='delay',
                        help='Signal delay (seconds)', default=0.0, type=float)
    parser.add_argument('-c', '--pixel-clock', dest='clock',
                        help='Pixel clock (milliseconds)',
                        default=10, type=int)
    parser.add_argument('-b', '--max-brightness', dest='maxBrightness',
                        help='Maximum brightness (0-255)',
                        default=155, type=int)
    parser.add_argument('-i', '--gpu-index', dest='deviceID',
                        help='Nvidia device index.', default=None, type=int)
    parser.add_argument('-m', '--color-map', dest='cmap',
                        help=('Color map for activity monitoring '
                              '(see matplotlib.pyplot.cm.datad for options).'),
                        default='cool', type=str)
    return parser
