from django.urls import path
from snippets import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('snippets/<int:pk>', views.snippet_detail),
    path('snippets/', views.snippet_list)
]
