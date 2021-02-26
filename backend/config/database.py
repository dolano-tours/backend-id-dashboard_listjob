from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import env


engine = create_engine('mysql://{}:{}@{}/{}'.format(env.DB_USERNAME, env.DB_PASSWORD, env.DB_HOST, env.DB_NAME), convert_unicode=True)#bikin koneksi dengan database 
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  Base.metadata.create_all(bind=engine)