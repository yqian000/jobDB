from django.db import models
from django.contrib.auth.models import User
from .models import *
from datetime import date


def post_new_job(title, company, type, level, address, city, state, zipcode, description, userID):
    new_job_zipcode = Zipcode.objects.get_or_create(zipcode=zipcode, city=city, state=state)
    new_job_location = Location.objects.get_or_create(street_address=address, zipcode_id=new_job_zipcode[0].zipcode)
    new_job_company = Company.objects.get_or_create(name=company)
    new_job_level = JobLevel.objects.get_or_create(level_name=level)
    new_job_type = JobType.objects.get_or_create(type_name=type)
    today = date.today()
    new_job_post = JobPost(title=title, post_date=today,
                           job_description= description, company_id= new_job_company[0].id,
                           job_level_id=new_job_level[0].id, job_type_id = new_job_type[0].id,
                           location_id=new_job_location[0].id,
                           poster_id=userID
                           )
    new_job_post.save()



def update_post(postID, title, company, job_type,job_level,address, zipcode, city, state, job_description):
    post = JobPost.objects.get(id=postID)
    new_job_zipcode = Zipcode.objects.get_or_create(zipcode=zipcode, city=city, state=state)
    new_job_location = Location.objects.get_or_create(street_address=address, zipcode_id=new_job_zipcode[0].zipcode)
    new_job_company = Company.objects.get_or_create(name=company)
    new_job_level = JobLevel.objects.get_or_create(level_name=job_level)
    new_job_type = JobType.objects.get_or_create(type_name=job_type)
    today = date.today()
    post.title = title
    post.post_date = today
    post.job_description = job_description
    post.company_id = new_job_company[0].id
    post.job_level_id = new_job_level[0].id
    post.job_type_id = new_job_type[0].id
    post.location_id=new_job_location[0].id
    post.save()




