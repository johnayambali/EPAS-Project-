from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, ApplicationCreateView, ApplicationListView, ApplicationDetailView, ApplicationUpdateView, ApplicationDeleteView, UpdateApprovalView, UpdateStatusView, UpdateOfferView

urlpatterns = [
    path('', PostListView.as_view(), name='projectListing-home'),
    path('profile/', views.profile, name='projectListing-profile'),
    path('approval/', views.homeDirector, name='projectListing-homeDirector'),
    path('myprojects/', views.myprojects, name='projectListing-myprojects'),
    path('applications/', views.applications, name='projectListing-applications'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/apply', ApplicationCreateView.as_view(), name='application-create'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<int:pk>/update', ApplicationUpdateView.as_view(), name='application-update'),
    path('post/<int:pk>/approval', UpdateApprovalView.as_view(), name='post-approval'),
    path('application/<int:pk>/status', UpdateStatusView.as_view(), name='application-status'),
    path('application/<int:pk>/offer', UpdateOfferView.as_view(), name='application-offer'),
    path('application/<int:pk>/delete', ApplicationDeleteView.as_view(), name='application-delete'),
    path('profmyprojects/', views.profmyprojects, name='projectListing-prof_myprojects'),
    path('profprojectapplications/', views.profprojectapplications, name='projectListing-prof_projectapplication'),
    path('profactiveprojects/', views.profmyactiveprojects, name='projectListing-prof_myactiveprojects'),
    path('profprofile/', views.profprofile, name='projectListing-prof_profile'),
    path('profile/',views.createapplication2,name="createapplication2"),
    
    
]

