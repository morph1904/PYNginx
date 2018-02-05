from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "dashboard/home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"
