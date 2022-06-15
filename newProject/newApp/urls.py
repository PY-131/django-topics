from django.urls import path
from .views import PublisherListView, BookDetailView, Index

urlpatterns=[
  path('', Index.as_view(), name='index'),
  path('publishers/', PublisherListView.as_view(), name="publishers"),
  path('<slug:slug>/', BookDetailView.as_view(), name='book-detail') 
]