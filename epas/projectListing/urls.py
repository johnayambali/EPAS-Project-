from django.urls import path
from . import views
from users import views as user_views
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostUpdateView2, PostUpdateView3, PostDeleteView, ApplicationCreateView, ApplicationListView, ApplicationDetailView, ApplicationUpdateView, ApplicationDeleteView, UpdateStatusView, UpdateOfferView



urlpatterns = [
    path('', views.home, name='projectListing-home'),
    path('profile/', user_views.profile, name='projectListing-profile'),
    path('approval/', views.homeDirector, name='projectListing-homeDirector'),
    path('myprojects/', views.myprojects, name='projectListing-myprojects'),
    path('applications/', views.applications, name='projectListing-applications'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/assign', PostUpdateView2.as_view(), name='post-assign'),
    path('post/<int:pk>/complete', PostUpdateView3.as_view(), name='post-complete'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/apply', ApplicationCreateView.as_view(), name='application-create'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<int:pk>/update', ApplicationUpdateView.as_view(), name='application-update'),
    path('application/<int:pk>/status', UpdateStatusView.as_view(), name='application-status'),
    path('application/<int:pk>/offer', UpdateOfferView.as_view(), name='application-offer'),
    path('application/<int:pk>/delete', ApplicationDeleteView.as_view(), name='application-delete'),
    path('profprojectapplications/', views.profprojectapplications, name='projectListing-prof_projectapplication'),
    path('profactiveprojects/', views.profmyactiveprojects, name='projectListing-prof_myactiveprojects'),
    
    
]

