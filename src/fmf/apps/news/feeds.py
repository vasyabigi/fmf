import datetime
from django.contrib.syndication.views import Feed
from django.utils import feedgenerator

from news.models import News, Event


class LatestNewsFeed(Feed):
    feed_type = feedgenerator.Rss201rev2Feed
    title = "Latest news from fmf.kpi.ua"
    link = "http://fmf.kpi.ua/"
    description = "Site of Faculty of Physics and Mathematics"

    def items(self):
        return News.objects.filter(is_active=True).order_by('position')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.get_absolute_url()


class LatestEventsFeed(Feed):
    feed_type = feedgenerator.Rss201rev2Feed
    title = "Latest news from fmf.kpi.ua"
    link = "http://fmf.kpi.ua/"
    description = "Site of Faculty of Physics and Mathematics"

    def items(self):
        return Event.objects.filter(is_active=True, date_from__gte=datetime.datetime.today()).order_by('date_from')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.get_absolute_url()
