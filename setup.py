"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['mictoggler.py']
DATA_FILES = ['mic-on.png', 'mic-off.png']
plist = dict(LSBackgroundOnly=True, argv_emulation=False)
OPTIONS = {'plist': plist}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
