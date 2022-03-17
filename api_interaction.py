from time import clock_settime
import requests

def call_api(api_endpoint_url):
    '''calls the aws api that was created to run and cache google geocoding apis'''
    #call aws api endpoint
    inbound_response = requests.get(api_endpoint_url)
    
    #parse api response
    outbound_response = {'request_status': inbound_response.status_code, 'response_headers': inbound_response.headers, 'response_body': inbound_response.text}
    
    
    print(outbound_response)
    #print('request status: {}\nresponse headers: {}\nresponse body:{}'.format(response.status_code, response.headers, response.text))


#---------------program starts here---------------#

call_api(api_endpoint_url='https://eoo9fwrwdl.execute-api.us-west-2.amazonaws.com/test/geocode-address')