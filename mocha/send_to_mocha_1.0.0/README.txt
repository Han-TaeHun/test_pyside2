Send to mocha for NUKE
Version: 1.0.0

Copyright (c) 2014, Imagineer Systems Ltd
All rights reserved.

See LICENSE.txt for license conditions.

Installation:

1. Extract the attached zipped folder to your ~/.nuke directory
2. Edit the Nuke init.py to add this line: nuke.pluginAddPath(‘./mocha’)

If you are not sure where the Nuke plugin path resides, load Nuke and in the script editor type: nuke.pluginPath()
- On MacOS it is normally located at /Users/YOUR_USERNAME/.nuke
- On Windows it is normally located at C:\users\YOUR_USERNAME\.nuke
- On Linux, the .nuke folder is located in your home directory

When you run Nuke with this script you should see a mocha icon in the lefthand panel. To run the script:

1. Select a read node in Nuke
2. Click the mocha icon
3. If Nuke asks you for the path to your mocha executable, browse to it.

The script should then load mocha with the footage.

While this should work on your machine, we can’t guarantee that it will work with everyone’s version of Python. Please contact support if you have any questions.


