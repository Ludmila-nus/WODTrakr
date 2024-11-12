from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include("core.urls", namespace="core")),
    path("users/", include("users.urls", namespace="users")),
    path("workouts/", include("workouts.urls", namespace="workouts")),
    path('groups/', include("groups.urls", namespace='groups')),
    path('dictionary/', include('dictionary.urls', namespace='dictionary')),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


