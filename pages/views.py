from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Wiget 1", "Wiget 2", "Wiget 3"],
        "greeting": "THank you FOR visitING",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-11-22-11"
        return context