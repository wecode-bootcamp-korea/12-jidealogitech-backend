# from django.shortcuts import render

# import json
# from django .views import View
# from django.http   import JsonResponse

# from account.models import Account

# class CreateView(View):
#     def post(self,request):
#         data = json.load(request.body)
#         Account(
#             name     = data['name'],
#             email    = data['email'],
#             password = data['password'],
#             language = data['language'],
#             country  = data['country'],
#             birthday = data['birthday'],
#             phone    = data['phone'],
#         )
        
#         if  Account.objects.filter(name = data['name']).exists() == True:
#             return JsonResponse({"message":"이미 존재하는 아이디입니다."},status = 401)

#         else:
#             Account.objects.create(name= data['name'], email = data['email'], password = data['password'], language = data['language'],country=data['country'],
#                                    birthday =data['birthday'],phone=data['phone'])
#             return JsonResponse({"message" : "회원으로 가입되셨습니다."}, status = 200)
                               
#     def get(self,request):
#         account = Account.objects.values()
#         return JsonResponse({"list":list(account)},status=200)

# class LoginView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         Account(
#             name     = data['name'],
#             email    = data['email'],
#             password = data['password']
#         )

#         if Account.objects.filter(nane = data['name'],password = data['password']).exists() == True:
#             return JsonResponse({"message": "로그인에 성공하셨습니다."},status=200)            
#         else:
#             return JsonResponse({"message" : "아이디나 비밀번호가 일치하지 않습니다."}, status = 401)

#     def get(self, request):
#         account = Account.objects.values()
#         return JsonResponse({"list" : list(account)}, status = 200)
