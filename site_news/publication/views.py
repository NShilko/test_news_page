from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class NewsList(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-date')
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now().strftime("%d.%m.%Y %H:%M")
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'publ.html'
    context_object_name = 'publ'
