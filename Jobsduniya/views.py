from django.shortcuts import render
from .models import Vacancy,Contact,Feedback
from django.contrib import messages

# Create your views here.
def home(request):
    all_jobs = Vacancy.objects.all()    
    all = {
        'all_jobs' : all_jobs,
    }
    return render(request,'home.html',all)

def jobspage(request):
    all_jobs = Vacancy.objects.all()    
    all = {
        'all_jobs' : all_jobs,
    }
    return render(request,'jobs.html',all)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name , email = email , phone = phone , desc = desc)
        contact.save()
        messages.success(request,"Thank You ! We will reach you back soon")
    return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def services(request):
    return render(request,'services.html',{})

def postjob(request):
    if request.method == "POST":
        jbtitle = request.POST.get("jobtitle",'')
        jbindustry = request.POST.get("jobindustry",'')
        jbdesignation = request.POST.get("jobdesignation",'')
        jbreponsibility = request.POST.get("jobresponsibility",'')
        jbexperience = request.POST.get("jobexperience",'')
        jbeducation = request.POST.get("jobeducation",'')
        jbemployer = request.POST.get("jobemployer",'')
        jbempphone = request.POST.get("jobempphone",'')
        jbempemail = request.POST.get("jobempemail",'')
        jbempwebsite = request.POST.get("jobempwebsite",'')
        jbctc = request.POST.get("jobctc",'')
        jblocation = request.POST.get("joblocation",'')
        jbtype = request.POST.get("jobtype",'')
        jbapplylink = request.POST.get("jobapplylink",'')
        vacancy = Vacancy(title = jbtitle,industryy=jbindustry , Designation = jbdesignation, Responsibility = jbreponsibility,
        Experience = jbexperience, Education_Qualification = jbeducation,
        Employer_name = jbemployer,Employer_phone = jbempphone,Employer_email = jbempemail,Employer_website = jbempwebsite,Ctc = jbctc,location = jblocation,
        JobType = jbtype,apply_link = jbapplylink)
        vacancy.save()
        messages.success(request, "Thank You ! This job will be posted as soon as verified.")
    return render(request,'postjob.html',{})


def search(request):
    query = request.GET['search']
    seajobdesig = Vacancy.objects.filter(Designation__icontains = query)
    seajobtitle = Vacancy.objects.filter(title__icontains = query)
    seajobindus = Vacancy.objects.filter(industryy__icontains = query)
    seajobloc = Vacancy.objects.filter(location__icontains = query)
    seajobtype = Vacancy.objects.filter(JobType__icontains=query)
    seajob = seajobdesig.union(seajobindus,seajobtitle,seajobloc,seajobtype)

    sea = {
        'seajob' : seajob 
    } 
    return render(request,"search.html", sea)