#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)  # pylint: disable=invalid-name
app.config.from_object(Config)
db = SQLAlchemy(app)  # pylint: disable=invalid-name
migrate = Migrate(app, db)  # pylint: disable=invalid-name

from app import routes, models  # pylint: disable=unused-import, wrong-import-position
