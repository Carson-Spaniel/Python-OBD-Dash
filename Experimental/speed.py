import requests
import json
import time
import random

def create_compass():
    # Define the compass points and the total length
    compass_points = [
        "N", "30", "NE", "60", 
        "E", "120", "SE", "150", 
        "S", "210", "SW", "240", 
        "W", "300", "NW", "330"
    ]
    
    # Total length of the compass string
    total_length = 360
    num_points = len(compass_points)
    
    # Calculate the width of each segment
    segment_width = total_length // num_points
    
    # Create the compass string
    compass_str = ""
    for point in compass_points:
        compass_str += point.center(segment_width, " ")
    
    # Ensure the length is exactly 360 characters
    return compass_str[:total_length]

def get_compass_heading_display(heading, width=60):
    compass_str = create_compass()
    compass_len = len(compass_str)
    
    # Normalize heading to a value between 0 and 359
    normalized_heading = heading % 360
    # Calculate the index in the compass string
    index = int(normalized_heading * (compass_len / 360))
    
    # Calculate the starting index to center the heading
    start_index = (index - width // 2) % compass_len
    end_index = (start_index + width) % compass_len
    
    # Extract and return the relevant part of the compass string
    if start_index < end_index:
        display_str = compass_str[start_index:end_index]
    else:
        # Handle wrapping around the end of the string
        display_str = compass_str[start_index:] + compass_str[:end_index]
    
    return display_str

prev = 0
while True:
    heading = (prev + random.randint(0, 2)) % 360  # Example heading in degrees
    display_width = 50  # Width of the displayed compass portion
    display = get_compass_heading_display(heading, display_width)

    with open("../Data/compass.txt", "w") as file:
        file.write(str(display))
    print(f'({display})')
    print(heading)
    prev = heading

    # # Define the URL for the POST request
    # url = "http://127.0.0.1:5000/speed"

    # # Define the headers, specifying that we're sending JSON data
    # headers = {
    #     "Content-Type": "application/json"
    # }

    # lat, lon = 30.681598416806178, -97.7147931842906

    # if lat and lon:

    #     # Define the data payload as a Python dictionary
    #     data = {
    #         "lat": lat,
    #         "lon": lon
    #     }

    #     # Convert the dictionary to a JSON string
    #     json_data = json.dumps(data)

    #     try:
    #         # Send the POST request
    #         response = requests.post(url, headers=headers, data=json_data)
        
    #         with open("../Data/speed_limit.txt", "w") as file:
    #             file.write(str(response.json()['data']['speed_limit']))

    #     except requests.exceptions.RequestException as e:
    #         print(f"Request failed: {e}")
    
    time.sleep(.2)