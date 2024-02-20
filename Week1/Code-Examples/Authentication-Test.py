import requests
 
reqUrl = "https://runtime-us-east.quantum-computing.ibm.com/jobs?limit=10&offset=0&exclude_params=true"
 
headersList = {
  "Accept": "application/json",
  "Authorization": "Bearer YOUR_API_TOKEN_HERE"
}
 
payload = ""
 
response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
 
print(response.json())