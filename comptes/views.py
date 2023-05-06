from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm,UpdForm
from .models import User
from caisse.models import Caisse
import dateparser
from personnels.models import Perso, Task
from stocks.models import Stocks



def login_view(request):
    form = LoginForm(request.POST or None)
    user=''
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                messages.success(request,"bienvenu Admin")
                login(request, user)
                return redirect('administrateur')
            elif user is not None and user.is_grh:
                messages.success(request,"bienvenu GRH")
                login(request, user)
                return redirect('grh')
            elif user is not None and user.is_gstock:
                messages.success(request,"bienvenu GS")
                login(request, user)
                return redirect('gstock')
            elif user is not None and user.is_comptable:
                messages.success(request,"bienvenu GJC")
                login(request, user)
                return redirect('comptable')
            elif user is not None and user.is_anonimous:
                messages.warning(request,"Compte Anonyme veuillez attendre la validation de votre compte")
                return redirect('anonimous')
            else:
                messages.warning(request,"Compte Anonyme veuillez attendre la validation de votre compte")
                return redirect('anonimous')
            
        else:
            messages.error(request,"Erreur lors de la validation du formulaire")
    return render(request, 'comptes/login.html', {'form': form, 'user':user})


login_required
def administrateur(request):
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

    obj = 0
    objs = 0
    datet = dateparser.parse('today').date()
    obs = Caisse.objects.filter(typeO="Encaissement", date=datet)
    ob = Caisse.objects.filter(typeO="Decaissement", date=datet)        
    objp = Perso.objects.all().count()
    obja = Stocks.objects.all().count()
    for o in obs:
        objs = objs+o.montant
    for o in ob:
        obj = obj+o.montant
    use = User.objects.filter(is_anonimous=True)
    taskN = Task.objects.filter(etat="Nouveau").count()
    taskE = Task.objects.filter(etat="En Cour").count()
    taskR = Task.objects.filter(etat="Realiser").count()
    
    return render(request, 'comptes/dashboard.html', {'objs':objs,'obj':obj,'objp':objp,'obja':obja,'use':use,'taskN':taskN,'taskE':taskE,'taskR':taskR,'agE':agE,'bgE':bgE,'cgE':cgE,'dgE':dgE,'egE':egE,'fgE':fgE,'agD':agD,'bgD':bgD,'cgD':cgD,'dgD':dgD,'egD':egD,'fgD':fgD})

login_required
def accounts(request):
    obj = User.objects.all()
    return render(request, 'comptes/accounts.html',{'obj':obj})

login_required
def anonimous(request):
    return render(request, 'comptes/anonimous.html')

login_required
def index(request):
    return render(request, 'comptes/index.html')

def register(request):
    user = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"Compte cree avec success")
            return redirect('login')
        else:
            messages.error(request,"Formulaire non Valide")
    else:
        form = SignUpForm()
    return render(request,'comptes/register.html', {'form': form, 'user':user})

login_required
def Logout(request):
    messages.warning(request,"vous allez vous deconnecter")
    logout(request)
    return redirect('index')

login_required
def update_Me(request, myid):
    obj = get_object_or_404(User, id=myid)
    if request.method == "POST":
        try:
            obj.username = request.POST.get('musername')
            obj.email = request.POST.get('memail')
            obj.save()
            messages.success(request,"Modifier avec succes")
        except:
            messages.error(request,"Une Erreur s'est produite")
    return render(request, 'comptes/settings.html',{"obj":obj})
login_required
def update_User(request, myid):
    form=UpdForm(request.POST)
    obj = get_object_or_404(User, id=myid)
    if request.method == "POST":
        try:
            obj.username = request.POST.get('username')
            obj.email = request.POST.get('email')
            obj.is_admin = request.POST.get('is_admin')
            obj.is_comptable = request.POST.get('is_comptable')
            obj.is_grh = request.POST.get('is_grh')
            obj.is_gstock = request.POST.get('is_gstock')
            obj.is_anonimous = request.POST.get('is_anonimous')
            obj.save()
            messages.success(request,"Modifier avec succes")
        except:
            messages.error(request,"Verifier le format des champs")
    return render(request, 'comptes/updUser.html',{"obj":obj,'form':form})
login_required
def delete_User(request, myid):
    obj = get_object_or_404(User,id=myid)
    if request.method == "POST":
        try:
            obj.delete()
            messages.success(request,"Supprimer avec succes")
        except:
            messages.error(request,"Impossible de supprimer")
        return redirect('grh')
    return render(request, 'comptes/deleteUser.html')


