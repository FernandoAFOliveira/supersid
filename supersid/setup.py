import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {
    'packages': ['matplotlib', 'numpy', 'pandas', 'pyalsaaudio', 'pyparsing', 'python-dateutil', 'ix', 'pyephem', 'PyAudio', 'PyPubSub', 'ounddevice'],
    'include_files': ['supersid.py', 'README.md', 'LICENSE'],
    'optimize': 2
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='SuperSID',
    version='1.00',
    description='A Python application for displaying Amateur Radio contacts and logging the activity.',
    options={'build_exe': build_exe_options},
    executables=[Executable('supersid.py', base=base, icon='icon.ico')]
)