from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from mysite.settings import EMAIL_HOST_USER

from blog.forms import EmailPostForm
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

    def post_share(request, post_id):
        post = get_object_or_404(Post, id=post_id, status="published")
        sent = False
        if request.method == "POST":
            form = EmailPostForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                post_url = request.build_absolute_uri(
                    post.get_absolute_url())
                subject = f"{cd['name']} recommends you read {post.title}"
                message = f"Read {post.title} at {post_url}\n\n" \
                          f"{cd['name']}\'s comments: {cd['comments']}"
                send_mail(subject, message, EMAIL_HOST_USER, [cd["to"]])
                sent = True
        else:
            form = EmailPostForm()
        return render(request,
                      "blog/share.html",
                      {"post": post, "form": form, "sent": sent})
