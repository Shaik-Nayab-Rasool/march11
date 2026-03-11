# import jwt
# import datetime

# secret_key = 'f9f9f9f9f9f9f9f9f9f9'

# payload = {
#     'user_id': 1,
#     'username': 'Nayab',
#     'iat': datetime.datetime.now(datetime.timezone.utc),
#     'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
# }

# token = jwt.encode(payload,secret_key,algorithm='HS256')
# print(token)

# decoded_token = jwt.decode(token,'TATA Salt2343546578fv',algorithms='HS256')
# print(decoded_token)