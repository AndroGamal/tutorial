from xml.etree.ElementInclude import include
from django.db import router
from django.urls import path ,include
from Data import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("datav",views.test_veiwset,basename="")
router.register("show",views.test_veiwset_model,basename="")
urlpatterns = [
    path("regest/",views.test_apiview.as_view()),
    path("login/",views.Api_login.as_view()),
    path("veiw/",include(router.urls)),
]