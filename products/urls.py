from django.urls import path, include


from products.views import ProductListView # ProductDetailView

urlpatterns = [
    path('/micelist', ProductListView.as_view()),
    # path("/detail-product",ProductDetailView.as_view()),
]

#localhost:8000/products/micelist