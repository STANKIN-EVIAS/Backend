#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys
import time

from psycopg2 import OperationalError

logger = logging.getLogger("evias")


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Make sure it's installed and your venv is active.") from exc

    logger.info("Starting EVIAS backend...")
    execute_from_command_line(sys.argv)


if __name__ == "__main__":

    max_retries = 5
    delay = 10  # seconds, will exponential backoff up to 30s

    for attempt in range(1, max_retries + 1):
        try:
            main()
            break
        except OperationalError as e:
            logger.info(
                f"Запуск backend задерживается, ожидание подключения к базе данных... (попытка {attempt}/{max_retries})"
            )
            if attempt == max_retries:
                logger.error("Max retries reached, exiting.")
                sys.exit(1)
            time.sleep(delay)
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            sys.exit(1)
