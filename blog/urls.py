from django.urls import path

from blog.views import PostDetail, PostList

app_name = "blog"


urlpatterns = [
    # path("", PostList.as_view(), name="post_list"),
    path("", PostList.post_taglist, name="post_list"),
    path("tag/<slug:tag_slug>/",
         PostList.post_taglist,
         name="post_list_by_tag"),
    path("<slug:slug>", PostDetail.as_view(), name="post_detail"),
    path("<slug:slug>/share/", PostDetail.post_share, name="post_share"),
    path("<slug:slug>/comment/",
         PostDetail.post_comment,
         name="post_comment"),
    path("search/", PostList.post_search, name="post_search"),
]
