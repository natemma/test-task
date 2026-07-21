import subprocess
from pathlib import Path

OUTPUT = Path("output/amsterdam.mbtiles")

if OUTPUT.exists():
    OUTPUT.unlink()

OUTPUT_DIR = Path("output")
OUTPUT = OUTPUT_DIR / "amsterdam.mbtiles"

command = [
    "tippecanoe",
    "-o", str(OUTPUT),

    "-Z", "12",
    "-z", "16", 
    "--force",

    "-L", f"roads:{OUTPUT_DIR / 'roads.geojson'}",
    "-L", f"buildings:{OUTPUT_DIR / 'buildings.geojson'}",
    "-L", f"water:{OUTPUT_DIR / 'water.geojson'}",
    "-L", f"landuse:{OUTPUT_DIR / 'landuse.geojson'}"
]
print("Создание MBTiles")

subprocess.run(command, check=True)
print(OUTPUT)