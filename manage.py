#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys
import time
import psycopg2
import subprocess
import os
from psycopg2 import OperationalError

from app.settings.dev import DATABASES

logger = logging.getLogger("evias")


def wait_for_db():
    db = DATABASES["default"]
    i = 0
    while i < 3:
        try:
            conn = psycopg2.connect(
                dbname=db.get("NAME"),
                user=db.get("USER"),
                password=db.get("PASSWORD"),
                host=db.get("HOST"),
                port=db.get("PORT"),
            )
            conn.close()
            print("База доступна, запускаем сервер...")
            break
        except psycopg2.OperationalError:
            print("База недоступна, пробуем снова через 10 секунд...")
            time.sleep(10)
            i += 1


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Make sure it's installed and your venv is active.") from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    wait_for_db()
    main()
