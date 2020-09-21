import json 

from django.views import View
from django.http import JsonResponse, HttpResponse

# from django.core.exceptions import ObjectDoesNotExist

from products.models import Main_category, Category, Product, Color, Thumbnail


class ProductListView(View):
    def get(self,request):
        # thumbnail = Thumbnail.objects.values('thumbnail_url')
        # specified_products = list(Product.objects.values('product_title','product_details','product_price','thumbnail'))
        
        
        # return JsonResponse({'data':specified_products}, status = 200)

        try: 
            # requested_product  = request.GET.get('category')
            specified_products = Product.objects.all()
            product_list =[]
            for specified_product in specified_products:
                product_list.append(
                    {
                        'product_title'   : specified_product.product_title,
                        'product_details' : specified_product.product_details,
                        'product_price'   : specified_product.product_price, 
                        'thumbnail_url'   : specified_product.thumbnail_set.first().thumbnail_url            
                    }
                )

            return JsonResponse({"mice_list": product_list}, status = 200) 
         
        except ValueError:
            return JsonResponse({"message": 'INVALID_CATEGORY'}, status = 400)



# class ProductDetailView(View):
#     def get(self,request, product_id):
#         try: 
#             requested_product = product_title 
            

#             return JsonResponse({"mice_data": })
#         except ObjectsDoesNotExist:
#             return JsonResponse({"message": 'INVALID_PRODUCT'}, status =400)
