from urllib import request
import json
def findjsonresp():
    url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
    query = input("what do you want to search for ? >>")
    query = request.urlretrieve({'q':query})
    response = request. (url+open).read()
    data =  json.loads (response)
    print (data)


print(findjsonresp())