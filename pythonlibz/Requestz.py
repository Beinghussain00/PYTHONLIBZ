import requests # Invite the elder to your fireplace
# send message to a website and get a response
response = requests.get('https://www.mkglobalservices.com/') 

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful!")
else:
    print("Request failed with status code:", response.status_code)

    #print the respnse text (the content of the requested page)
    print (response.text)


    #print the response headers 
    print (response.headers) # Metadata about the response
    print (response.headers['Content-Type']) # Type of content returned
    print (response.headers['Content-Length']) # Size of the content in bytes
    print (response.headers['Server']) # Server software handling the request
    print (response.headers['Date']) # Date and time when the response was generated
    print (response.headers['Connection']) # Connection status
