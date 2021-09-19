from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def studPaginationView(request):
    studs = Student.objects.all()
    p = Paginator(studs,3)
    page_num = request.GET.get('page',1)  # page_num = 1
    print(page_num)
    print('Number of pages: ')
    print(p.num_pages)
    try:
        page_data = p.page(page_num)  # page = p.page(1) -->this returns page 1 of
        print(page_data)
    except EmptyPage:
        page = p.page(1)

    return render(request,'App1/showstuds.html',{'page_data':page_data})



#class based generic view pagination
from django.views.generic.list import ListView

class StudPaginationGeneric(ListView):
    model = Student
    paginate_by=3