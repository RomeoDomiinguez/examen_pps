from sqlmodel import create_engine, SQLModel

SQLITE_FILE_NAME = "db.sqlite3"
engine = create_engine(f"sqlite:///{SQLITE_FILE_NAME}", echo=True)


def create_db_and_tables():
    """Crea todas las tablas definidas en los modelos SQLModel."""
    SQLModel.metadata.create_all(engine)
