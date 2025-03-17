from django.shortcuts import render
from myapp.models import Blog
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    all_blog = Blog.objects.all().order_by('id')
    pag = Paginator(all_blog, 3, orphans=1)
    page_number = request.GET.get('page')
    print("page_number = ",page_number)
    page_obj = pag.get_page(page_number)
    return render(request, 'myapp/home.html', {'page_obj':page_obj})