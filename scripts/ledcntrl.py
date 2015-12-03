#! /usr/bin/env python

import pcled
from pcled.utils import assertion, execute, get_args

try:
    from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex
except ImportError:
    nvmlInit = nvmlDeviceGetHandleByIndex = None

try:
    import psutil
except ImportError:
    psutil = None

try:
    import matplotlib as mpl
except ImportError:
    mpl = None

try:
    import PIL
except ImportError:
    PIL = None


def parse_cmdln():
    parser = get_args()
    args = parser.parse_args()
    if args.program == 'gpu_temp':

        assertion(nvmlInit,
                  ImportError('nvidia-ml-py is required for this program.'))

        assertion(mpl,
                  ImportError('matplotlib is required for this program.'))

        assertion(args.deviceID,
                  AssertionError('GPU index must be declared.'))

        nvmlInit()
        args.handle = nvmlDeviceGetHandleByIndex(args.deviceID)

    if args.program == 'cpu_usage':

        assertion(psutil,
                  ImportError('psutil is required for this program.'))

    if args.program == 'screen_glow':

        assertion(PIL,
                  ImportError('PIL is required for this program.'))

    return args


if __name__ == "__main__":
    args = parse_cmdln()
    execute(getattr(pcled, args.program), **vars(args))
