import geopandas as gbd
from config import INPUT_FILE, OUTPUT_DIR

def load_layer(layer_name: str) -> gbd.GeoDataFrame:
    print(f"слой загружается: {layer_name}")
    return gbd.read_file(INPUT_FILE, layer = layer_name)

def save_layers(data,filename):
    path = OUTPUT_DIR / filename
    data.to_file(path, driver = "GeoJSON")

def extract_roads():
    lines = load_layer("lines")
    roads = lines[lines["highway"].notna()].copy()
    save_layers(roads, "roads.geojson")
def extract_water():
    lines = load_layer("lines")
    water_lines = lines[lines["waterway"].notna()].copy()
    polygons = load_layer("multipolygons")
    water_polygons = polygons[(polygons["natural"] == "water")].copy()
    water = gbd.GeoDataFrame(gbd.pd.concat([water_lines, water_polygons], ignore_index = True), crs = lines.crs)
    save_layers(water, "water.geojson")
def extract_building():
    polygons = load_layer("multipolygons")
    buildings = polygons[polygons["building"].notna()].copy()
    save_layers(buildings, "buildings.geojson")
def extract_landuse():
    polygons = load_layer("multipolygons")
    landuse = polygons[polygons["landuse"].notna()].copy()
    save_layers(landuse, "landuse.geojson")

if __name__ == "__main__":
    OUTPUT_DIR.mkdir(exist_ok=True)
    extract_roads()
    extract_water()
    extract_building()
    extract_landuse()