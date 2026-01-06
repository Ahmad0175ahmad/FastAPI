from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SERVER = "localhost"
DATABASE = "FastAPIDB"   # or master if you want default
DRIVER = "ODBC Driver 17 for SQL Server"

DATABASE_URL = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}"
    f"&Trusted_Connection=yes"
    f"&Encrypt=yes"
    f"&TrustServerCertificate=yes"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
