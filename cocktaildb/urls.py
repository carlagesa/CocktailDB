from django.contrib import admin
from django.urls import path, include
from cocktail import views
from cocktail.views import CocktailList, CocktailDetail
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from cocktail.views import ImageView

urlpatterns = [
    path('cocktails/', CocktailList.as_view(), name='cocktail-list'),
    path('cocktails/<int:pk>', CocktailDetail.as_view(), name='cocktail-detail'),
    path('search/', CocktailList.as_view(), name='cocktail-search'),
    path('api/images/<path:path>/', ImageView.as_view(), name='image-view'),
    # path('media/<path:path>', views.serve_image, name='serve_image'),
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)