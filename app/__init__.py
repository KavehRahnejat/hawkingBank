"""
    Here you should import any routes / apis you want to have included in the
    application.

"""

from flask import Flask

app = Flask(__name__) # pylint: disable=invalid-name

from app import routes  # pylint: disable=unused-import, wrong-import-position
