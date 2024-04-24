from rest_framework import viewsets
from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse
from io import BytesIO

class POCListPDFViewSet(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
#         html_content = """
# <html>
# <head>
#     <style>
#         /* Additional styles can be added here */
#         .page {
#             page-break-before: always;
#             padding: 20px; /* Example padding for better visualization */
#         }
#     </style>
# </head>
# <body>
#     <div class="page">
#         Page 1 content
#     </div>
#     <div class="page">
#         Page 2 content
#     </div>
# </body>
# </html>
# """


        context = {
             'student_name': "Paras Lohia",
             'course_name': "Django Rest Framework",
            'completion_date': "24/04/20204"
        }

        email_html_message = render_to_string('certificate.html', context)

        pdf_buffer = BytesIO()

        try:
            HTML(string=email_html_message).write_pdf(pdf_buffer )
            pdf_buffer.seek(0)  
        except Exception as e:
            print(f'Error: {e}')


        response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=output.pdf'  
        return response