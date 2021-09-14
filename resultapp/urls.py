
from django.urls import path, re_path
from resultapp.views import (dashboard, pages )

urlpatterns = [

    # The home page
    path('', dashboard, name='dashboard'),

    # Matches any html file
    #re_path(r'^.*\.*', pages, name='pages'),
    path('home/', pages, name='pages')

]