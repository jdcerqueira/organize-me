import requests
from datetime import datetime, timedelta
from jwcrypto import jwe, jwk
from jwcrypto.common import json_encode, json_decode
import json

DATETIME_NOW = datetime.now()
DATETIME_FIFTEEN = DATETIME_NOW + timedelta(minutes=15)

r = requests.get("http://localhost:8080/fontes/bancos/vinculados")
payload = {"return": r.json()}

public_key = jwk.JWK()
private_key = jwk.JWK.generate(kty="RSA", size=2048)
public_key.import_key(**json_decode(private_key.export_public()))

protected_header = {
    "alg":"RSA-OAEP-256",
    "enc":"A256CBC-HS512",
    "typ":"JWE",
    "kid":public_key.thumbprint()
}

jweToken = jwe.JWE(str(payload).encode("utf-8"), recipient=public_key, protected=protected_header)
encrypted_token = jweToken.serialize()


jweToken = jwe.JWE()
jweToken.deserialize(encrypted_token,key=private_key)
decrypted_json = jweToken.payload
print(str(decrypted_json))