from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/', views.SnippetList.as_view()),
    url(r'^snippets/<int:pk>/', views.SnippetDetail.as_view()),
    url('users/', views.UserList.as_view()),
    url('users/<int:pk>/', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
