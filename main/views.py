import openpyxl
from django.http import HttpResponse
from openpyxl.styles import Alignment, Side, Border, Font
from openpyxl.workbook import Workbook
from rest_framework import generics
from .models import CourseRegistration, Course
from .serializers import CourseRegistrationSerializer, CourseListSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = []


class CourseRegistrationCreateView(generics.CreateAPIView):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    permission_classes = []


class CourseRegistrationListView(generics.ListAPIView):
    queryset = CourseRegistration.objects.all().order_by('-created_at')
    serializer_class = CourseRegistrationSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        if request.query_params.get('export') == 'excel':
            return self.export_to_excel()
        return super().list(request, *args, **kwargs)

    def export_to_excel(self):
        registrations = self.get_queryset().select_related('course')

        wb = Workbook()
        ws = wb.active
        ws.title = "Registrations"

        header_font = Font(bold=True)
        center_alignment = Alignment(horizontal='center', vertical='center')
        thin_border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )

        headers = ["Full Name", "Email", "Course", "Notes", "Created At"]
        ws.append(headers)
        for col_num, column_title in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col_num)
            cell.font = header_font
            cell.alignment = center_alignment
            cell.border = thin_border
            ws.column_dimensions[cell.column_letter].width = 20

        for row_num, reg in enumerate(registrations, start=2):
            row = [
                reg.full_name,
                reg.email,
                reg.course.name,
                reg.notes or "",
                reg.created_at.strftime('%Y-%m-%d %H:%M'),
            ]
            for col_num, value in enumerate(row, 1):
                cell = ws.cell(row=row_num, column=col_num, value=value)
                cell.alignment = Alignment(vertical='top')
                cell.border = thin_border

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=course_registrations.xlsx'
        wb.save(response)
        return response
