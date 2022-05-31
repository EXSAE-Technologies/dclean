from importlib import import_module
import os

# Base directory
BASE_DIR = os.path.dirname(__file__)

# Loaded plugins
PLUGINS = list()

# Plugin directory
PLUGIN_DIR = f"{BASE_DIR}/plugins/"

# Load plugins
for pld in os.listdir(PLUGIN_DIR):
    if os.path.isdir(f"{PLUGIN_DIR}/{pld}"):
        if os.path.exists(f"{PLUGIN_DIR}/{pld}/config.py"):
            PLUGINS.append(import_module(f'plugins.{pld}.config'))