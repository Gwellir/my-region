from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import rest_framework.authtoken.views as token_views

import mainsite.views as main_views
import travelapp.views as travel_views
import socialapp.views as social_views
import ordersapp.views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main, name='main'),
    path('travel/', include('travelapp.urls', namespace='travel')),
    path('user/', include('userapp.urls', namespace='user')),
    path('orders/', include('ordersapp.urls', namespace='orders')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('social/', include('socialapp.urls', namespace='social')),
]

urlpatterns += [
    path('djrichtextfield/', include('djrichtextfield.urls')),
]

router = DefaultRouter()
router.register('routes', travel_views.RouteViewSet)
router.register('trips', travel_views.TripViewSet)
router.register('comments', social_views.TripCommentViewSet)
router.register('orders', order_views.OrderViewSet)

urlpatterns += [
    path('api/', include(router.urls))
]

urlpatterns += [
    path('api-token-auth/', token_views.obtain_auth_token),
]
