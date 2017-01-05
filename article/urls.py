from django.conf.urls import url
from django.conf.urls.static import static

from article import views

from MySite import settings
from article.views import main, rus, eng, rus1, rus2, eng2, eng1, rus3, eng3, rus4, eng4, rus5, eng5

urlpatterns = [
                  url(r'^$', main, name='main'),
                  url(r'^rus/', rus, name='rus'),
                  url(r'^eng/', eng, name='eng'),
                  url(r'^rus1/', rus1, name='rus1'),
                  url(r'^eng1/', eng1, name='eng1'),
                  url(r'^rus2/', rus2, name='rus2'),
                  url(r'^eng2/', eng2, name='eng2'),
                  url(r'^rus3/', rus3, name='rus3'),
                  url(r'^eng3/', eng3, name='eng3'),
                  url(r'^rus4/', rus4, name='rus4'),
                  url(r'^eng4/', eng4, name='eng4'),
                  url(r'^rus5/', rus5, name='rus5'),
                  url(r'^eng5/', eng5, name='eng5'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
