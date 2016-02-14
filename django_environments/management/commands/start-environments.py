from django.core.management.base import BaseCommand

from django_environments.core.environments import EnvironmentStarter, EnvironmentCreate


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        from django.conf import settings
        EnvironmentStarter(settings.BASE_DIR).run()
        EnvironmentCreate(settings.BASE_DIR, "develop", environment_version_code="dev").run()
