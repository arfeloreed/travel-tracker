from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Note, Trip


# Create your views here.
# view route for home page
class IndexView(TemplateView):
    template_name = "trips/index.html"


# view route for dashboard of all trips
def trip_list(request):
    trips = Trip.objects.filter(owner=request.user)

    return render(
        request,
        "trips/trips-list.html",
        {
            "trips": trips,
        },
    )


# view route for creating a trip
class CreateTripView(CreateView):
    model = Trip
    fields = ["city", "country_code", "start_date", "end_date"]
    success_url = reverse_lazy("trips-list")
    # expects a template name of modelname_form.html
    # in my case it's trip_form.html

    # adding the detail for owner field when the form is saved
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        # owner field = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


# view route for updating a trip
class TripUpdateView(UpdateView):
    model = Trip
    fields = ["city", "country_code", "start_date", "end_date"]
    success_url = reverse_lazy("trips-list")
    # template name is the same as the CreateView
    # there is no need to override the form for the owner field, since the owner is already created and stored


# route for deleting a trip
class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy("trips-list")


# view route for every trip's detail
class TripDetailView(DetailView):
    model = Trip
    # default template name modelname_detail.html
    # trip_detail.html

    # override the context data to access the Note model objects
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # notes = self.object.notes.all()
        notes = context["object"].notes.all()
        # print(f"\n{notes}\n")
        context["notes"] = notes
        return context


# view route for note detail page
class NoteDetailView(DetailView):
    model = Note
    # epexcts a template name of note_detail.html


# view route for all notes page
class NoteListView(ListView):
    model = Note
    # expects a template name of note_list.html

    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset


# view route for creating new notes
class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"
    # expects a template name of note_form.html

    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields["trip"].queryset = trips
        return form


# view route for updating a note
class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy("note-list")
    fields = "__all__"
    # the template is the same as for the createview

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields["trip"].queryset = trips
        return form


# route for deleting a note
class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note-list")
    # template name is note_confirm_delete.html
    # it doesn't require a template. It's optional to create one.
    # It is done by creating a POST request submission using a form in the tempate.
