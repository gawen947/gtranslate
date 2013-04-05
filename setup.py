#!/usr/bin/env python
# File: setup.py
#
#  Copyright (C) 2013 David Hauweele <david@hauweele.net>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
from distutils.core import setup

from gtranslate_const import *

setup(name=PKG_NAME,
         version=PKG_VERSION,
         description=PKG_DESCRIPTION,
         author=PKG_VERSION,
         author_email=PKG_AUTHOR_EMAIL,
         url=PKG_URL,
         scripts=["gtranslate"],
         py_modules=["gtranslate_const"],
         data_files=[(PKG_LIB_SH,["lib/translate.sh"]),
                     (PKG_SHARE,["ui/gtranslate.ui", "data/gtranslate.png", "data/languages.list"])])

if not os.access('/usr/local/lib/sh/', os.F_OK):
        os.mkdir('/usr/local/lib/sh')
if not os.access('/usr/local/share/gtranslate', os.F_OK):
        os.mkdir('/usr/local/share/gtranslate')
