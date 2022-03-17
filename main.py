#use google maps api to get address gps coordinates if they are not in the cache

from msilib.schema import Component
import googlemaps #for gmaps api
import json

#this could be retired and stored as an environment parameter on aws
import keys #to pull the gmaps api key

#leave the client in the global space for performance in context reuse for aws lambda
gmaps_client = googlemaps.Client(key=keys.google_api_key)

test_address = '5600 Nebraska Furniture Mart Dr, The Colony, TX'

def gmaps_geocode(address_to_geocode):
    '''call google maps api to fetch gps coordinates for the input address'''

    #call geocode api
    geocode_result = gmaps_client.geocode(address_to_geocode)    

    #format the response output
    output_string = json.dumps(geocode_result, indent=4)    

    print(output_string)

    #write response to a file    
    with open('./maps_output.txt', 'w') as gmaps_out:
        gmaps_out.write(output_string)


def extract_gps_coords(input_file):
    '''extract the lat and lng values from the google api call response and return them as a tuple'''

    #read response output file
    with open(input_file, 'r') as gmaps_out:
        gmaps_response = json.loads(gmaps_out.read())    

    #parse lat and lon from response data
    latitude = float(gmaps_response[0]['geometry']['location']['lat'])
    longitude = float(gmaps_response[0]['geometry']['location']['lng'])

    print('latitude = {}'.format(latitude))
    print('longitude = {}'.format(longitude))

    #return extracted values as a tuple
    return (latitude, longitude)


#call fuction to geocode the test address and output the response
gmaps_geocode(test_address)

#call function to pull gps coordinates from gmaps response
extract_gps_coords('./maps_output.txt')
