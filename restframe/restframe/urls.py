
from django.contrib import admin

from django.urls import path,include
from rest_framework import routers
from restapp. views import Taskviewset,Dueviewset,Completed,CreateUserview
from restapp import views
from django.conf import settings
from django.conf.urls.static import static
# router=DefaultRouter()
router=routers.SimpleRouter()
router.register('task',Taskviewset,basename='task')
router.register('due',Dueviewset,basename='due')
router.register('completed',Completed,basename='completed')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',CreateUserview.as_view(),name='register'),
    path('api_auth',include('rest_framework.urls')),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
