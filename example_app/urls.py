from django.urls import path
from .views import IndicatorListView, ExportReportView, home, HeaderListView, LineListView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('indicators/', IndicatorListView.as_view(), name='indicator-list'),
    path('headers/', HeaderListView.as_view(), name='header-list'),
    path('lines/', LineListView.as_view(), name='line-list'),
    path('export-report/', ExportReportView.as_view(), name='export-report'),
    path('', home, name='main_page'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
