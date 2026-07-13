from sqlalchemy import create_engine
import os
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
load_dotenv()
database_url=os.getenv("DATABASE_URL",'sqlite:///movie_explorer_database.db')

engine=create_engine(database_url)
Base=declarative_base()
sessionlocal=sessionmaker(bind=engine,autoflush=None,autocommit=False)
