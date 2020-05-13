from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import BlogPost, BlogCategory
from project.models import ProjectPost, ProjectCategory
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponse





def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New message from HHK:', message, sender_email, ['hevalhazal@gmail.com'])
            return HttpResponse("Thank you for contacting me!")
    else:
        form = ContactForm()
    return render(request, "blog/contact.html", {"form": form})
    #return render(request, "blog/contact.html", {"title": "Contact"})



class HomePageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = BlogPost.objects.order_by('-date_posted')[:3]
        context['latest_projects'] = ProjectPost.objects.order_by('-date_posted')[:4]
        context['post_categories'] = BlogCategory.objects.all()
        context['project_categories'] = ProjectCategory.objects.all()
        return context



class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/bloghome.html"
    context_object_name = "blog_posts"
    ordering = ["-date_posted"]
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_categories'] = BlogCategory.objects.all()
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = BlogPost.objects.filter(category=self.object.category).order_by('?')[:3]
        return context


class BlogCategoryListView(ListView):
    model = BlogPost
    template_name = "blog/category_posts.html"
    context_object_name = "category_posts"
    paginate_by = 9


    def get_queryset(self):
        category = get_object_or_404(BlogCategory, slug=self.kwargs.get("slug"))
        return BlogPost.objects.filter(category_id=category).order_by("-date_posted")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_categories'] = BlogCategory.objects.all()
        return context
