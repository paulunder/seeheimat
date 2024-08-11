from . import views
from django.urls import path

urlpatterns = [
    path("blog_list", views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='blog_detail'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit,
        name='comment_edit'
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete,
        name='comment_delete'
    ),
]
