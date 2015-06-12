from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin


urlpatterns = patterns(
    '',

    # backoffice
    url(r'^backoffice/', include('backoffice.urls')),

    # django admin
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns += i18n_patterns(
    # frontoffice
    url(r'', include('frontoffice.urls')),
)
