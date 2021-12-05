from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *
from .models import *
from .forms import *
from . import utility

# Create your views here.

def register(request):
	form = RegisterForm()

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')

	context = {'form': form}
	return render(request, "job/register.html", context)

def login(request):
	message = None
	if request.method == 'POST':

		form = LoginForm(request.POST)

		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth_login(request, user)
				return redirect('/job/main/')
			else:
				message = "Incorrect username or password."

	form = LoginForm()
	context = {'form': form, 'msg': message}
	return render(request, "job/login.html", context)


def logout(request):
	auth_logout(request)
	return redirect('home')


def home(request):
	return render(request, "job/home.html", {})


def main(request):
	all_posts = JobPost.objects.all()
	return render(request, "job/main.html", {
		"all_posts": all_posts
	})


def postjob(request):
	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			title = request.POST.get("title")
			company = request.POST.get("company")
			type = request.POST.get("type")
			level = request.POST.get("level")
			address = request.POST.get("address")
			city = request.POST.get("city")
			state = request.POST.get("state")
			zipcode = request.POST.get("zipcode")
			description = request.POST.get("description")
			userID = request.user.id
			utility.post_new_job(title, company, type, level, address, city, state, zipcode, description, userID)

	form = JobForm()
	return render(request, "job/postjob.html", {'form': form})

def myposts(request):
	all_myposts = JobPost.objects.filter(poster_id=request.user.id)
	return render(request, "job/myposts.html",{
		"myposts": all_myposts
	})

def updatePost(request, pk=None):
	if request.method == "GET":
		target_post = JobPost.objects.get(id=pk)
		return render(request, "job/updatepost.html",{
			"post": target_post
		})
	else:
		title = request.POST['job_title']
		company = request.POST['company']
		job_type = request.POST['job_type']
		job_level = request.POST['job_level']
		address = request.POST['address']
		zipcode = request.POST['job_zipcode']
		city = request.POST['city']
		state = request.POST['state']
		job_description = request.POST['job_description']
		utility.update_post(pk, title, company, job_type,job_level,address, zipcode, city, state, job_description)
	return redirect('/job/myposts/')

def deletePost(request, pk=None):
	JobPost.objects.get(id=pk).delete()
	return redirect('/job/myposts/')

class JobViewOrCreate(generics.ListCreateAPIView):
	queryset = JobPost.objects.all()
	serializer_class = JobSerializer

class JobUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
	queryset = JobPost.objects.all()
	serializer_class = JobSerializer


# class JobViewOrCreate(APIView):
# 	"""
# 	List all jobs, or create a new job.
# 	"""
# 	def get(self, request, format=None):
# 		jobs = Job.objects.all()
# 		serializer = JobSerializer(jobs, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = JobSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class JobUpdateOrDelete(APIView):
# 	"""
# 	Update or delete a job instance.
# 	"""
# 	def get_object(self, pk):
# 		try:
# 			return Job.objects.get(pk=pk)
# 		except Job.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		job = self.get_object(pk)
# 		serializer = JobSerializer(job)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		job = self.get_object(pk)
# 		serializer = JobSerializer(job, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		job = self.get_object(pk)
# 		job.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
