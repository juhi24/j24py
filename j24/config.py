# -*- coding: utf-8 -*-
from os import path
import shutil
import configparser
from j24 import ensure_dir, home

HOME = home()
HERE = path.abspath(path.dirname(__file__))

class Configurer:
    def __init__(self, appname, template_path=HERE):
        self.appname = appname
        self.template_path = template_path

    def filename(self):
        return self.appname+'.conf'

    def conf_path_template(self):
        return path.join(self.template_path, self.filename() + '.template')

    def conf_path_user(self):
        return path.join(HOME, '.'+self.appname, self.filename())

    def conf_path_global(self):
        return path.join('/etc', self.filename())

    def conf_paths(self):
        return (self.config_path_user, self.config_path_global)

    def get_config_path(self):
        for p in self.config_paths():
            if path.isfile(p):
                return p
        return self.install_config()

    def install_config(self):
        user_file = self.conf_path_user()
        global_file = self.conf_path_global()
        template_file = self.conf_path_template()
        if path.isfile(user_file):
            conf_path = user_file
        elif path.isfile(global_file):
            conf_path = global_file
        else:
            try:
                conf_path = global_file
                shutil.copy(template_file, conf_path)
            except PermissionError as e:
                conf_path = user_file
                if not path.isfile(conf_path):
                    notice = 'Not installing as root. ' +\
                             'Installing configuration file to {}.'
                    print(notice.format(conf_path))
                    ensure_dir(path.dirname(conf_path))
                    shutil.copy(template_file, conf_path)
        return conf_path

    def initialize_config(self):
        config_path = self.get_config_path()
        conf = configparser.ConfigParser()
        conf.read(config_path)
        return conf
