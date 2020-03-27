from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost, BlogCategory
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


def home(request):
    return render(request, "blog/home.html")




class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/bloghome.html"
    context_object_name = "blog_posts"
    ordering = ["-date_posted"]




class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"



class BlogCategoryListView(ListView):
    model = BlogPost
    template_name = "blog/category_posts.html"
    context_object_name = "category_posts"


    def get_queryset(self):
        category = get_object_or_404(BlogCategory, slug=self.kwargs.get("slug"))
        return BlogPost.objects.filter(category_id=category).order_by("-date_posted")
