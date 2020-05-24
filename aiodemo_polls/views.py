from aiohttp import web
from aiohttp_jinja2 import template

import db

@template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor_q = await conn.execute(db.question.select())
        records_q = await cursor_q.fetchall()
        cursor_c = await conn.execute(db.choice.select())
        records_c = await cursor_c.fetchall()
        questions = [dict(q) for q in records_q]
        choices = [dict(c) for c in records_c]
        return {'questions': questions, 'choices': choices, 'title': None}

