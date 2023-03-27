from django.contrib import admin
from django.urls import path
from cocktail.views import CocktailList, CocktailDetail
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('cocktails/', CocktailList.as_view(), name='cocktail-list'),
    path('cocktails/<int:pk>', CocktailDetail.as_view(), name='cocktail-detail'),
    path('search/', CocktailList.as_view(), name='cocktail-search'),
    path('admin/', admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]