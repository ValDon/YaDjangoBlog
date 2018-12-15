from django.urls import re_path
from django.views.generic import TemplateView


vueUrlPatterns = [
                  # url for vue page
                  re_path(r'^home/', TemplateView.as_view(template_name="vueindex.html")),
              ]

