import jwt   # PyJWT 
import uuid
import os

ACCESS_KEY=os.environ['ACCESS_KEY']

payload = {
    'access_key': ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, ACCESS_KEY)
authorization_token = 'Bearer {}'.format(jwt_token)
print(authorization_token)