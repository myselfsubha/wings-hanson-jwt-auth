from django.urls import path
from .views import (WatchListView, WatchListDetailView, StreamListView,
                     StreamDetailView,ReviewListView, ReviewDetailView, ReviewCreate)

urlpatterns = [
    path('',WatchListView.as_view(),name='watchlist_view'),
    path('<int:pk>/',WatchListDetailView.as_view(),name='watch_detail_view'),
    path('<int:pk>/review/',ReviewListView.as_view(),name='Review_List'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='Review_Create'),
    path('review/<int:pk>/',ReviewDetailView.as_view(),name='Review_Detail'),
    path('stream/',StreamListView.as_view(),name='streamlist_view'),
    path('stream/<int:pk>',StreamDetailView.as_view(),name='stream_detail_view'),
    
]