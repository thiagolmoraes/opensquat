# -*- coding: utf-8 -*-
# Module: __init__.py
"""
openSquat - Domain squatting and phishing detection library.

* https://github.com/atenreiro/opensquat

software licensed under GNU version 3
"""
__VERSION__ = "2.1.2"

from opensquat.app import Domain
from opensquat.phishing import Phishing
from opensquat.vt import VirusTotal
from opensquat.port_check import PortCheck
from opensquat.output import SaveFile

__all__ = [
    "__VERSION__",
    "Domain",
    "Phishing",
    "VirusTotal",
    "PortCheck",
    "SaveFile",
]
