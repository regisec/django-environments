import os
import shutil
import re

from django_habitat import exceptions, __version__, templates


class BaseEnvironment:
    def __init__(self, django_project_path):
        django_settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", None)
        if django_settings_module is None:
            msg = "Environment DJANGO_SETTINGS_MODULE not found."
            raise exceptions.IncompatibleProjectSetup(msg)
        settings_values = django_settings_module.split(".")
        settings_file_name = "{0}.py".format(settings_values.pop(-1))
        settings_dir_path = os.path.join(*([django_project_path] + settings_values))
        self.settings_file_path = os.path.join(settings_dir_path, settings_file_name)
        self.settings_module_path = os.path.join(settings_dir_path, "settings")

    def build_environment_file_name(self, environment_name):
        return "{0}.py".format(environment_name.replace(" ", "-").lower())

    def run(self):
        raise NotImplemented("The run() method must be implemented.")


class EnvironmentStarter(BaseEnvironment):
    def __init__(self, django_project_path):
        BaseEnvironment.__init__(self, django_project_path)
        self.settings_init_path = os.path.join(self.settings_module_path, "__init__.py")

    def validate(self):
        if not os.path.exists(self.settings_file_path):
            msg = "Django settings file not found. ({0})".format(self.settings_file_path)
            raise exceptions.IncompatibleProjectSetup(msg)
        if not os.path.isfile(self.settings_file_path):
            msg = "Django settings must be a file. ({0})".format(self.settings_file_path)
            raise exceptions.IncompatibleProjectSetup(msg)
        if os.path.exists(self.settings_module_path):
            msg = "Django environments settings module already exists. ({0})".format(self.settings_module_path)
            raise exceptions.IncompatibleProjectSetup(msg)

    def setup_common(self):
        path = os.path.join(self.settings_module_path, "common.py")
        shutil.move(self.settings_file_path, path)
        lines = []
        with open(path, "r") as f:
            # TODO: SEARCH ANOTHER VERSION FIRST
            for line in f.readlines():
                if line.startswith("BASE_DIR"):
                    line_data = "=".join([v.strip() for v in line.replace("\n", "").split("=")[1:]])
                    line = "BASE_DIR = os.path.dirname({0})\n".format(line_data)
                lines.append(line)
        lines.append("\nVERSION = \"0.0.0\"\n")
        with open(path, "w") as f:
            f.writelines(lines)

    def run(self):
        self.validate()
        os.mkdir(self.settings_module_path)
        self.setup_common()
        templates.process_init_template(self.settings_init_path, VERSION=__version__)


class EnvironmentCreate(BaseEnvironment):
    file_name_validator = re.compile("^[\d\w_]+\.py$")
    reserved_names = ["__init__.py", "__habitat__.py", "common.py"]

    def __init__(self, django_project_path, environment_name, environment_version_code=""):
        BaseEnvironment.__init__(self, django_project_path)
        self.environment_name = " ".join([w.capitalize() for w in environment_name.split(" ")])
        self.environment_version_code = environment_version_code
        self.environment_file_name = self.build_environment_file_name(environment_name)
        self.settings_environment_path = os.path.join(self.settings_module_path, self.environment_file_name)

    def validate(self):
        if not self.file_name_validator.match(self.environment_file_name):
            msg = "Environment name must contain one or more numbers, letters or underlines."
            raise exceptions.InvalidEnvironmentName(msg)
        if self.environment_file_name in self.reserved_names:
            msg = "This name is reserved."
            raise exceptions.InvalidEnvironmentName(msg)
        if os.path.exists(self.settings_environment_path):
            msg = "This name is already in use."
            raise exceptions.InvalidEnvironmentName(msg)

    def run(self):
        self.validate()
        templates.process_environment_template(self.settings_environment_path,
                                               VERSION=__version__,
                                               ENVIRONMENT_NAME=self.environment_name,
                                               ENVIRONMENT_VERSION_CODE=self.environment_version_code)


class EnvironmentSwitch(BaseEnvironment):
    def __init__(self, django_project_path, environment_name):
        BaseEnvironment.__init__(self, django_project_path)
        self.environment_name = " ".join([w.capitalize() for w in environment_name.split(" ")])
        self.environment_file_name = self.build_environment_file_name(environment_name)
        self.settings_environment_path = os.path.join(self.settings_module_path, self.environment_file_name)
        self.settings_load_path = os.path.join(self.settings_module_path, "__habitat__.py")

    def validate(self):
        if not os.path.exists(self.settings_environment_path):
            msg = "Environment not found."
            raise exceptions.InvalidEnvironmentName(msg)

    def run(self):
        self.validate()
        try:
            os.remove(self.settings_load_path)
        except OSError:
            pass
        finally:
            shutil.copy(self.settings_environment_path, self.settings_load_path)
