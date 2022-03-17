#use google maps api to get address gps coordinates if they are not in the cache

import googlemaps #for gmaps api
import json

#this could be retired and stored as an environment parameter on aws
import keys #to pull the gmaps api key

#leave the client in the global space for performance in context reuse for aws lambda
gmaps_client = googlemaps.Client(key=keys.google_api_key)

test_address = '5600 Nebraska Furniture Mart Dr, The Colony, TX'

def gmaps_geocode(address):
    '''call google maps api to fetch gps coordinates for the input address'''

    try:
        geocode_result = gmaps_client.geocode(address)

        #format the response output
        output_string = json.dumps(geocode_result, indent=4)

        print(output_string)
        
        with open('./maps_output.txt', 'w') as gmaps_out:
            gmaps_out.write(output_string)

    except:
        print('an exception occured, and retries did not resolve it')



#call fuction to geocode the test address and output the response
gmaps_geocode(test_address)
