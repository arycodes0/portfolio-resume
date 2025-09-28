"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
import json
from . import views
from .sitemaps import PortfolioSitemap

def csp_report_view(request):
    """Handle CSP violation reports"""
    if request.method == 'POST':
        try:
            report = json.loads(request.body)
            # Log the CSP violation (in production, you'd want to log to a file or database)
            print(f"CSP Violation: {report}")
            return JsonResponse({'status': 'received'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def robots_txt(request):
    """Serve robots.txt file"""
    try:
        robots_path = settings.STATICFILES_DIRS[0] / 'robots.txt'
        with open(robots_path, 'r') as f:
            content = f.read()
        return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')

# Sitemap configuration
sitemaps = {
    'portfolio': PortfolioSitemap,
}

# def serve_from_db(request, name):
#     try:
#         file = DatabaseFile.objects.get(name=name)
#         return HttpResponse(file.content, content_type="application/octet-stream")
#     except DatabaseFile.DoesNotExist:
#         return HttpResponse("Not found", status=404)
        
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('csp-report/', csrf_exempt(csp_report_view), name='csp-report'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path("media/<str:name>", serve_from_db, name="db_media"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])