from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from owner.forms import BookForm,EmployeeForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from owner.models import Books
from customer.decorators import owner_permission_required
from django.utils.decorators import method_decorator

# Create your views here.
# class based views,function based
@method_decorator(owner_permission_required,name='dispatch')
class AddBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'addbook.html'
    success_url = reverse_lazy("booklist")
    # def get(self,request,*args,**kwargs):
    #     form=BookForm()
    #     context={'form':form}
    #     return render(request,'addbook.html',context)
    #
    # def post(self,request,*args,**kwargs):
    #     form=BookForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         # book_name=form.cleaned_data.get('book_name')
    #         # author = form.cleaned_data.get('author')
    #         # price=form.cleaned_data.get('price')
    #         # copies=form.cleaned_data.get('copies')
    #         # qs=Books(book_name=book_name,author=author,price=price,copies=copies)
    #         # qs.save()
    #         print('saved successfully')
    #         return render(request,'addbook.html')
    #     else:
    #         context = {'form': form}
    #         return render(request, 'addbook.html', context)
@method_decorator(owner_permission_required,name='dispatch')
class BookListView(ListView):
    model=Books
    context_object_name='books'
    template_name='booklist.html'
    # def get(self,request,*args,**kwargs):
    #     qs=Books.objects.all()
    #     context={'books':qs}
    #     return render(request,'booklist.html',context)
@method_decorator(owner_permission_required,name='dispatch')
class BookDetailView(DetailView):
    model = Books
    context_object_name = 'book'
    template_name = 'bookdetail.html'
    pk_url_kwarg = "id"
    # def get(self, request, **kwargs):
    #     print(kwargs)
    #     id=kwargs.get('id')
    #     qs = Books.objects.get(id=id)
    #     context = {'book': qs}
    #     return render(request, 'bookdetail.html', context)
@method_decorator(owner_permission_required,name='dispatch')
class BookEditView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'editbook.html'
    pk_url_kwarg = "id"
    success_url = reverse_lazy("booklist")
    # def get(self, request,*args,**kwargs):
    #     print(kwargs)
    #     id = kwargs.get('id')
    #     qs = Books.objects.get(id=id)
    #     form=BookForm(instance=qs) #to display currently selected book in thre textbox
    #     context = {'form':form}
    #     return render(request, 'editbook.html', context)
    # def post(self,request,**kwargs):
    #     id = kwargs.get('id')
    #     qs = Books.objects.get(id=id)
    #     form=BookForm(request.POST,files=request.FILES,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,'editbook.html')
    #     else:
    #         print('form error')
    #         context={'form':form}
    #         return render(request,'editbook.html',context)

@method_decorator(owner_permission_required,name='dispatch')
class BookDeleteView(DeleteView):
    model = Books
    template_name = 'bookdelete.html'
    pk_url_kwarg = "id"
    success_url = reverse_lazy("booklist")

    # model = Books
    # context_object_name = 'book'
    # template_name = 'bookdetail.html'
    # pk_url_kwarg = "id"
    # def get(self, request, **kwargs):
    #     print(kwargs)
    #     id=kwargs.get('id')
    #     qs = Books.objects.get(id=id)
    #     qs.delete()
    #     context={'book':qs}
    #     return render(request,'booklist.html',context)
        # return redirect('listbook')
@method_decorator(owner_permission_required,name='dispatch')
class AddEmployeeView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeForm()
        context={'form':form}
        return render(request,'addemp.html',context)

    def post(self,request,*args,**kwargs):
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved successfully')
            return render(request,'addemp.html')
        else:
            context = {'form': form}
            return render(request, 'addemp.html', context)
@method_decorator(owner_permission_required,name='dispatch')
class OwnerHomeView(View):
    def get(self, request, *args, **kwargs):
        form = BookForm()
        context = {'form': form}
        return render(request, 'index.html', context)
    def post(self, request, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        else:
            print('form error')
            context = {'form': form}
            return render(request, 'index.html', context)
# from owner.models import books
# def owner_home(request):
#     return render(request,"index.html")


# def add_book(request):
#     if request.method=="GET":
#         print("Inside get")
#         return render(request,"addbook.html")
#     else:
#         print(request.method)
#         return render(request, "addbook.html")

# def list_book(request):
#     context={"books":books}
#     return render(request,"booklist.html",context)
#
# def book_detail(request,id):
#     book=[book for book in books if book["id"]==id]
#     context={"books":book}
#     return render(request,"bookdetail.html",context)

