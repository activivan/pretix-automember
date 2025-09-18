from django.urls import path

from .views import AutomemberSettingsView

urlpatterns = [
    path(
        'control/organizer/<str:organizer>/automember/',
        AutomemberSettingsView.as_view(),
        name='org_settings'
    ),
]
