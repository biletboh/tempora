import django_filters

from users.models import UserProfile


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = UserProfile
        fields = ['email']
