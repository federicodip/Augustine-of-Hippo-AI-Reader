import csv
import folium
import os

def read_csv_to_dict(csv_file):
    """
    Reads the CSV file and returns a dictionary where:
    key = place name
    value = (latitude, longitude) as floats
    Assumes CSV has two columns: 'Name', 'Coordinates'
    and coordinates are stored as 'lat,lon'.
    """
    name_coords = {}
    
    with open(csv_file, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)

        # If there's a header row, uncomment the next line to skip it:
        # next(reader)  
        
        for row in reader:
            if len(row) < 2:
                # Skip lines that don't have at least two columns
                continue
            
            name = row[0].strip()
            coords_str = row[1].strip()
            
            # Parse "lat,lon" string into float values
            try:
                lat_str, lon_str = coords_str.split(',')
                lat, lon = float(lat_str), float(lon_str)
                name_coords[name] = (lat, lon)
            except ValueError:
                # If splitting/casting fails, skip this row
                continue
    
    return name_coords

def read_text_file(txt_file):
    """
    Reads the .txt file and returns a list of place names (one per line).
    """
    places = []
    with open(txt_file, 'r', encoding='utf-8') as f:
        for line in f:
            place = line.strip()
            if place:
                places.append(place)
    return places

def create_map(place_coords, output_map="map.html"):
    """
    Create an interactive Folium map with markers for each place
    and save it to an HTML file (default: map.html).
    """
    # Center the map around the first valid coordinate or default to (0, 0).
    if place_coords:
        first_coord = next(iter(place_coords.values()))
        m = folium.Map(location=[first_coord[0], first_coord[1]], zoom_start=2)
    else:
        m = folium.Map(location=[0, 0], zoom_start=2)

    # Add a marker for each place
    for place, coords in place_coords.items():
        folium.Marker(
            location=[coords[0], coords[1]],
            popup=place,
            tooltip=place
        ).add_to(m)
    
    # Save the map to an HTML file
    m.save(output_map)
    print(f"Map has been created and saved to {output_map}")

def main():
    # Prompt the user for the paths to the .txt and .csv files
    txt_file = "places.txt"
    csv_file = "names.csv"

    # Optional: Check if the files exist
    if not os.path.isfile(txt_file):
        print(f"Error: The text file '{txt_file}' does not exist.")
        return
    if not os.path.isfile(csv_file):
        print(f"Error: The CSV file '{csv_file}' does not exist.")
        return
    
    # Read the CSV data into a dictionary
    name_coords = read_csv_to_dict(csv_file)
    
    # Read the list of places from the text file
    places_to_find = read_text_file(txt_file)
    
    # Collect coordinates for the matching names
    place_coords = {}
    for place in places_to_find:
        if place in name_coords:
            place_coords[place] = name_coords[place]
        else:
            print(f"Warning: '{place}' not found in CSV coordinates list.")
    
    # Create and save the map
    create_map(place_coords, output_map="map.html")

if __name__ == "__main__":
    main()
