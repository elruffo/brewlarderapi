from django.conf.urls import patterns


urlpatterns = patterns(
    'frontoffice.views',

    # Home
    (r'^[/]?$', 'home', {'template_name': 'frontoffice/home.html'}, 'frontoffice_home'),

    # API
    (r'^search_beer[/]?$', 'search_beer', {}, 'search_beer'),

)
