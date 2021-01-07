from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('snippets/<int:pk>', views.SnippetDetails.as_view()),
    path('snippets/', views.SnippetList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetails.as_view())

]
urlpatters = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
