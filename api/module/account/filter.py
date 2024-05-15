from django_filters import CharFilter
from django_filters import rest_framework as filters

from module.account.models import User

class UserFilter(filters.FilterSet):
    sport = CharFilter(field_name="user_sports__sport")

    class Meta:
        model = User
        exclude = ()
