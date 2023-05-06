from .models import Caisse, Solde
from django.urls import reverse_lazy
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import os
from xhtml2pdf import pisa
from fpdf import FPDF
from django.contrib.auth.decorators import login_required
from datetime import date
import dateparser

def render_pdf_JC(request):
    dat = dateparser.parse('today')
    obj = Caisse.objects.all()
    sol = Solde.objects.filter(pk=1)  
    obje = Caisse.objects.filter(typeO="Encaissement")
    objd = Caisse.objects.filter(typeO="Decaissement")
    
    somE=0
    somD=0
    si=0
    sf=0
    for a in sol:
        si=a.soldeI
    for ad in obje:
        somE=somE+ad.montant
    for av in objd:
        somD=somD+av.montant
    sf=int(si)+int(somE)-int(somD)
    template_path = 'caisse/JC.html'
    context = {'obj': obj,'date':dat,'si':si,'sf':sf,'somE':somE,'somD':somD}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="JC.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       messages.error(request,"Impossible d'imprimer")
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def flux(request):
    lun = dateparser.parse('lundi').date()
    mar = dateparser.parse('mardi').date()
    mer = dateparser.parse('mercredi').date()
    ven = dateparser.parse('vendredi').date()
    jeu = dateparser.parse('jeudi').date()
    sam = dateparser.parse('samedi').date()
    agE=0
    bgE=0
    cgE=0
    dgE=0
    egE=0
    fgE=0
    agD=0
    bgD=0
    cgD=0
    dgD=0
    egD=0
    fgD=0
    EagE = Caisse.objects.filter(typeO="Encaissement", date=lun)
    EbgE = Caisse.objects.filter(typeO="Encaissement", date=mar)
    EcgE = Caisse.objects.filter(typeO="Encaissement", date=mer)
    EdgE = Caisse.objects.filter(typeO="Encaissement", date=jeu)
    EegE = Caisse.objects.filter(typeO="Encaissement", date=ven)
    EfgE = Caisse.objects.filter(typeO="Encaissement", date=sam)
    DagD = Caisse.objects.filter(typeO="Decaissement", date=lun)
    DbgD = Caisse.objects.filter(typeO="Decaissement", date=mar)
    DcgD = Caisse.objects.filter(typeO="Decaissement", date=mer)
    DdgD = Caisse.objects.filter(typeO="Decaissement", date=jeu)
    DegD = Caisse.objects.filter(typeO="Decaissement", date=ven)
    DfgD = Caisse.objects.filter(typeO="Decaissement", date=sam)
    for age in EagE: 
        agE = agE+ int(age.montant)
    for age in EbgE: 
        bgE = bgE+int(age.montant)
    for age in EcgE: 
        cgE = cgE+int(age.montant)
    for age in EdgE: 
        dgE = dgE+ int(age.montant)
    for age in EegE: 
        egE = egE+ int(age.montant)
    for age in EfgE: 
        fgE = fgE+int(age.montant)
    for age in DagD: 
        agD = agD+int(age.montant)
    for age in DbgD: 
        bgD = bgD+int(age.montant)
    for age in DcgD: 
        cgD = cgD+int(age.montant)
    for age in DdgD: 
        dgD = dgD+int(age.montant)
    for age in DegD: 
        egD = egD+int(age.montant)
    for age in DfgD: 
        fgD = fgD+int(age.montant)
    
    if type(agE) is not int:
        agE = 0
    if type(bgE) is not int:
        bgE = 0
    if type(cgE) is not int:
        cgE = 0
    if type(dgE) is not int:
        dgE = 0
    if type(egE) is not int:
        egE = 0
    if type(fgE) is not int:
        fgE = 0
    if type(agD) is not int:
        agD = 0
    if type(bgD) is not int:
        bgD = 0
    if type(cgD) is not int:
        cgD = 0
    if type(dgD) is not int:
        dgD = 0
    if type(egD) is not int:
        egD = 0
    if type(fgD) is not int:
        fgD = 0

    objs = Caisse.objects.filter(typeO="Encaissement")
    obj = Caisse.objects.filter(typeO="Decaissement")
    item_nameE = request.GET.get('item_nameE')
    item_nameD = request.GET.get('item_nameD')
    if item_nameE !='' and item_nameE is not None:
        objs = Caisse.objects.filter(typeO="Encaissement",reference__icontains=item_nameE)
    if item_nameD !='' and item_nameD is not None:
        obj = Caisse.objects.filter(typeO="Decaissement",reference__icontains=item_nameD)
    soldei = Solde.objects.filter(pk=1)
    somE=0
    somD=0
    si=0
    sf=0
    for a in soldei:
        si=a.soldeI
    for ad in objs:
        somE=somE+ad.montant
    for av in obj:
        somD=somD+av.montant
    sf=int(si)+int(somE)-int(somD)
    return render(request, 'caisse/flux.html', {'objs':objs,'obj':obj,'si':si,'sf':sf,'somE':somE,'somD':somD,'agE':agE,'bgE':bgE,'cgE':cgE,'dgE':dgE,'egE':egE,'fgE':fgE,'agD':agD,'bgD':bgD,'cgD':cgD,'dgD':dgD,'egD':egD,'fgD':fgD})


def create_pro(request):
    if request.method == "POST":
        try:
            ref = request.POST.get('reference')
            lib = request.POST.get('libele')
            mont = request.POST.get('montant')
            dat = request.POST.get('date')
            typ = request.POST.get('typeO')
            newpro = Caisse.objects.create(reference=ref,libele=lib,montant=mont,date=dat,typeO=typ)
            newpro.save()
            messages.success(request,"Operation creer avec success")
        except:
            messages.error("champs vide ou mauvais format")
        return redirect('flux')
    
    return render(request, 'caisse/flux.html')

def update_O(request, myid):
    obj = get_object_or_404(Caisse, id=myid)
    if request.method == "POST":
        try:
            obj.reference = request.POST.get('reference')
            obj.libele = request.POST.get('libele')
            obj.montant = request.POST.get('montant')
            obj.date = request.POST.get('date')
            obj.save()
            messages.success(request,"Operation modifier avec success")
        except:
            messages.error(request,"Erreur lors de la validation")
    return render(request, 'caisse/updO.html',{"obj":obj})

def update_SoldeI(request, myid):
    obj = get_object_or_404(Solde,id=myid)
    if request.method == "POST":
        try:
            obj.soldeI = request.POST.get('soldeI')
            obj.save()
            messages.success(request,"Solde Initial modifier avec success")
            return redirect('flux')
        except:
            messages.error(request,"Entrer un montant valide")
    return render(request, 'caisse/updsi.html',{"obj":obj})

def delete_O(request, myid):
    obj = get_object_or_404(Caisse,id=myid)
    if request.method == "POST":
        try:
            obj.delete()
            messages.success(request,"Operation supprimer avec success")
        except:
            messages.error(request,"Imposible de supprimer")
    return render(request, 'caisse/deleteO.html')
    
