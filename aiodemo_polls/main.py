"""
Run aioapp and settings him
"""

import asyncio

from aiohttp import web
import aiohttp_jinja2
import jinja2

from db import close_pg, init_pg
from middlewares import setup_middlewares
from settings import config, BASE_DIR
from routes import setup_routes

loop = asyncio.get_event_loop()

app = web.Application(loop=loop)

setup_routes(app)
setup_middlewares(app)
app['config'] = config
aiohttp_jinja2.setup(app, 
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'aiodemo_polls' / 'templates')))
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

web.run_app(app, host='127.0.0.1')
