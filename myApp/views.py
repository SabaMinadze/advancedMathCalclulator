from django.shortcuts import render
from math import sqrt


def index(request):
    return render(request, 'index.html')



def result(request):
    if request.method == "POST":
        a = request.POST.get("a")
        b = request.POST.get("b")
        a = int(a)
        b = int(b)
        c = sqrt((a * a) + (b * b))
        c = float(c)
        return render(request, "result.html", {"a":a, "b":b, "c":c})
    
def heron(request):
    if request.method == "POST":        
                a1 = request.POST.get("a1")
                b1 = request.POST.get("b1")
                c1 = request.POST.get("c1")
                a1 = int(a1)
                b1 = int(b1)
                c1 = int(c1)
                p1 = ((a1 + b1 + c1) / 2)
                p1 = int(p1)
                answ = sqrt(p1 * (p1 - a1) * (p1 - b1) * (p1 - c1))
                return render(request, 'heron.html', {"answ": answ})   


def discriminant(request):
      if request.method == "POST":  
        a2 = request.POST.get("a2")  
        b2 = request.POST.get("b2")
        c2 = request.POST.get("c2")
        a2 = int(a2)
        b2 = int(b2)
        c2 = int(c2)
        d = (b2 * b2) - (4 * a2 * c2)
        x1 = ((0 - b2) - sqrt(d)) / (2 * a2)
        x2 = ((0 - b2) + sqrt(d)) / (2 * a2)
        return render(request, "discriminant.html", {"d":d, "x1":x1, "x2":x2})     