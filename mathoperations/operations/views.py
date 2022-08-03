from django.shortcuts import render
from django.views.generic import View
from operations.forms import OperationForm,StarForm
from math import factorial

# Create your views here.

class AddView(View):
    def get(self,request):
        form=OperationForm()
        context={'form':form}
        return render(request,'add.html',context)
    def post(self,request):
        form=OperationForm(request.POST)
        if form.is_valid(): #ensures no error
            print(form.cleaned_data) #ctrl goes to clean method in forms.py
            num1=form.cleaned_data.get('num1')
            num2=form.cleaned_data.get('num2')
            result = int(num1) + int(num2)
            context={"result":result}
            return render(request, 'add.html',context)
        else:
            form = OperationForm(request.POST)
            context = {'form': form}
            return render(request, 'add.html', context)
class SubView(View):
    def get(self,request):
        form = OperationForm()
        context = {'form': form}
        return render(request, 'sub.html', context)
    def post(self,request):
        form = OperationForm(request.POST)
        if form.is_valid():  # ensures no error
            print(form.cleaned_data)
            num1 = form.cleaned_data.get('num1')
            num2 = form.cleaned_data.get('num2')
            result = int(num1) - int(num2)
            context = {"result": result}
            return render(request, 'sub.html', context)
        else:
            form = OperationForm(request.POST)
            context = {'form': form}
            return render(request, 'sub.html', context)
class MulView(View):
    def get(self,request):
        form = OperationForm()
        context = {'form': form}
        return render(request, 'mul.html', context)
    def post(self,request):
        form = OperationForm(request.POST)
        if form.is_valid():  # ensures no error
            print(form.cleaned_data) #ctrl goes to clean method in forms.py
            num1 = form.cleaned_data.get('num1')
            num2 = form.cleaned_data.get('num2')
            result = int(num1) * int(num2)
            context = {"result": result}
            return render(request, 'mul.html', context)
        else:
            form = OperationForm(request.POST)
            context={'form':form}
            return render(request, 'mul.html', context)
class DivView(View):
    def get(self,request):
        form = OperationForm()
        context = {'form': form}
        return render(request, 'div.html', context)
    def post(self,request):
        form = OperationForm(request.POST)
        if form.is_valid():  # ensures no error
            print(form.cleaned_data)
            num1 = form.cleaned_data.get('num1')
            num2 = form.cleaned_data.get('num2')
            result = int(num1) / int(num2)
            context = {"result": result}
            return render(request, 'div.html', context)
        else:
            form=OperationForm(request.POST)
            context={'form':form}
            return render(request,'div.html',context)
class SquareView(View):
    template_name='square.html'
    form_class=StarForm
    def get(self,request):
        form = self.form_class
        context = {'form': form}
        return render(request,self.template_name, context)
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():  # ensures no error
            num = form.cleaned_data.get('num')
            result = int(num)**2
            context = {"result": result}
            return render(request, self.template_name, context)
        else:
            form = self.form_class(request.POST)
            context = {'form': form}
            return render(request, self.template_name, context)
class CubeView(View):
    template_name='cube.html'
    form_class=StarForm
    def get(self,request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            num = form.cleaned_data.get('num')
            result = int(num)**3
            context = {'result': result}
            return render(request, self.template_name, context)
        else:
            form = self.form_class(request.POST)
            context = {'form': form}
            return render(request, self.template_name, context)
class FactView(View):
    template_name='fact.html'
    form_class=StarForm
    def get(self,request):
        form=self.form_class()
        context={'form':form}
        return render(request,self.template_name,context)
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            num=int(form.cleaned_data.get('num'))
            fact=1
            result=factorial(num)
            print(result)
            context={'result':result}
            return render(request,self.template_name,context)
        else:
            form = self.form_class(request.POST)
            context = {'form': form}
            return render(request, self.template_name, context)
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
