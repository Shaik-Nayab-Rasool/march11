import json, jwt, datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializer import UserSerializer
from django.views.decorators.csrf import csrf_exempt
import bcrypt
from .models import User
from .password import password_hash, password_check
from django.conf import settings

SECRET_KEY = settings.SECRET_KEY

# Create your views here.
def home_page(req):
        try:
            auth_token = req.headers.get('Authorization').split(' ')[1]
            decoded_token = jwt.decode(auth_token,SECRET_KEY,algorithms='HS256')
            print(decoded_token)
            return JsonResponse({"status":'Hello User Welcome to Home Page..!'})
        except:
            return JsonResponse({"status":'Hello user...Login first..!'})

@csrf_exempt
def register(req):
    user_data = json.loads(req.body)
    # user_password = user_data.get('password').encode('utf-8')
    # salt = bcrypt.gensalt(rounds=12)
    # hashed_password = bcrypt.hashpw(user_password,salt).decode('utf-8')
    user_data['password'] = password_hash(user_data['password'])
    user_obj = UserSerializer(data = user_data)
    if user_obj.is_valid():
        user_obj.save()
        return JsonResponse({'message':'User Register Successfully..!'})
    else:
        return JsonResponse(user_obj.errors)

@csrf_exempt
def login(req):
    if 'username' in req.COOKIES:
        return JsonResponse({'status':'Your already Logged in'})
    user_data = json.loads(req.body)
    # user_password = user_data.get('password').encode('utf-8')
    input_username = user_data.get('username')
    db_user = User.objects.get(username = input_username)
    # db_password = db_user.password.encode('utf-8')
    if password_check(user_data['password'],db_user.password):
        payload = {
            'user_id': 1,
            'username': 'Nayab',
            'iat': datetime.datetime.now(datetime.timezone.utc),
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')
        return JsonResponse({'status':'Login Success..!','token':token})
    else:
        return JsonResponse({'status':'Login Failed..!'})

@csrf_exempt 
def update(req):
    if not req.COOKIES.get('is_logged_in'):
        return JsonResponse({'status':'Login First..!'})
    user_data = json.loads(req.body)
    # user_password = user_data.get('password').encode('utf-8')
    # salt = bcrypt.gensalt(rounds=12)
    # hashed_password = bcrypt.hashpw(user_password,salt).decode('utf-8')
    user_username = user_data.get('username')
    user_data['password'] = password_hash(user_data['password'])
    user_obj = User.objects.get(username = user_username)
    updated_user = UserSerializer(user_obj, data = user_data, partial = True)
    if updated_user.is_valid():
        updated_user.save()
        return JsonResponse({'status':'Password Changed Successfully..!'})
    else:
        return JsonResponse(updated_user.errors)

def set_cookie(req):
    response = JsonResponse({'status':'Set Cookie'})
    response.set_cookie(
        key = 'theme',
        value = 'dark',
        max_age = 36,
        httponly=True       
    )
    return response

def log_out(req):
    if 'username' in req.session:
        req.session.flush()
        return JsonResponse({'status':'Logged out Successfully..!'})
    else:
        return JsonResponse({'status':'Log out Failed..!'})


# aws
# s3
# 
# render
# aiven
# cloudinary 