import argparse
from random import randint

import aiohttp
import aioreloader

from aioproj import create_app
from aioproj.settings import load_config

parser = argparse.ArgumentParser(description="Aiohttp project")
parser.add_argument('--host', help = 'Host to listen', default="127.0.0.1")
parser.add_argument('--port', help = 'Port to accept connection', default='5000')
parser.add_argument(
    '--reload', 
    action="store_true", 
    help='Developer mode'
)

parser.add_argument('-c', '--config', type=argparse.FileType('r'),
    help='Path to configuration file'
)

args = parser.parse_args()

app = create_app(config = load_config(args.config))

if args.reload:
    print("Start with code reload")
    n = randint(0,3000)
    args.port = str(int(args.port) + n)
    aioreloader.start()

if __name__ == '__main__':
    aiohttp.web.run_app(app, host = args.host, port = args.port)