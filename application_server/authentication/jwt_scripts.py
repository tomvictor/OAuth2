
import jwt
from jwt import InvalidTokenError

jwt_payload = {
  "token_type": "access",
  "exp": 1620131375,
  "jti": "5d6f7a57bd18409ea5c2679478edbfb6",
  "user_id": 49
}

c = {'token_type': 'access', 'exp': 1706529954, 'jti': '2b49d40413024c338ab1b05fa2c17352', 'user_id': 49}

signing_key = "w+jti1kra5si$(0934lv2u&6#%inaf3x0t4m+)4*t3r(=%4slj"
algorithm = "HS256"


access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NTMwNTU5LCJqdGkiOiI0NTE0MThjY2UzYWY0ZWMwYTQxMTFiMGI3NTdjNDc1NSIsInVzZXJfaWQiOjQ5fQ.Y4kiAffvvRg2o0QLnxwx7C45z5OAIP-yK2prWoaHcDg"



def main():
    # token = jwt.encode(jwt_payload, signing_key, algorithm=algorithm)
    # print(token)
    # encoded_token = token.decode('utf-8')
    # print(encoded_token)


    # decode
    jwt.decode(access_token, signing_key, algorithms=[algorithm], verify=True,
               audience=None, issuer=None,
               options={'verify_aud': False})


if __name__ == '__main__':
    main()