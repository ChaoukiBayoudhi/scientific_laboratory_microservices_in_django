from rest_framework import routers
from .views import ExprementationViewSet,ResultViewSet
from django.urls import path,include

router=routers.DefaultRouter()
router.register('expr',ExprementationViewSet)
router.register('restlts',ResultViewSet)
urlpatterns=[
    path('',include(router.urls))
]