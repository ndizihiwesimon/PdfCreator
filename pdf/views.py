import pdfkit
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

def generate_prescription_pdf(request):
   # Render the HTML template with the data
   context = {
       'patient_name': 'John Doe',
       'date_of_birth': '01/01/1990',
       'address': '123 Street, City',
       'medications': [
           {'name': 'Medication A', 'dosage': '10mg', 'instructions': 'Take once daily'},
           {'name': 'Medication B', 'dosage': '20mg', 'instructions': 'Take twice daily'}
       ],
       'physician_name': 'Dr. Jane Smith',
       'physician_email': 'jane.smith@example.com',
       'physician_signature': '/path/to/physician_signature.png'
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
   pdf_file = pdfkit.from_string(rendered_html, False, options=options, css=settings.STATIC_ROOT, cover=None, configuration=None, cover_first=False, toc=None, xsl_style_sheet=None, toc_disable_links=False, toc_header_text=None, toc_header_fs=None, toc_header_depth=None, toc_text_size_shrink=None, dump_outline=None, outline=None, outline_depth=None, repeat_table_of_contents=None, include_in_outline=None, disable_external_links=False, disable_internal_links=False, print_media_type=None, dpi=None, image_dpi=None, image_quality=None, no_pdf_compression=False, zoom=None, page_offset=None, copies=None, quiet=False, grayscale=False, lowquality=False, enable_plugins=False, disable_javascript=False, no_background=False, enable_javascript=False, javascript_delay=None, no_images=False, no_hyperlinks=False, background=None, images=None, no_collate=False, disable_smart_shrinking=False, use_xserver=False, enable_smart_shrinking=False, header_html=None, footer_html=None, header_spacing=None, footer_spacing=None, allow=None, web=None, custom_headers=None, custom_options=None, cookie=None, post=None, username=None, password=None, window_status=None, run_script=None, replacements=None, debug_javascript=False, no_print=False, disable_dotted_lines=False, disable_form_fields=False, disable_extern_links=False, disable_intern_links=False, print_media_type=False, disable_local_file_access=False, disable_sandbox=False, remote_js=False, javascript_debug=False, user_style_sheet=None, minimum_font_size=None, no_outline=False, outline_depth=None, dump_default_toc_xsl=None, dump_page=None, dump_links=None, dump_html=None, dump_text=None, dump_images=None, dump_outline=None, disable_slow_scripts=False, debug=False, cover=None, page_size=None, orientation=None, toc=None, use_print_media=False, footer_center=None, footer_font_name=None, footer_font_size=None, footer_html=None, footer_left=None, footer_line=False, footer_right=None, footer_spacing=None, footer_font_name=None, footer_font_size=None, footer_line=False, no_pdf_compression=None, footer_left=None, footer_center=None, footer_right=None, footer_font_name=None, footer_font_size=None)
   # Return the PDF file as a response
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="prescription.pdf"'
   response.write(pdf_file)
   return response
