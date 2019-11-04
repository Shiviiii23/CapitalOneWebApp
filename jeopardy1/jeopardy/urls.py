from django.urls import path
from jeopardy import views

urlpatterns = [
	# path('search/', SearchResultViews.as_view(), name='search_results'),
	path('', views.search, name='search'),
	#path('value/', views.values, name='results')
	# path('value/', views.values, name='values')
	# path('', HomePageView.as_view(), name='home'),
]
