#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="everything-wallpaper" 

def setup():
     #shelltools.export("AUTOPOINT", "/bin/true")
     autotools.autoreconf("-vfi")
     autotools.configure("--disable-static")

def build():
     autotools.make()

def install():
     autotools.rawInstall("DESTDIR=%s" % get.installDIR())
     pisitools.dodoc("AUTHORS", "COPYING", "README")
