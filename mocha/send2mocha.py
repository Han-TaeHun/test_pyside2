#!/usr/bin/env python
# coding=utf-8

###    send2mocha.py v1.1
###    Created: 2010/01/10
###    Modified: 2012/05/18
###    Written by Diogo Girondi
###    diogogirondi@gmail.com

import os
import nuke
import nukescripts

def send2mocha( node=None, mocha_path=None ):

    """
    send2mocha( node, mocha_path )

    Opens the node passed as argument or the selected one in Mocha for further work.

    :param node: Node Object. A Nuke node object. This is optional, if not passed it will use the selected node.
    :param mocha_path: String. The path for the MochaPro application.
    """

    if not node:
        try:
            node = nuke.selectedNode()
        except ValueError:
            nuke.message( 'Select a node' )
            return

    if not mocha_path:
        raise RuntimeError( 'You must supply the Mocha application path for this script to work' )

    switches = None

    if nuke.env['MACOS']:
        switches = 'open -a'

    if 'file' in node.knobs().keys():
        try:
            filename = nukescripts.replaceHashes( node.knob('file').value() ) % node.firstFrame()
        except TypeError:
            filename = node.knob('file').value()

        file_ext = filename.split('.')[-1]
        if file_ext.lower() in ('r3d'):
            nuke.message( 'Mocha currently does not support {0:>s} files'.format(file_ext) )
            return

        cmd = '"{0:>s}" "{1:>s}"'.format( mocha_path, filename )
        if switches:
            cmd = '{0:>s} {1:>s}'.format( switches, cmd )
        os.system( cmd )
    else:
        nuke.message( 'Select a node that has a file knob' )