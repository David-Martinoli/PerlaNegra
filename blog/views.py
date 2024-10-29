from django.shortcuts import render
from django.views import View

# Create your views here.
class blogListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'blog/post_list.html', context)