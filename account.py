import os
import jwt
import uuid
import hashlib
import requests
from urllib.parse import urlencode


access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']
server_url = "https://api.upbit.com"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)

print(res.json())