from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from wcapp.forms import WordForm, VowelForm


class WordCountView(View):
    def get(self,request,*args,**kwargs):
        form=WordForm()
        context={"form":form}
        return render(request,"wordcount.html", context)
    def post(self,request,*args,**kwargs):
        form=WordForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data.get("text")
            words=text.split(" ")
            wc={}
            for word in words:
                if(word in wc):
                    wc[word]+=1
                else:
                    wc[word]=1
            context={"result":wc}
            return render(request,"wordcount.html",context)
        else:
            context = {"form": form}
            return render(request, "wordcount.html", context)
class VowelCountView(View):
    def get(self, request, *args, **kwargs):
        form=VowelForm()
        context = {"form": form}
        return render(request, "vowelcount.html", context)

    def post(self, request, *args, **kwargs):
        form = VowelForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text")
            vowel=["a","e","i","o","u"]
            word=[]
            vc=[ i for i in text if i in vowel]
        context = {"result": vc}
        return render(request, "vowelcount.html", context)
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')