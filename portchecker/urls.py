from django.urls import path
from portchecker.views import HomePageView

app_name = 'portchecker'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # Currently Unused
    path('success/', HomePageView.as_view(), name='success'),
]