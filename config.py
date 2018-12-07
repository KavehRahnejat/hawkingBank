"""
    Configuration for the application goes here.

    Most things are fetched from environment variables, for security reasons
    these are not set in the repo, you need to set them locally.

    To do this add: export {KEY}={VALUE} to your {virtualenv}/bin/activate

"""

import os


class Config:  # pylint: disable=too-few-public-methods
    """
        Variables should be placed in this class.

    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
