from django.urls import path
from .views import IndexView, DetailView


urlpatterns = [
    path('', IndexView.as_view(), name='cms_index'),
    path('<article_id>/', DetailView.as_view(), name='cms_detail')
]