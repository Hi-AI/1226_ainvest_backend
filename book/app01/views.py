from django.shortcuts import render,redirect,reverse
from django.views import View
from app01 import models
# Create your views here.

class Book(View):
    def get(self,request):
        book_lst = models.Books.objects.all()
        return render(request, 'home.html', {'book_lst': book_lst})

def book_add(request):
    if request.method=='POST':
        bookname = request.POST.get('bookname')
        authorpk_lst = request.POST.getlist('autherpk')
        presspk = request.POST.get('presspk')
        obj =models.Books.objects.create(bname=bookname,pub_id=presspk)
        obj.save()
        obj.author_set.set(authorpk_lst)
        return redirect(reverse('book_home'))
#删除书籍
# def book_del(request):
#     pk = request.GET.get('pk')
#     models.Books.objects.filter(pk=pk).delete()
#     return redirect(reverse('book_home'))