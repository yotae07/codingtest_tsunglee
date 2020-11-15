from django.urls                import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views                     import UserView

user_sign = UserView.as_view({
    'get': 'signin',
    'post': 'create'
    })

user_list = UserView.as_view({
    'get': 'retrieve'
    })

urlpatterns = format_suffix_patterns([
    path('/sign', user_sign),
    path('/<int:pk>', user_list)
])
