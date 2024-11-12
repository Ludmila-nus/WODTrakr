from django.views.generic import TemplateView
from .models import Term
from django.http import JsonResponse
from django.views import View
from django.db.models import Count


class DictionaryView(TemplateView):
    template_name = 'dictionary/dictionary.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms'] = Term.objects.all().order_by('category', 'term')
        return context
    

class TermsDataView(View):
    def get(self, request, *args, **kwargs):
       # Filter or collect the data you want to show in the graph
        terms = Term.objects.values('category').annotate(total=Count('category'))

        # Format the data in a dictionary for JSON
        data = {
            'labels': [term['category'] for term in terms],
            'totals': [term['total'] for term in terms]
        }

        return JsonResponse(data)