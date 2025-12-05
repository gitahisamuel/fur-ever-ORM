from database import engine, Base
import models  

def init_db():
    Base.metadata.create_all(engine)
    print("Database and tables created (if they did not exist).")

if __name__ == "__main__":
    init_db()
