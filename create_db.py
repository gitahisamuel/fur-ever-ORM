from database import engine, Base
import models  # This ensures all model modules are imported so SQLAlchemy sees them

def init_db():
    Base.metadata.create_all(engine)
    print("Database and tables created (if they did not exist).")

if __name__ == "__main__":
    init_db()
