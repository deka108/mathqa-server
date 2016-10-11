"""
# Name:           meas/wsgi.py
# Description:
# Created by:     Auto
# Date Created:   Oct 07 2016
# Last Modified:  Oct 10 2016
# Modified by:    Phuc Le-Sanh
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meas_development.settings")

application = get_wsgi_application()
