import pdfkit
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

def generate_prescription_pdf(request):
   # Render the HTML template with the data
   context = {
       'patient_name': 'John Doe',
       'patient_gender': 'Female',
       'date_of_birth': '01/01/1990',
       'address': '123 Street, City',
       'medications': [
           {'name': 'Medication A', 'dosage': '10mg', 'instructions': 'Take once daily'},
           {'name': 'Medication B', 'dosage': '20mg', 'instructions': 'Take twice daily'}
       ],
       'physician_name': 'Dr. Jane Smith',
       'physician_email': 'jane.smith@example.com',
       'physician_signature': 'https://www.freepnglogos.com/uploads/signature-png/antonin-scalia-signature-png-picture-download-22.png',
       'stamp_image': 'https://www.freeiconspng.com/uploads/free-stamp-png-10.jpg'
   }
   html_template = 'prescription.html'
   rendered_html = render_to_string(html_template, context)

   # Generate PDF from the rendered HTML content
   options = {
       'page-size': 'A4',
       'encoding': 'UTF-8',
       'load-error-handling': 'ignore',
       'no-stop-slow-scripts': True,
       'quiet': ''
   }
   base_url = request.build_absolute_uri('/')[:-1]  # Base URL for resolving relative paths
   pdf_file = pdfkit.from_string(rendered_html, False, options=options, css=settings.STATIC_ROOT, cover=None, configuration=None, toc=None, cover_first=False)

   # Return the PDF file as a response
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="prescription.pdf"'
   response.write(pdf_file)
   return response
