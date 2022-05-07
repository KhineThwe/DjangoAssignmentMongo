from django.contrib.auth import logout
from django.core.checks import messages
from django.shortcuts import render,redirect
import pymongo
import random

connection = pymongo.MongoClient("localhost", 27017)
database = connection["myTestDB"]
collection = database["myCollection"]


# Create your views here.
def home(request):
	return render(request, 'home.html')

def add(request):
	try:
		randomNo = random.randint(100,900)
		rId = randomNo
		rname = request.POST['name']
		rpass = request.POST['password']
		ramount = request.POST['amount']
		data = {"_id":rId,"username": rname, "password": rpass, "amount": ramount}
		collection.insert_one(data)
		return render(request, 'result.html', {"id":rId,"name": rname, "passcode": rpass, "amount": ramount})
	except Exception as err:
		return render(request,'result.html',{"error":err})

def login(request):
	return render(request, 'login.html')

def registerroute(request):
	return render(request, 'register.html')

def logout_request(request):
	return redirect("/")

def loginInfo(request):
	try:
		lname = request.POST['uname']
		lpass = request.POST['upass']
		query={"username":lname,"password":lpass}
		result = collection.find_one(query)
		name,password,amount = result.get("username"),result.get("password"),result.get("amount")
		return render(request,'lresult.html' ,{"name": name,"passcode": password,"amount": amount})
	except Exception as err:
		return render(request,{"err":err})
		
def backTohomePageroute(request):
    message = "Register successful!!!"
    return render(request, 'home.html',{"message":message})

def retrieve(request):
	result = collection.find()
	return render(request ,'retrieve.html' ,{"details": result})

def edit(request,id):
	query = {"_id": id}
	object = collection.find_one(query)
	return render(request ,'edit.html' ,{"object": query})

def update(request,id):
	# object = Details.objects.get(id=id)
	# form = detailsForm(request.POST,instance = object)
	# if form.is_valid():
	# 	form.save()
	# 	object=Details.objects.all()
	# 	return redirect('retrieve')
	pass

def delete(request,id):
	# Details.objects.filter(id=id).delete()
	# return redirect('retrieve')
	pass
