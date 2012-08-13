#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "TurboGears-1.0.4.3"

def install():
    pythonmodules.install()

    pisitools.dosed("%s/usr/bin/turbogears" % get.installDIR(),
                    get.installDIR(),
                    "/")