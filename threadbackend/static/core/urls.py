from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<email>\w)/$', views.index, name='index'),

    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles/(?P<tag>\w)/$', views.articles, name='articles'),

    url(r'^about/$', views.about, name='about'),
    url(r'^about/(?P<email>\w)/$', views.about, name='about'),

    url(r'^issues/$', views.issues, name='issues'),
    url(r'^issues/(?P<issue_term>\w)/$', views.issues, name='issues'),
    # url(r'^article/(?P<article_id>\w)/$', views.article, name='article'),
    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
