from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from blog.forms import CommentForm, EmailPostForm
from blog.models import Post
from mysite.settings import EMAIL_HOST_USER


class PostList(ListView):
    model = Post
    queryset = Post.published.all()
    paginate_by = 3
    context_object_name = "posts"
    template_name = "blog/post_list.html"

    def post_taglist(request, tag_slug=None):
        query = request.GET.get("query")
        if query:
            object_list = Post.objects.filter(
                    Q(title__icontains=query) |
                    Q(body__icontains=query)
            ).order_by("title")
        else:
            object_list = Post.published.all()

        tag = None

        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            object_list = object_list.filter(tags__in=[tag])

        paginator = Paginator(object_list, 3)
        page = request.GET.get("page")

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request,
                      "blog/post_list.html",
                      {"page": page,
                       "posts": posts,
                       "tag": tag})


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def post_share(request, slug):
        post = get_object_or_404(Post, slug=slug, status="published")
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

    def post_comment(request, slug):
        post = get_object_or_404(Post, slug=slug, status="published")
        new_comment = None
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = post
                new_comment.save()
        else:
            form = CommentForm()

        return render(request,
                      "blog/comment.html",
                      {"post": post,
                       "new_comment": new_comment,
                       "form": form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "slug" in self.kwargs:
            slug = self.kwargs["slug"]
            post = get_object_or_404(Post, slug=slug, status="published")
            post_tags_ids = post.tags.values_list("id", flat=True)
            similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                          .exclude(slug=slug)
            similar_posts = similar_posts.annotate(same_tags=Count("tags"))\
                                         .order_by("-same_tags",
                                                   "-publish")[:4]
            context["similar_posts"] = similar_posts
        return context
