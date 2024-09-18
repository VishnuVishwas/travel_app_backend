# config.py
class Config:
    # Path to the existing SQLite database created by Flutter
    SQLALCHEMY_DATABASE_URI = 'sqlite:///udupi_insights.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
