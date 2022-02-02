from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "cbv/",
        views.IndexClassView.as_view(template_name="cbv_index.html"),
        name="index_cbv",
    ),
    path(
        "cbv2/",
        views.IndexClassView.as_view(template_name="cbv_index2.html"),
        name="index_cbv2",
    ),
    path("admin/", admin.site.urls),
]
