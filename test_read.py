from pathlib import Path
import geopandas as gpd
from config import INPUT_FILE

print("File is existing:", INPUT_FILE.exists())

layers = gpd.list_layers(INPUT_FILE)
print(layers)