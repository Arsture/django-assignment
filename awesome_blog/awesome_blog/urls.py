from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('post/', include('post.urls')),
    path('comment/', include('comment.urls')),
    path('tag/', include('tag.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
