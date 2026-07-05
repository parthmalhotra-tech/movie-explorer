from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('sqlite:///movie_explorer_database.db')
Base=declarative_base()
sessionlocal=sessionmaker(bind=engine,autoflush=None,autocommit=False)
