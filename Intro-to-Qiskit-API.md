## Intro to Qiskit REST API
* Main Documentation: [Link](https://docs.quantum.ibm.com/api/runtime)
* The Qiskit IBM Runtime REST API allows you to run on quantum systems using Qiskit Runtime primitives, a simplified interface for circuit execution powered by advanced runtime compilation, error suppression, and error mitigation techniques, as well as getting information about instances and systems you have access to.

## Backend Setup
1. Set up Qiskit and IBM Quantum account:
* Install Qiskit: Follow the installation instructions on the (Qiskit documentation).
* Create an IBM Quantum account: Sign up on the (IBM Quantum Experience) website.

2. Get API key and access token:
* After creating an IBM Quantum account, generate an API key from the IBM Quantum Experience dashboard.
* Use the API key to generate an access token.
* Authentication Test:
```
import requests
 
reqUrl = "https://runtime-us-east.quantum-computing.ibm.com/jobs?limit=10&offset=0&exclude_params=true"
 
headersList = {
  "Accept": "application/json",
  "Authorization": "Bearer YOUR_API_TOKEN_HERE" 
}
 
payload = ""
 
response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
 
print(response.json())
```
