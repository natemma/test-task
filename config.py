from pathlib import Path

BASE_DIR = Path(__file__).parent

INPUT_FILE = BASE_DIR / "data" / "amsterdam.osm.pbf"
OUTPUT_DIR = BASE_DIR / "output"

MIN_LON = 4.6274
MIN_LAT = 52.1712
MAX_LNG = 5.4339
MAX_LAT = 52.5258

MIN_ZOOM = 12
MAX_ZOOM = 16