from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('meetjoin',meetjoin,name='meetjoin'),
    path('video',video,name='video'),
    path('haqqinda',about,name='about'),
    path('foto',foto,name='foto'),
    path('xeberler',blog,name='blog'),
    path('meqale',article,name='article'),
    path('xeber/<slug>',blogsingle,name='blogsingle'),
    path('meqale/<slug>',articlesingle,name='articlesingle'),
]
urlpatterns += [

    path('video/<str:lang_code>/', video, name='video_lang'),
    # Add other language-specific URLs as needed
]