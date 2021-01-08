from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('snippets/<int:pk>', views.SnippetDetails.as_view(), name='snippet-detail'),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetails.as_view(), name='user-detail'),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/',
         views.SnippetHightlight.as_view(), name='snippet-highlight'),

]
urlpatters = format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
