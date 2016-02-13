import os


def setup_installed_apps(path):
    settings_file_path = os.path.join(path, "settings.py")
    lines = []
    with open(settings_file_path, "r") as f:
        for line in f.readlines():
            if line.startswith("INSTALLED_APPS"):
                line += "\t'django_environments',\n"
            lines.append(line)
    with open(settings_file_path, "w") as f:
        f.writelines(lines)
