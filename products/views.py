import json 

from django.views import View
from django.http import JsonResponse, HttpResponse

from django.core.exceptions import ObjectDoesNotExist

from products.models import Main_category, Category, Product, Color, Thumbnail

class CategoryView(View):
    def get(self,request):
        try: 
            target_categories = Category.objects.all()
            subcategory = []
            for category in target_categories: 
                subcategory.append(
                    {
                      
                      'id'   : category.id,
                      'category' : category.name
                    #   'main_category': category.Category.objects.prefetch_
                    }
                )
            return JsonResponse({"category_list":subcategory}, status = 200)    

        except ValueError:
            return JsonResponse({"category":'INVALID_CATEGORY'},status = 400)    


class ProductListView(View):
    def get(self,request):
        try: 
            specified_products = Product.objects.all()
            product_list =[]
            for specified_product in specified_products:
                product_list.append(
                    {
                        'product_id'      : specified_product.product_id,
                        'product_title'   : specified_product.product_title,
                        'product_details' : specified_product.product_details,
                        'product_price'   : specified_product.product_price, 
                        'thumbnail_url'   : specified_product.thumbnail_set.first().thumbnail_url            
                    }
                )

            return JsonResponse({"mice_list":product_list}, status = 200) 
         
        except ValueError:
            return JsonResponse({"message":'INVALID_LIST'}, status = 400)

class ProductDetailView(View):
    def get(self,request,product_id):
        try: 
            
            target_product = Product.objects.get(id=product_id)
            category = Category.objects.get(id = target_product.category_id)
            mice_product={
                    'id'                   : target_product.id,
                  # 'product_banner'       : target_product.product_banner,
                    'product_teaser'       : target_product.product_teaser,      
                  # 'product_key_feature'  : target_product.product_key_feature,
                    'product_title'        : target_product.product_title,
                    'product_details'      : target_product.product_details,
                    'product_price'        : target_product.product_price,
                    'product_note'         : target_product.product_note,
                  # 'additional_feature'   : target_product.additional_feature,
                  # 'specs_details'        : target_product.specs_details,
                    'recommended_products' : target_product.recommended_products,
                    'thumnbnail_url'       : target_product.thumbnail_set.first().thumbnail_url,
                    'category'             : category.name
                }
                                  

            return JsonResponse({"mice_data":mice_product}, status = 200)

        except ObjectDoesNotExist:
            return JsonResponse({"message":'INVALID_PRODUCT'}, status =400)

