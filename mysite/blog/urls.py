from django.urls import path

urlpatterns = [
    path('', views.PostViews.as_view(), name='home')
]