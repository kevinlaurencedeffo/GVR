from .models import Stocks
from django.shortcuts import render, get_object_or_404,redirect
import dateparser
from django.http import  HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from .forms import StockForm

def render_pdf_art(self):
    dat = dateparser.parse('today')
    query = Stocks.objects.all().all()
    obj={}
    if query:
        obj = StockForm(query).data
    template_path = 'stocks/art.html'
    context = {'obj': obj,'date':dat}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="art.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response

@login_required    
def gstock(request):
    
    obj = Stocks.objects.all()
    return render(request, 'stocks/gstock.html',{'obj':obj})


def create_Art(request): 
    msg= ''
    try:
        article_nane = request.POST.get('article_name')
        libele = request.POST.get('libele')
        quantite = request.POST.get('quantite')
        typea = request.POST.get('typea')
        prix = request.POST.get('prix')
        si = request.POST.get('si')
        date = request.POST.get('date')
        img = request.POST.get('img')
        newpro = Stocks.objects.create(article_name=article_nane,si=si,typea=typea,libele=libele,img=img,quantite=quantite,prix=prix,date=date)
        newpro.save()
        msg = 'cree'
        messages.success(request,"Creer avec success")
        return redirect('gstock')
    except Exception as e:
        messages.error(request,f"{e}")
    return render(request, 'stocks/create.html',{'msg':msg})

def update_Art(request, myid):
    obj = get_object_or_404(Stocks, id=myid)
    try:
        obj.article_name = request.POST.get('article_name')
        obj.libele = request.POST.get('libele')
        obj.prix = request.POST.get('prix')
        obj.si = request.POST.get('si')
        obj.typea = request.POST.get('typea')
        obj.quantite = request.POST.get('quantite')
        obj.date = request.POST.get('date')
        obj.img = request.POST.get('img')
        obj.save()
        messages.success(request,"Modifier avec success")
    except:
        messages.error(request,"erreur veuillez verifier le formulaire")
    return render(request, 'stocks/updArt.html',{"obj":obj})

def detail_Art(request, myid):
    product_object  =  get_object_or_404(Stocks,id=myid)
    
    return render(request, 'stocks/detailArt.html', {'product_object': product_object})

def delete_Art(request, myid):
    obj = get_object_or_404(Stocks,id=myid)
    if request.method == "POST":
        obj.delete()
        return redirect('gstock')
    return render(request, 'stocks/deleteArt.html')
