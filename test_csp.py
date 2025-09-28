#!/usr/bin/env python3
"""
Test script to verify CSP headers are being set correctly
"""
import os
import sys
import django
from django.conf import settings
from django.test import RequestFactory
from django.http import HttpResponse

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from portfolio.views import home

def test_csp_headers():
    """Test that CSP headers are being set"""
    factory = RequestFactory()
    request = factory.get('/', HTTP_HOST='localhost')
    
    # Get the response
    response = home(request)
    
    # Check for CSP headers
    csp_headers = []
    for header_name, header_value in response.items():
        if 'content-security-policy' in header_name.lower():
            csp_headers.append(f"{header_name}: {header_value}")
    
    print("CSP Headers found:")
    if csp_headers:
        for header in csp_headers:
            print(f"  {header}")
    else:
        print("  No CSP headers found!")
    
    # Print all security headers
    print("\nAll security-related headers:")
    security_headers = ['content-security-policy', 'x-frame-options', 'x-content-type-options', 'referrer-policy']
    for header_name, header_value in response.items():
        if any(sec_header in header_name.lower() for sec_header in security_headers):
            print(f"  {header_name}: {header_value}")

if __name__ == "__main__":
    test_csp_headers()
