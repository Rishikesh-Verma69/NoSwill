from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView, MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/singup/', CreateUserView.as_view(), name='signup'),
    path("api/login/", MyObtainTokenPairView.as_view(), name="get_token"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path('api/', include("api.urls")),
]

