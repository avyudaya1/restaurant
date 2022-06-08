from rest_framework.routers import DefaultRouter
from main.views import ItemCategoryViewSet, ItemViewSet, MenuItemCategoryViewSet, MenuItemViewSet, StoreViewSet

router = DefaultRouter()

router.register("items", ItemViewSet)
router.register("menuitems", MenuItemViewSet)
router.register("itemcategories", ItemCategoryViewSet)
router.register("menuitemcategories", MenuItemCategoryViewSet)
router.register("store", StoreViewSet)

app_name = "api"
urlpatterns = router.urls