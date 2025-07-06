from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="CocktailDB API",
      default_version='v1',
      description="API for cocktail recipes and ingredients",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cocktails.urls')), # cocktails.urls now contains the token paths
    path("ping/", health_check),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Removed redundant token paths here as they are included via 'cocktails.urls' under /api/
]
