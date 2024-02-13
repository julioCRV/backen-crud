from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tareas import views

router = routers.DefaultRouter()
router.register('tareas/api/v1/', views.TareasVistas, 'tareas')

urlpatterns = router.urls