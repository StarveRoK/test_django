from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Indicator, Header, Line, Organization, User
from .serializers import IndicatorSerializer, HeaderSerializer, LineSerializer
import xlsxwriter
from django.http import HttpResponse


class IndicatorListView(APIView):

    def get(self, request):
        indicators = Indicator.objects.all()
        serializer = IndicatorSerializer(indicators, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IndicatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeaderListView(APIView):

    def get(self, request):
        headers = Header.objects.all()
        serializer = HeaderSerializer(headers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LineListView(APIView):

    def get(self, request):
        line = Line.objects.all()
        serializer = LineSerializer(line, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExportReportView(APIView):
    def get(self, request):

        if not request.GET.get('from_month', '') or not request.GET.get('to_month', ''):
            return

        from_month = int(request.GET.get('from_month', ''))
        to_month = int(request.GET.get('to_month', ''))
        lines = Line.objects.filter(last_updated__month__range=(from_month, to_month))

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'

        workbook = xlsxwriter.Workbook(response)
        worksheet = workbook.add_worksheet('Indicators')

        data = {
            'org': 'Итого',
            'summ': 0,
        }

        for line in lines:
            code = line.indicator.article_code

            if code in data:
                data[code] = [
                    line.indicator.article_name,
                    data[code][1] + int(line.distribution_count) + int(line.targeted_distribution_count),
                    data[code][2] + line.targeted_distribution_count,
                    data[code][3] + line.distribution_count,
                ]

            else:
                data[code] = [
                    line.indicator.article_name,
                    int(line.distribution_count) + int(line.targeted_distribution_count),
                    line.targeted_distribution_count,
                    line.distribution_count,
                ]

            data['summ'] = data['summ'] + int(line.distribution_count) + int(line.targeted_distribution_count)

        worksheet.merge_range('A1:A3', 'Наименование организации')
        worksheet.merge_range('B1:B3', 'Общая численность молодых специалистов')
        worksheet.write_row(3, 0, [data.pop('org'), data.pop('summ')])

        index = 2
        for d in data:
            add_info_into_wb(worksheet, data[d], index)
            index += 3

        workbook.close()
        return response


def home(request):
    return render(request, 'report_form.html')


def add_info_into_wb(worksheet, data_list, index):
    worksheet.merge_range(0, index, 0, (index + 2), data_list[0])
    worksheet.merge_range(1, index, 2, index, 'Всего')
    worksheet.merge_range(1, (index + 1), 1, (index + 2), 'Категория, источник приема на работу')
    worksheet.write_row(2, index + 1, ['Целевое', 'Распределение'])
    worksheet.write_row(3, index, [data_list[1], data_list[2], data_list[3]])

