from django.http import HttpResponse
from django.utils import feedgenerator
from models import Article

def index(request):
    # articles = Article.objects.all()
    context = {}
    feed = feedgenerator.Rss201rev2Feed(
        title = u"Pat's feed",
        link = u"http://myfeed.patmaddox.com",
        description = u"My super awesome custom feed",
        language = u"en",
    )

    for article in Article.objects.all():
        feed.add_item(
            title=article.title,
            link=article.url,
            description=article.text
        )

    return HttpResponse(feed.writeString('utf-8'))

def add(request):
    url = request.POST['url']
    if url:
        a = Article(url=url)
        a.save()
        a.fetch()
    return HttpResponse('OK')
