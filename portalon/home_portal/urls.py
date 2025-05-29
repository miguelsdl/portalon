from django.urls import path
from home_portal.views.home_page_view import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]