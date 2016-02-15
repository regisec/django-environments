from django.core.management.base import BaseCommand

from django_environments.core.environments import EnvironmentSwitch


class Command(BaseCommand):
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        from django.conf import settings
        EnvironmentSwitch(settings.BASE_DIR, options["name"]).run()
