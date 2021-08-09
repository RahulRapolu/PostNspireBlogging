from django.urls import path, include
from .views import BlogPostListView, BlogPostDetailView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BlogPostListView.as_view(), name='index'),
    path('blog/new/', views.createBlog , name = 'blog-create'),
    path('blog/<int:pk>/', BlogPostDetailView.as_view(), name = 'blog-detail'),
    path('blog/<int:pk>/edit/', views.editBlog, name = 'blog-edit'),
    path('blog/<int:pk>/del/', views.deleteBlog, name = 'blog-delete'),
    path('like/<int:pk>/', views.likePost, name='like-post-home'),
    path('blog/<int:pk>/like/', views.likePost, name='like-post'),
    path('blog/<int:pk>/new-comment/', views.addComment,name='add-comment'),
    path('blog/<int:cid>/<int:pk>/delete-comment/', views.delComment,name='delete-comment')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)