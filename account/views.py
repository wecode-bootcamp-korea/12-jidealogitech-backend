import json
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse, HttpResponse

from account.models import Account
from django.db import IntegrityError

class  SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if '@' not in data['email']:
                return JsonResponse(
					{"message":"Email_Not_Verified"},
					status = 404
                )
            elif len(data['email']) < 3:
                return JsonResponse(
                    {"message":"Email_length_short"}
                )
          
            elif len(data['password']) < 5:
                return JsonResponse(
					{"message":"Password_Not_Verified"},
					status = 411
                )

            if Account.objects.filter(email = data['email']).exists():
               return JsonResponse({"message":"ACCOUNT_ALREADY_EXIST"},stauts=401)
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            Account(
                email    = data['email'],
                password = hashed_password,
                # name     = data['name'],
                # language = data['language'],
                # country  = data['country'],
                # birthday = data['birthday'],
                # phone    = data['phone'],
            ).save()
            return JsonResponse({"message":"SUCCESS"}, status =200)
            
        except IntegrityError:
            return JsonResponse(
					{"message":"Data_Already_Exists"},
					status = 409
				)    
        except KeyError:
            return JsonResponse({'message':"INVALID_KEYS"},status=400) 

    # def get(self, request):
    #     account = Account.objects.values()
    #     return JsonResponse({"data":list(account)}, stauts = 200) 

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if '@' not in data['email']:
                return JsonResponse(
					{"message":"Email_Not_Verified"},
					status = 404
                )
            elif len(data['email']) < 3:
                return JsonResponse(
                    {"message":"Email_length_short"}
                )
          
            elif len(data['password']) < 5:
                return JsonResponse(
					{"message":"Password_Not_Verified"},
					status = 411
                )
            if Account.objects.filter(email = data['email']).exists() :
                account = Account.objects.get(email = data['email'])
                
                if bcrypt.checkpw(data['password'].encode('utf-8'), account.password.encode('utf-8')):
                    access_token = jwt.encode({'email' : account.email}, 'secret', algorithm = 'HS256')
                    return JsonResponse({"Authorization" : access_token.decode('utf-8')}, status=200)
                return JsonResponse ({"message":"UNAUTHORIZED"},status=401) # password 에러
            return JsonResponse ({"message":"UNAUTHORIZED"},status=401)  # email 에러
       
        except KeyError:
            return JsonResponse({'message' : "INVALID_KEYS"}, status = 400)          
