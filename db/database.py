import os

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


if os.environ.get("FASTAPI_ENV") == "development":
    database_url = "sqlite:///db.sqlite3"
    engine = create_engine(
        database_url, connect_args={"check_same_thread": False}
    )  # noqa
else:
    database_url = os.environ.get("DATABASE_URL").replace(
        "postgres", "postgresql"
    )  # noqa
    engine = create_engine(database_url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
