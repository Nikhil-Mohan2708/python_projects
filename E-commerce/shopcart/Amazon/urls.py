from django.urls import path
from . import views
app_name='Amazon'

urlpatterns = [
    path('',views.allPodCat,name='allPodCat'),
    path('<slug:c_slug>/',views.allPodCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='proCatdetail')

]
