from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    import app.api.tasks  # noqa: F401
    SQLModel.metadata.create_all(engine)
