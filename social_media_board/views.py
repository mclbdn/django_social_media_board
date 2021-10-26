from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.
class PostsListView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'home.html'
    fields = ['body']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)