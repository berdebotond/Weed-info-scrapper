"""Load configuration from .ini file."""
import configparser as configparser
import pathlib

""" Read local file `config.ini`."""

path_config_file = pathlib.Path(__file__).parent.absolute() / "config.ini"
config = configparser.ConfigParser()
config.read(path_config_file)

