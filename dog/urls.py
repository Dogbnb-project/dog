from django.conf.urls import url
from dog import views

urlpatterns = [

    # INDEX [HOME]
    url(r'^$', views.index, name='index'),

    # ABOUT US
    url(r'about/$', views.about, name='about'),

    # CONTACT US
    url(r'contact/$', views.contact, name='contact'),
    
    # REGISTER
    #url(r'register/$', views.register, name='register'),

    # LATEST COTTAGES
    url(r'latest-cottages/$', views.latestcottages, name='latestcottages'), 

    # LOGOUT
    #url(r'^logout/$', views.user_logout, name='logout'),

    # SEARCH RESULTS
    url(r'^search-results/$', views.search_results, name='searchresults'),

    ########################################################################
    # HOST SPECIFIC
    ########################################################################

    # HOST - ADD COTTAGE
    url(r'^host-add-cottage/$', views.add_cottage, name='addcottage'),

    # HOST - EDIT COTTAGE
    url(r'^host-edit-cottage/$', views.edit_cottage, name='editcottage'),

    # HOST - SHOW BOOKINGS
    url(r'^host-show-bookings/$', views.show_bookings, name='showbookings'),

    ########################################################################
    # ADMIN SPECIFIC
    ########################################################################

    # ADMIN - REPORTS
    url(r'^admin-reports/$', views.admin_reports, name='adminreports'),

    ########################################################################
    # COTTAGE SPECIFIC
    ########################################################################
    #url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    
    # RANGO VIEWS FOR REFERENCE

    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='show_category'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',views.add_page,name='add_page'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^restricted/', views.restricted, name='restricted'),
]
