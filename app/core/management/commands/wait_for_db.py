"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError):
                self.stdout.write("Postgresql hasn't started yet,\
                                  waiting 1 second...")
                time.sleep(1)
            except (OperationalError):
                self.stdout.write("Postgresql started but not yet fully setup,\
                                  waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
