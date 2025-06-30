from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.your-terms.com/",
        contact=openapi.Contact(email="contact@your-api.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),

    path('api/swagger', schema_view.with_ui('swagger', cache_timeout=0))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
