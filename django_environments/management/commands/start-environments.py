from django.core.management.base import BaseCommand

from django_environments.core.environments import EnvironmentStarter, EnvironmentCreate


class Command(BaseCommand):
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('--ignore-develop',
                            action='store_false',
                            dest='can_create_develop',
                            default=True,
                            help='Does not create the develop environment.')

    def handle(self, *args, **options):
        from django.conf import settings
        EnvironmentStarter(settings.BASE_DIR).run()
        if options["can_create_develop"]:
            EnvironmentCreate(settings.BASE_DIR, "develop", environment_version_code="dev").run()
