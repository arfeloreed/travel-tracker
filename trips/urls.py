from django.urls import path

from . import views

# urls below
urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("dashboard/", views.trip_list, name="trips-list"),
    path("dashboard/create/trip/", views.CreateTripView.as_view(), name="create-trip"),
    path(
        "dashboard/trip/<int:pk>/", views.TripDetailView.as_view(), name="trip-detail"
    ),
    path(
        "dashboard/trip/<int:pk>/update/",
        views.TripUpdateView.as_view(),
        name="trip-update",
    ),
    path(
        "dashboard/trip/<int:pk>/delete/",
        views.TripDeleteView.as_view(),
        name="trip-delete",
    ),
    path("dashboard/note/create/", views.NoteCreateView.as_view(), name="create-note"),
    path("dashboard/notes/", views.NoteListView.as_view(), name="note-list"),
    path(
        "dashboard/note/<int:pk>/", views.NoteDetailView.as_view(), name="note-detail"
    ),
    path(
        "dashboard/note/<int:pk>/update/",
        views.NoteUpdateView.as_view(),
        name="note-update",
    ),
    path(
        "dashboard/note/<int:pk>/delete/",
        views.NoteDeleteView.as_view(),
        name="note-delete",
    ),
]
