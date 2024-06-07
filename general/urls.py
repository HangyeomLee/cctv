from django.urls import path, include
from .views import ExternalAPIView, UpdateAreaDetectedPeople, FetchAndSaveImageView
from . import views

app_name = "general"

urlpatterns = [
    path("", views.index_view, name="main_page"),
    path("area/<int:pk>", views.area_view, name="area_page"),
    path("area/<int:pk>/<int:pk2>", views.detail_area_view, name="detail_area_page"),
    path("statistics", views.statistics_view, name="statistics"),
    path('update-cctv-data/', ExternalAPIView.as_view(), name='update_cctv_data'),
    path('update-area-detected-people/<int:area_id>/', UpdateAreaDetectedPeople.as_view(), name='update_area_detected_people'),
    path("test/", views.testing_view, name = "test_page"),
    path('fetch-and-save-image/<int:pk>/', FetchAndSaveImageView.as_view(), name='fetch_and_save_image'),
]
