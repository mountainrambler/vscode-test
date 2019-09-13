#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:46:16 2019

@author: peternystrom
"""

import math
import os
import sys

import requests


# print(sys.version)
print("It starts here")
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    #    test = "test"
    return greeting


print(greet("World"))
print(greet("Peter"))

r = requests.get("http://www.industrivarden.se")
print(r.status_code)

