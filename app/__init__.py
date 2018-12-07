#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

from flask import Flask

app = Flask(__name__) # pylint: disable=invalid-name

from app import routes  # pylint: disable=unused-import, wrong-import-position
