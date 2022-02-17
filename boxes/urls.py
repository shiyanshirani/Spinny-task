# Django imports
from django.urls import path

# Project imports
from boxes.views import BoxDetailAPI, BoxListAPI, BoxAddAPI, BoxDetailAPI

urlpatterns = [
    path("list", BoxListAPI.as_view(), name="Box LIST API"),
    path("create", BoxAddAPI.as_view(), name="Box CREATE API"),
    path("users_box", BoxDetailAPI.as_view(), name="User's Box LIST API"),
    path("<int:pk>", BoxDetailAPI.as_view(), name="Box DELETE/UPDATE API"),
]
