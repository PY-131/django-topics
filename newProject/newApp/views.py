from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Publisher, Book



class Index(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello World")


# make the view closer to the model, but using generic views
class PublisherListView(ListView):
	template_name = "publisher_list.html"
	model = Publisher

class BookDetailView(DetailView):
	template_name = "book_detail.html"
	model = Book


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context