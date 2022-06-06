from rest_framework.routers import DefaultRouter
from main.views import ItemViewSet

router = DefaultRouter()

router.register("items", ItemViewSet)

app_name = "api"
urlpatterns = router.urls