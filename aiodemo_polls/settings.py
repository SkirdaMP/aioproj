import pathlib
import yaml

ROOT_DIR = pathlib.Path(__file__).parent.parent.parent
BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'polls.yaml'

def get_config(path):
    with open(path) as f:
        pass
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)