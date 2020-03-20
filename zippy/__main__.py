import os
import yaml
from argparse import ArgumentParser

from .config_creator import create_config
from .folder_watcher import FolderWatcher


parser = ArgumentParser(description='A program for automatically unzipping and sorting zipfiles')
parser.add_argument('-c', '--config', action='store_true')
args = parser.parse_args()

config_exists = os.path.exists('zippy/config.yml')
if not config_exists or args.config:
    create_config(config_exists=config_exists)

with open('zippy/config.yml') as f:  # reading in our config
    config_list = yaml.load(f, Loader=yaml.FullLoader)['config']

folder_watchers = [FolderWatcher(**config) for config in config_list]