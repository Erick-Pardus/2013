#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


includedir = "/usr/include/irrlicht"
librarydir = "/usr/lib"
mainsrcdir = "source/Irrlicht"
srcversion = get.srcVERSION()
abiversion = srcversion.rsplit(".", 1)[0]


def setup():
    for i in ["jpeglib", "zlib", "libpng", "aesGladman"]:
        unwanteddir = "%s/%s" % (mainsrcdir, i)
        if shelltools.isDirectory(unwanteddir):
            shelltools.unlinkDir(unwanteddir)

    for i in ["include/*.h", "doc/upgrade-guide.txt", "%s/*.cpp" % mainsrcdir, "%s/*.h" % mainsrcdir]:
        pisitools.dosed(i, "\r")
        shelltools.chmod(i, 0644)

def build():
    shelltools.cd(mainsrcdir)
    autotools.make('sharedlib RPM_OPT_FLAGS="%s"' % get.CXXFLAGS() )

def install():
    autotools.rawInstall("-C %s INSTALL_DIR=%s/%s" % (mainsrcdir, get.installDIR(), librarydir))

    for i in ["libIrrlicht",  "libIrrXML"]:
        pisitools.dosym( "%s.so.%s" % (i, srcversion), "/usr/lib/%s.so.%s" % (i, abiversion))

    pisitools.dodoc("doc/*.txt", "*.txt")
    pisitools.dohtml("doc/html/*")
