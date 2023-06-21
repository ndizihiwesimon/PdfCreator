from django.urls import path
from pdf.views import generate_prescription_pdf

urlpatterns = [
    # Other URL patterns
    path('generate-prescription-pdf/', generate_prescription_pdf, name='generate_prescription_pdf'),
]
