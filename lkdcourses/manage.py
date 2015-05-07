#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.path.exists('base/local_settings.py'):
        settings = 'base.local_settings'
    else:
        settings = 'base.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
