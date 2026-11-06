# Google Maps API

## Get a Google Maps API Key

1. **Visit the GCP Console:**
   - Go to the [Google Cloud Platform Console](https://console.cloud.google.com/).

2. **Create a New Project:**
   - Click on the project dropdown at the top of the page.
   - Click on the “New Project” button.
   - Enter a project name and select your billing account.
   - Click “Create”.

   ![New Project](https://kevinli-webbertech.github.io/blog/images/googlemap/new_project.png)

3. **Enable the Google Maps APIs:**
   - Navigate to “APIs & Services” > “Library”.
   - Search for “Maps”.
   - Enable the following APIs:
     - Maps JavaScript API
     - Geocoding API
     - Directions API

   ![Enable APIs](https://kevinli-webbertech.github.io/blog/images/googlemap/enable_apis.png)
   ![Enable APIs 2](https://kevinli-webbertech.github.io/blog/images/googlemap/enable_apis2.png)

4. **Generate the API Key:**
   - Navigate to “Credentials” in the left sidebar of the APIs & Services dashboard.
   - Click on the “Create Credentials” button and select “API Key”.
   - Restrict the API Key to the APIs enabled in Step 3 and restrict its usage to your IP addresses or HTTP referrers.
   - Copy the API Key displayed on the screen.

   ![API Key](https://kevinli-webbertech.github.io/blog/images/googlemap/api_key.png)
   ![API Key 2](https://kevinli-webbertech.github.io/blog/images/googlemap/api_key2.png)

## Check Distance Python Example

### Step 4: Write the Python Script

```python
import googlemaps
from datetime import datetime

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# List of colleges in New Jersey
colleges = [
    "Atlantic Cape Community College",
    "Bergen Community College",
    "Bloomfield College",
    "Brookdale Community College",
    "Caldwell University",
    "Camden County College",
    "Centenary University",
    "College of Saint Elizabeth",
    "County College of Morris",
    "Cumberland County College",
    "Drew University",
    "Essex County College",
    "Fairleigh Dickinson University",
    "Felician University",
    "Georgian Court University",
    "Hudson County Community College",
    "Kean University",
    "Middlesex County College",
    "Monmouth University",
    "Montclair State University",
    "New Jersey City University",
    "New Jersey Institute of Technology",
    "Ocean County College",
    "Passaic County Community College",
    "Princeton University",
    "Ramapo College of New Jersey",
    "Raritan Valley Community College",
    "Rider University",
    "Rowan College at Burlington County",
    "Rowan College of South Jersey",
    "Rowan University",
    "Rutgers University",
    "Saint Peter's University",
    "Salem Community College",
    "Seton Hall University",
    "Stevens Institute of Technology",
    "Stockton University",
    "Sussex County Community College",
    "The College of New Jersey",
    "Thomas Edison State University",
    "Union County College",
    "Warren County Community College",
    "William Paterson University"
]

# Address to calculate distances from
origin = "Valley Mall Shopping Center, 977 Valley Rd, Gillette, NJ 07933"

# Function to validate addresses using Geocoding API
def validate_address(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result[0]['formatted_address'] if geocode_result else None

# Validate the origin address
validated_origin = validate_address(origin)
if not validated_origin:
    print(f"Origin address '{origin}' could not be validated.")
else:
    print(f"Validated Origin Address: {validated_origin}")

# Calculate Distances
distances = {}

for college in colleges:
    validated_college = validate_address(college)
    
    if not validated_college:
        print(f"College address '{college}' could not be validated.")
        continue
    
    try:
        directions_result = gmaps.directions(validated_origin, validated_college, mode="driving")
        
        if directions_result:
            distance = directions_result[0]['legs'][0]['distance']['text']
            distances[college] = distance
        else:
            print(f"No directions found for {college}")
    
    except googlemaps.exceptions.ApiError as e:
        print(f"API error for {college}: {e}")
    
    except Exception as e:
        print(f"Error for {college}: {e}")

# Print the distances
for college, distance in distances.items():
    print(f"{college}: {distance}")


