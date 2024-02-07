from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogs.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog newest site"
    link = "/rss/feed"
    description = "blog test."

    def items(self):
        return Post.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]
