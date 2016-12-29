from django.conf.urls import include, url, patterns
import django.contrib.auth.views as auth_views 
import ksda.views as views

urlpatterns = patterns(
    #url(r'^$', views.profilePage), #this regex sucks
    url(r'^login$', auth_views.login, {'template_name': 'ksda/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', views.confirm_registration, name='confirm'),
    url(r'^profile$', views.profilePage, name='profile'),

    url(r'^profile/(?P<observedUserName>\w+)/$', views.profilePageObserved, name='profilePageObserved'),
    url(r'^changePassword$', views.changePassword, name='changePassword'),
    url(r'^updateProfileStandard$', views.updateProfileStandard, name='updateProfileStandard'),
    url(r'^updateProfileAdvanced$', views.updateProfileAdvanced, name='updateProfileAdvanced'),


    url(r'^worksessions$', views.worksessionsPage, name='worksessions'),
    url(r'^newWorksession$', views.addWorksession, name='newWorksession'),
    url(r'^newWorksessionTask$', views.addWorksessionTask, name='newWorksessionTask'),
    url(r'^newWorkunit$', views.addWorkunit, name='newWorkunit'),
    url(r'^toggleWorksessionComplete$', views.toggleWorksessionComplete, name='toggleWorksessionComplete'),
    url(r'^deleteWorksession$', views.deleteWorksession, name='deleteWorksession'),
    url(r'^deleteWorksessionTask$', views.deleteWorksessionTask, name='deleteWorksessionTask'),
    url(r'^getWorksessionInfo$', views.getWorksessionInfo, name='getWorksessionInfo'),

    url(r'^waitsessions$', views.waitsessionsPage, name='waitsessions'),
    url(r'^newWaitsession$', views.addWaitsession, name='newWaitsession'),
    url(r'^newWaitunit$', views.addWaitunit, name='newWaitunit'),
    url(r'^toggleWaitsessionComplete$', views.toggleWaitsessionComplete, name='toggleWaitsessionComplete'),
    url(r'^deleteWaitsession$', views.deleteWaitsession, name='deleteWaitsession'),
    url(r'^getWaitsessionInfo$', views.getWaitsessionInfo, name='getWaitsessionInfo'),

    url(r'^finances$', views.financesPage, name='finances'),
    url(r'^newFine$', views.newFine, name='newFine'),
    url(r'^deleteFine$', views.deleteFine, name='deleteFine'),
    url(r'^completeFine$', views.completeFine, name='completeFine'),
    
    url(r'^forum$', views.forumPage, name='forum'),
    url(r'^post/(?P<id>\d+)$', views.post, name = 'post'),
    url(r'^get-comment-html$', views.get_comment_html),
    url(r'^threads/(?P<id>\d+)$', views.threads, name = 'threads'),
    url(r'^thread$', views.threads, name = 'thread'),
    url(r'^new_thread', views.new_thread, name = 'new_thread'),

    url(r'^calendar$', views.calendarPage, name='calendar'),
    
    url(r'^documents$', views.documentsPage, name='documents'),
    url(r'^deleteDocument$', views.deleteDocument, name='deleteDocument'),

    url(r'^brotherRoll$', views.brotherRoll, name='brotherRoll'),
    url(r'^assignRole$', views.assignRole, name='assignRole'),
    url(r'^newRole$', views.newRole, name='newRole'),
    url(r'^deleteRole$', views.deleteRole, name='deleteRole'),

    url(r'^sendEmail$', views.sendEmail, name='sendEmail'))