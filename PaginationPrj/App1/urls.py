from django.urls import path
from . import views

urlpatterns=[
    path('allstuds/',views.studPaginationView,name='allstuds'),
    path('allstuds1/',views.StudPaginationGeneric.as_view(),name='allstuds1')
]