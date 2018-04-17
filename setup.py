import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = 'c:/python34/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'c:/python34/tcl/tk8.6'

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['c:/python34/DLLs/tcl86t.dll', 'c:/python34/DLLs/tk86t.dll']
)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('crypto.py', base=base)
]

setup(name='crypto',
      version = '1.1',
      description = 'Let talk safely now !!',
      options = dict(build_exe = buildOptions),
      executables = executables)
