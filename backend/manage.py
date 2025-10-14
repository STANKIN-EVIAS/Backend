#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

logger = logging.getLogger("evias")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings.dev')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and your venv is active."
        ) from exc

    logger.info("Starting EVIAS backend...")
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
