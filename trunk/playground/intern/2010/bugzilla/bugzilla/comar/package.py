#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("./var/www/localhost/htdocs/bugzilla/checksetup.pl")
