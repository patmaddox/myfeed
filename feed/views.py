from django.http import HttpResponse
from django.utils import feedgenerator
from models import Article

def index(request):
    context = {}
    feed = feedgenerator.Rss201rev2Feed(
        title = u"Pat's feed",
        link = u"http://myfeed.patmaddox.com",
        description = u"My super awesome custom feed",
        language = u"en",
    )

    for article in Article.ready():
        feed.add_item(
            title=article.title,
            link=article.url,
            description=article.text,
            updateddate=article.fetched_at
        )

    return HttpResponse(feed.writeString('utf-8'))

def add(request):
    response = HttpResponse('OK')
    url = request.POST['url']

    if url:
        Article.fetch(url)

    return response
