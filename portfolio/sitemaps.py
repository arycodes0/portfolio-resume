from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    priority = 0.8
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # Return current time as last modification date
        return timezone.now()


class PortfolioSitemap(Sitemap):
    """Main sitemap for the portfolio"""
    priority = 1.0
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        # Return the main pages of your portfolio
        return [
            'home',
        ]

    def location(self, item):
        if item == 'home':
            return '/'
        return reverse(item)

    def lastmod(self, item):
        return timezone.now()
