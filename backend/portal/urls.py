from rest_framework.routers import DefaultRouter
from portal.views import GalleryVS, PhotoVS, TariffVS

router = DefaultRouter()
router.register('gallery', GalleryVS)
router.register('photo', PhotoVS)
router.register('Tariff', TariffVS)

urlpatterns = router.urls
