from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ZipViewSet, AccessViewSet, PlansViewSet, PaymentViewSet, User_RentalsViewSet, RentalsViewSet, ContentViewSet, TypeViewSet, GenreViewSet, RatingsViewSet, DirectorViewSet, CastViewSet


router = SimpleRouter()

router.register("User", UserViewSet)
router.register("Zip", ZipViewSet)
router.register("Access", AccessViewSet)
router.register("Plans", PlansViewSet)
router.register("Payment", PaymentViewSet)
router.register("User_Rentals", User_RentalsViewSet)
router.register("Rentals", RentalsViewSet)
router.register("Content", ContentViewSet)
router.register("Type", TypeViewSet)
router.register("Genre", GenreViewSet)
router.register("Ratings", RatingsViewSet)
router.register("Director", DirectorViewSet)
router.register("Cast", CastViewSet)

urlpatterns = router.urls
