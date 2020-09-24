import json 

from django.views import View
from django.http import JsonResponse, HttpResponse

from django.core.exceptions import ObjectDoesNotExist

from products.models import Main_category, Category, Product, Color, Thumbnail

class CategoryView(View):
   def get(self,request):
        try: 
            target_categories = Category.objects.all()
            main_categories = Main_category.objects.get(id=2)
           
            subcategory = []
            for category in target_categories: 
           
                subcategory.append(
                    {
                      
                      'id'   : category.id,
                      'category' : category.name,
                      'main_category': main_categories.name
                    }
                )
           
            return JsonResponse({"category_list":subcategory}, status = 200)    

        except ValueError:
            return JsonResponse({"category":'INVALID_CATEGORY'},status = 400)    


class ProductListView(View):
   def get(self,request):
        try: 
            sorted_products = request.GET.get('sort') 

            if sorted_products == 'price_low_high':
                specified_products = Product.objects.order_by('product_price')
            
            elif sorted_products == 'price_high_low':
                specified_products = Product.objects.order_by('-product_price') 
            
            else:
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
            return JsonResponse({"mice_list":product_list}, status = 200) 

        except ValueError:
           return JsonResponse({"message":'INVALID_LIST'}, status = 400)


class ProductDetailView(View):
   def get(self,request,product_id):
       try:  
           target_product = Product.objects.filter(id=product_id)
           product_colors = target_product.prefetch_related('color')
           thumbnails = Product.objects.filter(id=product_id)[0].thumbnail_set.values_list('color__color', 'thumbnail_url')
           
           thumbnail_urls ={}          
           for thumbnail in thumbnails:
               if thumbnail_urls.get(thumbnail[0]):
                   thumbnail_urls[thumbnail[0]] = thumbnail_urls[thumbnail[0]] + [thumbnail[1]]
               else :
                   thumbnail_urls[thumbnail[0]] = [thumbnail[1]] 
            
           mice_product={
                   'id'                   : target_product[0].id,
                   'product_title'        : target_product[0].product_title,
                   'product_details'      : target_product[0].product_details,
                   'product_price'        : target_product[0].product_price,
                   'product_note'         : target_product[0].product_note,
                   'color_images'         : list(product_colors[0].color.values().distinct()),
                   'thumbnail_url'        : thumbnail_urls
               }
                                

           return JsonResponse({"mice_data":mice_product}, status = 200)

       except ObjectDoesNotExist:
           return JsonResponse({"message":'INVALID_PRODUCT'}, status =400)

