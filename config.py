"""
    Configuration for the application goes here.

    Most things are fetched from environment variables, for security reasons
    these are not set in the repo, you need to set them locally.

    To do this add: export {KEY}={VALUE} to your {virtualenv}/bin/activate

"""

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:  # pylint: disable=too-few-public-methods
    """
        Variables should be placed in this class.

    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

