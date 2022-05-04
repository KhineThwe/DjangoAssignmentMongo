from django.contrib.auth import logout
from django.core.checks import messages
from django.shortcuts import render,redirect
import pymongo

connection = pymongo.MongoClient("localhost", 27017)
database = connection["myTestDB"]
collection = database["myCollection"]


# Create your views here.
def home(request):
	return render(request, 'home.html')

def add(request):
	try:
		rname = request.POST['name']
		rpass = request.POST['password']
		ramount = request.POST['amount']
		data = {"username": rname, "password": rpass, "amount": ramount}
		collection.insert_one(data)
		return render(request, 'result.html', {"name": rname, "passcode": rpass, "amount": ramount})
	except Exception as err:
		return render(request,'result.html',{"error":err})

# def login(request):
# 	query = {"username": "khine", "password": "123"}
# 	result = collection.find(query)
# 	for i in result:
# 		idNo = i.get("_id")
# 		username = i.get("username")
# 		password = i.get("password")
# 		amount = i.get("amount")
# 	return render(request, 'home.html', {"name": username, "passcode": password, "amount": amount})
def login(request):
	return render(request, 'login.html')

def registerroute(request):
	return render(request, 'register.html')

# def resultroute(request):
# 	query = collection.find_one()
# 	return render(request, 'result.html', {"name": query.get("username"), "passcode": query.get("password"), "amount": query.get("amount")})
#
def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("")

def loginInfo(request):
	try:
		lname = request.POST['uname']
		lpass = request.POST['upass']
		result = collection.find({}, {"username": lname, "password": lpass})
		# if result.get("username") == lname a
		for i in result.items():
			print(i)
		if result:
			return render(request, 'lresult.html', {"name": result.get("username"), "passcode": result.get("password"),
			                                        "amount": result.get("amount")})
		else:
			return render(request, 'login.html')
	except Exception as err:
		print(err)
		
		
def backTohomePageroute(request):
    message = "Register successful!!!"
    return render(request, 'home.html',{"message":message})
	
	
		