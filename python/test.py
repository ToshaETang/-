import json
import requests 


responsOBJ = requests.request("GET", 'http://20.194.192.246:10004/main/api/BusAPI/all/')


# if request success.
if int(responsOBJ.status_code) == 200:
    data = json.loads(responsOBJ.text)
    
    unique_counties = []
    counties = []
    routes = []
    for i in data:
        counties.append(i['county'])
        routes.append(i['routename'])
    
    for i in counties:
        if i not in unique_counties:
            unique_counties.append(i)
    
    route_count = [0 for i in range(0, len(unique_counties))]
    #[taipei, taoyuan, ..... 20]
    #[0,0,0,0,0,0,,000,0,0,,0,, .... 20]
    for i in counties:
        index = unique_counties.index(i)
        route_count[index] += 1
    
    for i, j in zip(unique_counties, route_count):
        print(i+"  "+str(j))
