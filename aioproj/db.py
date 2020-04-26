from sqlalchemy import (
    Table, Integer, MetaData, VARCHAR, Column
)


__all__ = ('Post_model', )

meta_post = MetaData()
Post_model = Table(
    'post', meta_post,
    Column('id', Integer, primary_key=True),
    Column('title', VARCHAR(255), nullable = True),
    Column('g_url', VARCHAR, ),
    Column('save_url', VARCHAR, )
)

meta_login = MetaData()

Login_model = Table(
    'login', meta_login,
    Column('id', Integer, primary_key=True),
    Column('username', VARCHAR(255), index = True, unique = True, ),
    Column('email', VARCHAR, index = True, unique = True, ),
    Column('password_hash', VARCHAR, )
)