"""
# Name:           manage.py
# Description:
# Created by:     Auto
# Date Created:   Oct 07 2016
# Last Modified:  Oct 07 2016
# Modified by:    Phuc Le-Sanh
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "meas.development_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
