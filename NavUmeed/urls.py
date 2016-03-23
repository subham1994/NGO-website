from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^main/', 'umeed.views.home'),
                       url(r'^login/', 'umeed.views.loginRequest'),
                       url(r'^logout/', 'umeed.views.logout'),
                       url(r'^home/', 'umeed.views.profile'),
                       url(r'^signup/', 'umeed.views.signup'),
                       url(r'^getusers/', 'umeed.views.getUsers'),
                       url(r'^posts/(?P<article_id>\d+)/', 'umeed.views.article'),
                       url(r'^members/(?P<member_id>\d+)/', 'umeed.views.memberSection'),
                       url(r'^get_payment_data/', 'umeed.views.getPaymentData'),
                       url(r'^image_gallery/', 'umeed.views.imageGallery'),
                       # Examples:
                       # url(r'^$', 'NavUmeed.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )
