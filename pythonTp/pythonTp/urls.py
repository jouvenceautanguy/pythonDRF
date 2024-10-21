from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quickstart.views import AuthorViewSet, EditorViewSet, BookViewSet, CategoryViewSet, CopyViewSet, LoanViewSet, CommentViewSet, EvaluationViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from quickstart.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('editors', EditorViewSet)
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
router.register('copies', CopyViewSet)
router.register('loans', LoanViewSet)
router.register('comments', CommentViewSet)
router.register('evaluations', EvaluationViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Documentation de l'API pour votre projet",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourdomain.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Endpoints JWT
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoints Swagger et ReDoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
