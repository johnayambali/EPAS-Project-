from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='projectListing-home'),
    path('profile/', views.profile, name='projectListing-profile'),
    path('myprojects/', views.myprojects, name='projectListing-myprojects'),
    path('applications/', views.applications, name='projectListing-applications'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]

