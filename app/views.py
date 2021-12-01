from django.shortcuts import render
from django.http import HttpResponseRedirect

from app.models import *

from app.forms import *
import hashlib
from django.contrib.auth import logout
# Create your views here.
def home(request):
	return render(request,'home/index.html')

def employee_registration(request):
	if request.method=="POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		email=request.POST['email']
		phone=request.POST['phone']
		dob=request.POST['dob']
		age=request.POST['age']
		gender=request.POST['gender']
		marital_status=request.POST['marital_status']
		address=request.POST['address']
		language=request.POST['language']
		qalification=request.POST['qalification']
		experience=request.POST['experience']
		jobopted=request.POST['jobopted']
		compknowledge=request.POST['compknowledge']
		resume=request.FILES['resume']
		check=employee_tb.objects.all().filter(email=email)
		if check:
			return render(request,'home/candidates_my_resume_add_new.html',{'error':'Email Id Already Registerd '})
		else:
			add=employee_tb(fname=fname,lname=lname,email=email,phone=phone,dob=dob,age=age,gender=gender,marital_status=marital_status,address=address,language=language,qalification=qalification,experience=experience,jobopted=jobopted,compknowledge=compknowledge,resume=resume)
			add.save()
			return render(request,'home/candidates_my_resume_add_new.html',{'msg':'Thank You For Registering'})
	else:
		return render(request,'home/candidates_my_resume_add_new.html')

def employer_registration(request):
	if request.method=="POST":
		logo = request.FILES['logo']
		nameorg = request.POST['nameorg']
		rname = request.POST['rname']
		email = request.POST['email']
		phone = request.POST['phone']
		phoner = request.POST['phoner']
		designation = request.POST['designation']
		website = request.POST['website']
		address = request.POST['address']
		positionnumber = request.POST['noof']
		gender = request.POST['gender']
		jobtitle = request.POST['jobtitle']
		description = request.POST['jobdescription']
		positionnumber = request.POST['noof']
		gender = request.POST['gender']
		jobtitle = request.POST['jobtitle']
		description = request.POST['jobdescription']

		positionnumber1 = request.POST['noof1']
		gender1 = request.POST['gender1']
		jobtitle1 = request.POST['jobtitle1']
		description1 = request.POST['jobdescription1']

		positionnumber2 = request.POST['noof2']
		gender2 = request.POST['gender2']
		jobtitle2 = request.POST['jobtitle2']
		description2 = request.POST['jobdescription2']

		positionnumber3 = request.POST['noof3']
		gender3 = request.POST['gender3']
		jobtitle3 = request.POST['jobtitle3']
		description3 = request.POST['jobdescription3']

		positionnumber4 = request.POST['noof4']
		gender4 = request.POST['gender4']
		jobtitle4 = request.POST['jobtitle4']
		description4 = request.POST['jobdescription4']
		check=employer_tb.objects.all().filter(email=email)
		if check:
			return render(request,'home/employer_post_new.html',{'error':'Email Id Already Registerd '})
		else:
			add=employer_tb(logo=logo,nameorg=nameorg,rname=rname,email=email,phone=phone,phoner=phoner,designation=designation,website=website,address=address,positionnumber=positionnumber,gender=gender,jobtitle=jobtitle,description=description,positionnumber1=positionnumber1,gender1=gender1,jobtitle1=jobtitle1,description1=description1,positionnumber2=positionnumber2,gender2=gender2,jobtitle2=jobtitle2,description2=description2,positionnumber3=positionnumber3,gender3=gender3,jobtitle3=jobtitle3,description3=description3,positionnumber4=positionnumber4,gender4=gender4,jobtitle4=jobtitle4,description4=description4)
			add.save()
		return render(request,'home/employer_post_new.html',{'msg':'Thank You For Registering'})
	else:
		return render(request,'home/employer_post_new.html')

# def employer_registration(request):
# 	if request.method=="POST":
# 		logo = request.FILES['logo']
# 		nameorg = request.POST['nameorg']
# 		rname = request.POST['rname']
# 		email = request.POST['email']
# 		phone = request.POST['phone']
# 		phoner = request.POST['phoner']
# 		designation = request.POST['designation']
# 		website = request.POST['website']
# 		address = request.POST['address']
# 		positionnumber = request.POST.getlist('noof')
# 		gender = request.POST.getlist('gender')
# 		jobtitle = request.POST.getlist('jobtitle')
# 		description = request.POST.getlist('jobdescription')
# 		check=employer_tb.objects.all().filter(email=email)
# 		if check:
# 			return render(request,'employer_post_new.html')
# 		else:
# 			c = min([len(positionnumber), len(gender), len(jobtitle), len(description)])
# 			print(c,"_________________________________________")
# 			for i in range(c):
			
# 				add=employer_tb(logo=logo,nameorg=nameorg,rname=rname,email=email,phone=phone,phoner=phoner,designation=designation,website=website,address=address,positionnumber= positionnumber[i],gender=gender[i],jobtitle=jobtitle[i],description=description[i])
# 				add.save()
# 			return render(request,'employer_post_new.html')
# 	else:
# 		return render(request,'employer_post_new.html')


# def generatescripts(request):
#     if request.method == 'POST':
#         positionnumber = request.POST.getlist('noof')
#         gender = request.POST.getlist('gender')
#         jobtitle = request.POST.getlist('jobtitle')
#         description = request.POST.getlist('jobdescription')

#         # FIXME: number of each field should equal
#         c = min([len(positionnumber), len(gender), len(jobtitle), len(description)])
#         for i in range(c):
#         	form = GenerateScriptsForm({'positionnumber': positionnumber[i], 'gender': gender[i], 'jobtitle': jobtitle[i], 'description': description[i]})
#         	if form.is_valid():
#         		form.save()
#         return render(request, 'employer_post_new.html')
#         # return HttpResponseRedirect('/thanks/')

#     else:
#         form = GenerateScriptsForm()

#     return render(request, 'employer_post_new.html', {'form': form})

def admin_signup(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']		
		password=request.POST['password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		check=admin_tb.objects.all().filter(email=email)
		if check:
			return render(request,"auth/signup.html",{'msgkey':"Mail id Already Registerd"})
			
		else:
			add=admin_tb(email=email,name=name,password=hashpass,pwd=password)
			add.save()
		return render(request,"auth/login.html")

	else:
		return render(request,'auth/signup.html')
	# return render(request,'pages-login.html')


def admin_login(request):
	if request.method=="POST":
		email=request.POST['email']
		password=request.POST['password']
		hashpass=hashlib.md5(password.encode('utf8')).hexdigest()
		b=admin_tb.objects.all().filter(email=email,password=hashpass)
		if b.exists():
			for x in b:
				request.session["myid"]=x.id
				request.session["name"]=x.name

				return render(request,'auth/index.html')

		else:
			return render(request,'auth/login.html',{'msgkey':'Invalid credentials'})
	else:
		return render(request,'auth/login.html')
	


def logout(request):
    if request.session.has_key('myid'):
        del request.session['myid']
        del request.session['name']

        logout(request)
    return HttpResponseRedirect('/admin_login/')


def admin_index(request):
    if request.session.has_key('myid'):
        return render(request,'auth/index.html')
    return HttpResponseRedirect('/admin_login/')



def admin_view_employee(request):
    if request.session.has_key('myid'):
        query=employee_tb.objects.all()
        return render(request,'auth/employee_view.html',{'query':query})

    return HttpResponseRedirect('/admin_login/')


def admin_view_employer(request):
    if request.session.has_key('myid'):
        query=employer_tb.objects.all()
        return render(request,'auth/employer_view.html',{'query':query})

    return HttpResponseRedirect('/admin_login/')


########################################################################


