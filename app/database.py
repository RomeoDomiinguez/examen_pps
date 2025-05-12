from sqlmodel import create_engine, SQLModel

SQLITE_FILE_NAME="db.sqlite3"
engine = create_engine(f"sqlite:///{SQLITE_FILE_NAME}", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
