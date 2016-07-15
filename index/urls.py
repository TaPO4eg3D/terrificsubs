from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import(
	posts_home,
	post_detail,
	schedule,
	curseason,
	all_anime,
	)

urlpatterns = [
    url(r'^$', posts_home),
    url(r'^anime/(?P<id>\d+)$', post_detail, name = 'detail'),
    url(r'^schedule/$', schedule, name = 'schedule'),
    url(r'^season/$', curseason, name = 'curseason'),
    url(r'^all_anime/$', all_anime, name = 'all_anime'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
