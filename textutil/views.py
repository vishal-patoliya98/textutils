from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    a=request.POST.get("text","default")
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get("fullcaps", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")

    if removepunc=="on":
        #analyzed=a
        analyzed=""
        punctuations = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for char in a:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        a=analyzed
        #return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed=""
        for char in a:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        a=analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed=""
        for char in a:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        params = {'purpose': 'remover new lines', 'analyzed_text': analyzed}
        a=analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(a):
            if not(a[index]== " " and a[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'remover new lines', 'analyzed_text': analyzed}

    if(removepunc!="on" and newlineremover!="on" and fullcaps!="on" and extraspaceremover!="on"):
        return HttpResponse("Eroor")

    return render(request, 'analyze.html', params)

"""def capitlizefirst(request):
    return HttpResponse("capitlizefirst")

def newlineremove(request):
    return HttpResponse("newlineremove")

def charcount(request):
    return HttpResponse("charcount")

def about(request):
    return HttpResponse("hello vishal")
"""