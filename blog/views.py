from django.views.generic import DetailView, ListView

from blog.models import Post


class PostList(ListView):
    model = Post
    paginate_by = 3
    context_object_name = "posts"
    template_name = "blog/post_list.html"


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
