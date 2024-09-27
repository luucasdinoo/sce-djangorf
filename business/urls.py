# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('business/', views.BusinessCreateListView.as_view(), name='business-create-list'),
#     path('business/<uuid:pk>/', views.BusinessRetrievelDestroyView.as_view(), name='business-detail-view'),
# ]

from django.urls import path, include
from business import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('business', views.BusinnesViewSet, basename='business')

urlpatterns = [
     path('', include(router.urls)),
 ]
