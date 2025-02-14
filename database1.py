from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

data_url='mysql+pymysql://root:hellosunny@localhost:3306/mruh'

engine = create_engine(data_url)

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()