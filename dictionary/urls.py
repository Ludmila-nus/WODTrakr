from django.urls import path
from .views import DictionaryView, TermsDataView

app_name = 'dictionary'  

urlpatterns = [
    path('', DictionaryView.as_view(), name='dictionary'),
    path('terms_data/', TermsDataView.as_view(), name='terms_data'),
]
