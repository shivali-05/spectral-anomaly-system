from sqlalchemy import create_engine

password = "mySQL2026"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/spectral_db"
)

connection = engine.connect()

print("Database connected successfully!")

connection.close()