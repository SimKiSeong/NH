from django.shortcuts import render

from django.views.generic import ListView, DetailView
from bookmark.models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class BookmarkLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_list.html'
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkDV(DetailView):
   model = Bookmark

class SubGroupLV(ListView):
    model = SubGroup

class SubGroupDV(DetailView):
    model = SubGroup

class SubListLV(ListView):
    model = SubList

class SubListDV(DetailView):
    model = SubGroup




class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'price','owner']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView) :
    model = Bookmark
    fields = ['title', 'price','owner']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(LoginRequiredMixin, DeleteView) :
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')


def my_view(request):
    # View code here...
    return render_to_response('myapp/index.html', {'foo': 'bar'}, context_instance=RequestContext(request))

def my_view(request):
    bookmark = Bookmark.objects.all()

    return render(request, 'bookmark/bookmark_form.html', {
        'bookmark_list': bookmark_list
    })