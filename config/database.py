from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import env

engine = create_engine('mysql://{}:{}@{}/{}'.format(env.DB_NAME, env.DB_PASSWORD, env.DB_HOST, env.DB_NAME), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
base.query = db_session.query_property()

def init_db():
  from ..models import model
  Base.metadata.create_all(bind=engine)