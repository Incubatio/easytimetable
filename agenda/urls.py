from django.conf.urls.defaults import *

urlpatterns = patterns('agenda.views.locations',
    (r'^universities/add/$', 'add_university', {}, 'add_university'),
    (r'^universities/$', 'list_universities', {}, 'list_universities'),
    (r'^universities/(?P<university_id>\d+)/delete/$', 
        'delete_university', {}, 'delete_university'),
    (r'^universities/(?P<university_id>\d+)$', 'get_university', {}, 'get_university'),
    (r'^universities/(?P<university_id>\d+)/update/$', 'update_university', {}, 'update_university'),
   
    (r'^campuses/add/$', 'add_campus', {}, 'add_campus'),
    (r'^campuses/$', 'list_campuses', {}, 'list_campuses'),
    (r'^campuses/(?P<campus_id>\d+)$', 'get_campus', {}, 'get_campus'),
    (r'^campuses/(?P<campus_id>\d+)/delete/$', 
        'delete_campus', {}, 'delete_campus'),
    (r'^campuses/(?P<campus_id>\d+)/update/$', 'update_campus', {}, 'update_campus'),

    (r'^places/add/$', 'add_place', {}, 'add_place'),
    (r'^places/$', 'list_places', {}, 'list_places'),
    (r'^places/(?P<place_id>\d+)$', 'get_place', {}, 'get_place'),
    (r'^places/(?P<place_id>\d+)/delete/$',
         'delete_place', {}, 'delete_place'),
    (r'^places/(?P<place_id>\d+)/update/$', 'update_place', {}, 'update_place'),

)

urlpatterns += patterns('agenda.views.pedagogy',
    (r'^cursuses/add/$', 'add_cursus', {}, 'add_cursus'),
    (r'^cursuses/$', 'list_cursuses', {}, 'list_cursuses'),
    (r'^cursuses/(?P<cursus_id>\d+)$', 'get_cursus', {}, 'get_cursus'),
    (r'^cursuses/(?P<cursus_id>\d+)/delete/$',
       'delete_cursus', {}, 'delete_cursus'),

	(r'^studyperiods/add/$', 'add_studyperiod', {}, 'add_studyperiod'),
    (r'^studyperiods/$', 'list_studyperiods', {}, 'list_studyperiods'),
    (r'^studyperiods/(?P<studyperiod_id>\d+)$', 'get_studyperiod', {},
        'get_studyperiod'),
    (r'^studyperiods/(?P<studyperiod_id>\d+)/delete/$',
       'delete_studyperiod', {}, 'delete_studyperiod'),

	(r'^subjects/add/$', 'add_subject', {}, 'add_subject'),
    (r'^subjects/$', 'list_subjects', {}, 'list_subjects'),
    (r'^subjects/(?P<subject_id>\d+)$', 'get_subject', {}, 'get_subject'),
    (r'^subjects/(?P<subject_id>\d+)/delete/$',
       'delete_subject', {}, 'delete_subject'),
	   
	(r'^subjectmodalities/add/$', 'add_subjectmodality', {}, 'add_subjectmodality'),
    (r'^subjectmodalities/$', 'list_subjectmodalities', {}, 'list_subjectmodalities'),
    (r'^subjectmodalities/(?P<subjectmodality_id>\d+)$', 'get_subjectmodality', {}, 'get_subjectmodality'),
    (r'^subjectmodalities/(?P<subjectmodality_id>\d+)/delete/$',
       'delete_subjectmodality', {}, 'delete_subjectmodality'),

    (r'^classes/add/$', 'add_classgroup', {}, 'add_classgroup'),
    (r'^classes/$', 'list_classgroups', {}, 'list_classgroups'),
    (r'^classes/(?P<classgroup_id>\d+)$',
        'get_classgroup', {}, 'get_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/delete/$',
       'delete_classgroup', {}, 'delete_classgroup'),
    (r'^classes/(?P<classgroup_id>\d+)/update/$',
       'update_classgroup', {}, 'update_classgroup'),
)

urlpatterns += patterns('agenda.views.index',
    (r'^$', 'index', {}, 'index'),
)

urlpatterns += patterns('agenda.views.planning',
    (r'^planning/users/me$', 'get_planning', {'what': 'me' }, 
        'get_user_planning'),

    (r'^planning/classes/(?P<classgroup_id>\d+)$', 'get_planning', 
        {'what':'classgroup' }, 'get_class_planning'),

    (r'^planning/campuses/(?P<campus_id>\d+)$', 'get_planning', 
        {'what': 'campus' }, 'get_user_planning'),

    (r'^planning//me$', 'get_planning', {'what': 'me' }, 
        'get_user_planning'),

    (r'^planning/users/me$', 'get_planning', {'what': 'me' }, 
        'get_user_planning'),
)
