import jwt


payload = {"user_id" : 1, "user_name" : "sample_user", "is_admin" : True}

secret_key = "hello_secreate_modulation_keys"

token = jwt.encode(payload, secret_key, algorithm="HS256")

print("token encoded : ",token)

decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])

print("token decoded : ",decoded_token)