from django.urls import path
from .views import IndexView, DetailView, FakeGenView


urlpatterns = [
    # path('fakerfaker/', FakeGenView.as_view(), name='cms_fake'),
    path('<article_id>/', DetailView.as_view(), name='cms_detail'),
    path('', IndexView.as_view(), name='cms_index'),
]