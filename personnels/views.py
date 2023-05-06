from .models import Perso,Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
import smtplib
import ssl
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import os
from xhtml2pdf import pisa
from datetime import date
import dateparser
from email.message import EmailMessage
from django.contrib.auth.decorators import login_required

def render_pdf_Pers(request):
    dat = dateparser.parse('today')
    obj = Perso.objects.all()
    template_path = 'personnels/pers.html'
    context = {'obj': obj,'date':dat}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="pers.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       messages.error("Impossible d'imprimer")
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response
@login_required
def grh(request):
    objs=Perso.objects.all()
    obj=Task.objects.all()
    item_nameE = request.GET.get('item_nameE')
    item_nameD = request.GET.get('item_nameD')
    if item_nameE !='' and item_nameE is not None:
        objs = Perso.objects.filter(name__icontains=item_nameE)
    if item_nameD !='' and item_nameD is not None:
        obj = Task.objects.filter(nom__icontains=item_nameD)
    return render(request, 'personnels/perso.html', {'objs':objs,'obj':obj})


def create_Pers(request):
    try:
        nom = request.POST.get('name')
        prenom = request.POST.get('surname')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        cni = request.POST.get('cni')
        matricule = request.POST.get('matricule')
        sexe = request.POST.get('sexe')
        poste = request.POST.get('poste')
        date = request.POST.get('date')
        quartier = request.POST.get('quartier')
        nationalite = request.POST.get('nationalite')
        newpro = Perso.objects.create(name=nom,surname=prenom,cni=cni,nationalite=nationalite,matricule=matricule,poste=poste,quartier=quartier,sexe=sexe,date=date,email=email,tel=tel)
        newpro.save()
        messages.success(request,"Employe creer avec succes")
        return redirect('grh')
    except:
        messages.error(request,"Impossible d'ajouter l'employe.Veuillez verifier le format des champs.")
    return render(request, 'personnels/perso.html')

def create_Task(request):
    if request.method == "POST":
        try:
            nom = request.POST.get('nom')
            service = request.POST.get('service')
            montant = request.POST.get('montant')
            date_fin = request.POST.get('date_fin')
            date_debut = request.POST.get('date_debut')
            etat = request.POST.get('etat')
            chef_projet = request.POST.get('chef_projet')
            newpro = Task.objects.create(nom=nom,service=service,chef_projet=chef_projet,date_debut=date_debut,date_fin=date_fin,montant=montant,etat=etat)
            newpro.save()
            msg = f"Mr {chef_projet.split('(')[0].split(')')[0]} la tache: {nom} vous a ete confier ce {date_debut} et doit etre achever le {date_fin}.\n voici les services du projet: {service}.\n Veuillez contacter l'entreprise pour plus d'infos." 
            email = chef_projet.split('(')[1].split(')')[0]
            password = "yjvxhcnqppfrximx"
            sender ="kevinlaurencedeffo@gmail.com"
            em = EmailMessage()
            em['From'] = sender
            em['To'] = email
            em['Subject'] = "msg"
            em.set_content(msg)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender, password)
                smtp.sendmail(email, email, em.as_string())
                messages.success(request,"Tache attribuer avec success")
            return redirect('grh')
        except:
            messages.error(request,"Tache non Attribuer, veuillez verifier le format des chapms")

    return render(request, 'personnels/perso.html')

                
def update_Pers(request, myid):
    obj = get_object_or_404(Perso, id=myid)
    if request.method == "POST":
        try:
            obj.name = request.POST.get('name')
            obj.surname = request.POST.get('surname')
            obj.cni = request.POST.get('cni')
            obj.date = request.POST.get('date')
            obj.sexe = request.POST.get('sexe')
            obj.matricule = request.POST.get('matricule')
            obj.poste = request.POST.get('poste')
            obj.quartier = request.POST.get('quartier')
            obj.email = request.POST.get('email')
            obj.tel = request.POST.get('tel')
            obj.nationalite = request.POST.get('nationalite')
            obj.save()
            messages.success(request,"Employe Modifier Avec success")
        except:
            messages.error(request,"veuillez reesayer!")
    return render(request, 'personnels/updPers.html',{"obj":obj})

def update_Task(request, myid):
    obj = get_object_or_404(Task, id=myid)
    if request.method == "POST":
        try:
            obj.nom = request.POST.get('nom')
            obj.service = request.POST.get('service')
            obj.montant = request.POST.get('montant')
            obj.etat = request.POST.get('etat')
            obj.date_debut = request.POST.get('date_debut')
            obj.date_fin = request.POST.get('date_fin')
            obj.chef_projet = request.POST.get('chef_projet')
            obj.save()
            messages.success(request,"Tache Modifier avec success")
        except:
            messages.error(request,"Veuillez verifier le format des champs")
    return render(request, 'personnels/updTask.html',{"obj":obj})

def detail_Pers(request, myid):
    product_object  =  get_object_or_404(Perso,id=myid)
    return render(request, 'personnels/detailPers.html', {'product_object': product_object})


def delete_Pers(request, myid):
    obj = get_object_or_404(Perso,id=myid)
    if request.method == "POST":
        obj.delete()
        return redirect('grh')
    return render(request, 'personnels/deletePers.html')

def delete_Task(request, myid):
    obj = get_object_or_404(Task,id=myid)
    if request.method == "POST":
        obj.delete()
        return redirect('grh')
    return render(request, 'personnels/deleteTask.html')
