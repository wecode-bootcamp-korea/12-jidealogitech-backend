from django.urls import path, include


from products.views import CategoryView, ProductListView, ProductDetailView

urlpatterns = [
    path('',CategoryView.as_view()),
    path('/mice_list', ProductListView.as_view()),
    path('/product_mice/<int:product_id>',ProductDetailView.as_view()),
]
