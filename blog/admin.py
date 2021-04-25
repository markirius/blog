from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")
    fieldsets = ((
        None, {
            "fields": ("title", "slug", "body", "publish", "status")
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()
