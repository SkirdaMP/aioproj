from aiohttp import web
from aiohttp_jinja2 import template
from sqlalchemy.sql import text
from sqlalchemy import select

from .. import db

@template('index.html')
async def index(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name}


async def post(request):
    async with request.app['db'].acquire() as conn:
        query = select([db.Post_model])
        result = await conn.fetch(query)

    return web.Response(body = str(result))