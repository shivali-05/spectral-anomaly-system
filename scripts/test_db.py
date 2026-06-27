from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("MYSQL_PASSWORD")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/spectral_db"
)

connection = engine.connect()

print("Database connected successfully!")

connection.close()