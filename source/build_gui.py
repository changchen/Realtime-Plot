#!/usr/bin/env python

import os

command = "pyuic4 -o ui_mainWindow.py ui/mainWindow.ui"
print command
os.system(command)
