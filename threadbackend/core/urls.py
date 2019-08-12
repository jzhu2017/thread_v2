from django.conf.urls import url, include, re_path
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views
#from filebrowser.sites import site

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

#django 2.2 ver path('articles/<int:year>/', views.year_archive)
#path('index/', views.index, name='main-view'),

urlpatterns = [

    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<email>\w)/$', views.index, name='index'),

    re_path(r'^articles/$', views.articles, name='articles'),
    re_path(r'^articles/(?P<tag>\w)/$', views.articles, name='articles'),

    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^about/(?P<email>\w)/$', views.about, name='about'),

    re_path(r'^issues/$', views.issues, name='issues'),
    re_path(r'^issues/(?P<issue_term>\w)/$', views.issues, name='issues'),
    # url(r'^article/(?P<article_id>\w)/$', views.article, name='article'),
    re_path(r'^admin/', admin.site.urls),
    path(r'tinymce/', include('tinymce.urls')),
    path(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    #re_path(r'^admin/', include(admin.site.urls)),
    #re_path(r'^admin/filebrowser/', include('site.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
