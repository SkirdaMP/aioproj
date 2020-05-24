from datetime import datetime

from sqlalchemy import create_engine, MetaData

from aiodemo_polls.settings import config
from aiodemo_polls.db import question, choice

DSN = 'postgresql://{user}:{password}@{host}:{port}/{database}'

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[question, choice])

def sample_data(engine):
    conn = engine.connect()
    conn.execute(question.insert(), [
        {'question_text': 'What\'s new?', 
        'pub_date': datetime.utcnow()}
    ])
    conn.execute(choice.insert(), [
        {'choice_text': 'Not much', 'votes': 0, 'question_id': 1},
        {'choice_text': 'The sky', 'votes': 0, 'question_id': 1},
        {'choice_text': 'Just hacking again', 'votes': 0, 'question_id': 1},
    ])
    conn.close()

if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)