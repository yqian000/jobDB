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
from .forms import RegisterForm, LoginForm

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
				return redirect('job')
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


class JobViewOrCreate(generics.ListCreateAPIView):
	queryset = Job.objects.all()
	serializer_class = JobSerializer

class JobUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
	queryset = Job.objects.all()
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
