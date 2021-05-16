from django.urls import path

from blog.views import PostDetail, PostList

app_name = "blog"


urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<slug:slug>", PostDetail.as_view(), name="post_detail"),
    path("<int:post_id>/share/", PostDetail.post_share, name="post_share"),
    path("<slug:slug>/comment/",
         PostDetail.post_comment,
         name="post_comment"),
]
