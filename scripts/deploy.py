# -*- coding: utf-8 -*-
"""

"""

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import json
import os
import subprocess


__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-11-28 17:12:13"


DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(DIR, "deploy.json"), "r") as f:
    data = json.load(f)


username = data.get("username")
password = data.get("password")
subprocess.check_call(
    f"poetry publish --build --username {username} --password {password}"
)
