
from django.urls import path
from home.views import index , contact,dynamic_route,about, search_page,thank_you


urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('about/', about),
    path('search_page/', search_page),
    path('thank-you/', thank_you),
    path('dynamic_route/<number>/' , dynamic_route)
   
]
