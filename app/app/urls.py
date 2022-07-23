from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users.views import GetUserView,Signup,UserActivation,OTP,UserVerification,CheckEmail,Rate
from rest_framework import permissions
from listing.views import GetListingByUser,ListingGetall,Pusher
from reference.views import ReferenceGetall
from transactions.views import GetSales
from channel.views import ChannelSend
from chat.views import ChatGet
from comments.views import CommentsGetall
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/signup/', Signup.as_view(), name='Sign up'),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/activity/', include('activity.urls')),
    path('api/v1/listing/', include('listing.urls')),
    path('api/v1/bid/', include('bid.urls')),
    path('api/v1/transactions/', include('transactions.urls')),
    path('api/v1/users/details/', GetUserView.as_view(), name='get_user'),
    path('api/v1/reference/', include('reference.urls')),
    path('api/v1/swap/', include('swap.urls')),
    path('api/v1/sold/', include('sold.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/reports/', include('reports.urls')),
    path('api/v1/channel/', include('channel.urls')),
    path('api/v1/chat/', include('chat.urls')),
    path('api/v1/getsales/', GetSales.as_view(), name='get_user'),
    path('api/v1/listingbyuser/', GetListingByUser.as_view(), name='get_user'),
    path('api/v1/pusher/', Pusher.as_view(), name='get_user'),
    path('api/v1/listingGetall/', ListingGetall.as_view(), name='get_user'),
    path('api/v1/referencegetall/', ReferenceGetall.as_view(), name='get_user'),
    path('api/v1/sendMessage/', ChannelSend.as_view(), name='get_user'),
    path('api/v1/rate/', Rate.as_view(), name='get_user'),
    
    path('api/v1/commentsgetall/', CommentsGetall.as_view(), name='get_user'),
    path('api/v1/otp/', OTP.as_view(), name='get_user'),
    path('api/v1/chatgetall/', ChatGet.as_view(), name='get_user'),
    path('api/v1/verification/<str:email>/', UserVerification.as_view(), name='get_user'),
    path('api/v1/checkemail/', CheckEmail.as_view(), name='get_user'),
    path('api/v1/activation/users/', UserActivation.as_view(), name='get_user'),
    
]