# -*- coding: utf-8 -*-
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import os


DEFAULT_STATIC_FOLDER = os.path.join(__path__[0], "static")
CUSTOM_STATIC_FOLDERS = []
from .theme import MTheme


dayu_theme = MTheme("dark", primary_color=MTheme.orange)
# dayu_theme.default_size = dayu_theme.small
# dayu_theme = MTheme('light')
