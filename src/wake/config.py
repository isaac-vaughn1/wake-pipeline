from pathlib import Path 

PROJECT_ROOT = Path(__file__).resolve().parents[2]

BASE_URL = "https://ocmgeodatastor1.blob.core.windows.net/marinecadastre/ais2024/"
LANDING_DIR = PROJECT_ROOT / "data" / "raw" / "ais"
DB_PATH = PROJECT_ROOT / "data" / "warehouse.duckdb"
TEMP_DIR = PROJECT_ROOT / "data" / "tmp"
