#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pickle
import sys
import os
from lib.config_system import get_config
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


from config import *


class settings_class:
    def __init__(self, test_mode_settings= False, debug= False):
        self.test_mode_settings = test_mode_settings
        self.debug_mode_settings = debug

        self.save_settings()

    def test_mode(self, value= None):
        if value is not None:
            self.test_mode_settings = value
            self.save_settings()
        else:
            return self.test_mode_settings

    def debug_mode(self, value=None):
        if value is not None:
            self.debug_mode_settings = value
            self.save_settings()
        else:
            return self.debug_mode_settings

    def save_settings(self):

        os.chdir(get_config().main_folder)
        with open(SETTING_PATH, 'wb') as settings_file:
            pickle.dump(self, settings_file, protocol= 2)



def the_settings():
    os.chdir(get_config().main_folder)

    if not os.path.exists(SETTING_PATH):
        return settings_class()

    with open(SETTING_PATH, 'rb') as settings_file:
        return pickle.load(settings_file)
