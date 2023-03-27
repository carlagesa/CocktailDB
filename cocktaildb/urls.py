from django.contrib import admin
from django.urls import path
from cocktail.views import CocktailList, CocktailDetail
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="CocktailDB Swagger API Documentation",
#         default_version='v1',
#         description="Test Swagger CocktailDB",
#         terms_of_service="https://www.ourapp.com/policies/terms/",
#         contact=openapi.Contact(email="carltonagesa@gmail.com"),
#         license=openapi.License(name="Test License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
urlpatterns = [
    path('cocktails/', CocktailList.as_view(), name='cocktail-list'),
    path('cocktails/<int:pk>', CocktailDetail.as_view(), name='cocktail-detail'),
    path('search/', CocktailList.as_view(), name='cocktail-search'),
    path('admin/', admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
    # path('', schema_view.with_ui('swagger', cache_timeout=0),
    #      name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc',
    #      cache_timeout=0), name='schema-redoc'),
]