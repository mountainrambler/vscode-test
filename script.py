#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:46:16 2019

@author: peternystrom
"""


import requests


r = requests.get("http://www.industrivarden.se")
print(r.status_code)

