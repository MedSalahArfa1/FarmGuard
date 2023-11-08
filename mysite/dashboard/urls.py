from django.urls import path
from . import views

urlpatterns=[
	path("", views.main_view, name="main_page"),
    path("polygon/", views.add_polygon, name="polygon_page"),
    path("marker/",views.add_marker, name="marker_page"),
    path("dashboard/",views.dash_view,name="dashboard_page"),
    #######
    path('api/fetch_markers/', views.fetch_markers, name='fetch_markers'),
    path('api/fetch_polygons/', views.fetch_polygons, name='fetch_polygons'),
    path('api/fetch_user_data/', views.fetch_user_data, name='fetch_user_data'),
]

