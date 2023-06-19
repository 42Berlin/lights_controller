import requests
import json

row = 2
column = 5
requests.post(f'http://10.11.250.225:8080/api/v1/composition/layers/{row}/clips/{column}/connect')