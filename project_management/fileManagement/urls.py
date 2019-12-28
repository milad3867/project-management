from django.urls import path
from . import views

app_name = 'fileManagement'

urlpatterns = [
    path('doc1/<str:name>/',
         views.download_media_doc1, name='download_media_pdf'),
    path('doc2/<str:name>/',
         views.download_media_doc2, name='download_media_pdf'),
    path('form/<str:name>/',
         views.download_form, name='download_form'),
    path('download/guide/', views.download_guide, name='download_guide'),
    path('upload/<int:pk>/', views.upload_file.as_view(), name='upload'),
    # path('download/pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
    # path('download/docx/<int:pk>/',views.download_docx,name='download_docx'),

]
