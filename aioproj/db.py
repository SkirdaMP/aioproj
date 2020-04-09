from sqlalchemy import (
    Table, Integer, MetaData, VARCHAR, Column
)


__all__ = ('Post_model', )

meta = MetaData()
Post_model = Table(
    'post', meta,
    Column('id', Integer, primary_key=True),
    Column('title', VARCHAR(255), nullable = True),
    Column('g_url', VARCHAR, ),
    Column('save_url', VARCHAR, )
)