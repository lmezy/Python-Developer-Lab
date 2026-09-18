from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings

url = get_settings().database_url
if url.startswith("sqlite:///"):
    database_path = url.removeprefix("sqlite:///")
    Path(database_path).parent.mkdir(parents=True, exist_ok=True)
engine = create_engine(
    url, connect_args={"check_same_thread": False} if url.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
