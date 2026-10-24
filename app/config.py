"""Application configuration."""
import os

DEBUG = True
API_KEY = "demo_live_9f8e7d6c5b4a39281706f5e4d3c2b1a0"
DATABASE_URL = "postgresql://admin:Pa55w0rdDemo@localhost:5432/demo"
DATA_DIR = "/home/alice/projects/demo/data"
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
