from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.api import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="News Blog Api",
        default_version='v1',
        description="NewsBlogApi",
        contact=openapi.Contact(email="rbkrutoi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('posts/', views.PostListApiView.as_view()),
    path('category/', views.CategoryListApiView.as_view()),
    path('post/<int:pk>/', views.PostDetailAPIView.as_view()),
    path('post/like/<int:pk>/', views.LikePostAPIView.as_view()),
    path('post/create/', views.PostCreateAPIView.as_view()),

    path('docs/', schema_view.with_ui('swagger')),

    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]