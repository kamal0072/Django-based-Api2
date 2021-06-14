
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
