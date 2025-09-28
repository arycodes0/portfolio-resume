from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from project.models import Project, Tech, TechCategory

def home(request):
    data = {
    	"projects" : Project.objects.filter(visible=True).order_by("order"),
    	"technologies" : Tech.objects.filter(visible=True).order_by("order"),
        "tech_categories" : TechCategory.objects.filter(visible=True).order_by("order")
    	}
    # data = {
    #     "projects" : []
    # }
    return render(request,"index.html",data);

def dynamic_css(request):
    """Serve dynamic CSS for tech categories"""
    tech_categories = TechCategory.objects.filter(visible=True).order_by("order")
    
    context = {
        'tech_categories': tech_categories
    }
    
    css_content = render_to_string('dynamic_css.html', context)
    
    response = HttpResponse(css_content, content_type='text/css')
    response['Cache-Control'] = 'public, max-age=3600'  # Cache for 1 hour
    return response
