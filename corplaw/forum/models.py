from django.db import models
from django import forms
from django.utils import timezone
import re
from django.core.validators import validate_email

# Create your models here.
class user_main(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_id = models.EmailField()
	college_name = models.CharField(max_length=300)
	file_name = models.CharField(max_length=300)
	creation_date = models.DateTimeField(default=timezone.now())	
	def __unicode__(self):  
		return self.first_name
	def __unicode__(self):  
		return self.last_name
	def __unicode__(self):
		return self.email_id
	def __unicode__(self):
		return self.college_name
	def __unicode__(self):
		return self.file_name

class userForm(forms.Form):	
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email_id = forms.EmailField(required=True)
	college_name = forms.CharField(required=True)

	class Meta():
		model = user_main
		fields = ('first_name', 'last_name', 'email_id', 'college_name')

 	def clean(self):
		cleaned_data = super(userForm, self).clean()
		first_name = cleaned_data.get("first_name")
		last_name = cleaned_data.get("last_name")
		email_id = cleaned_data.get("email_id")		
		college_name = cleaned_data.get("college_name")		
		
		try:
		  if first_name and last_name and email_id and college_name:
		     if not re.match(r'^[a-zA-Z]*$', first_name):
		   	msg = "Name should have only characters."
			self._errors["first_name"] = self.error_class([msg])						
			del cleaned_data["first_name"]
		     elif not re.match(r'^[a-zA-Z]*$', last_name):
		   	msg = "Name should have only characters."
			self._errors["last_name"] = self.error_class([msg])						
			del cleaned_data["last_name"]
		     elif not re.match(r'^[a-zA-Z][a-zA-Z\s]*[A-Za-z]+$', college_name):
			msg = "College Name should have only characters."
			self._errors["college_name"] = self.error_class([msg])
			del cleaned_data["college_name"]
		     #elif not validate_email(email):
		     #	msg = "Enter a valid email."
		     #	self._errors["email"] = self.error_class([msg])
		     # 	del cleaned_data["email"]
		     #elif User.objects.exclude(pk=self.instance.pk).filter(models.Q(username=username) | models.Q(email=email)).exists():
		     #	msg = "Username/Email already in use."
		     #	self._errors["username"] = self.error_class([msg])
		     #	del cleaned_data["username"]
		     #	del cleaned_data["email"]
		#else:
		#	user = User.objects.create_user(first_name = first_name,
		#					last_name = last_name,
		#					username = username, 
		#					email = email, 		
		#					password = password )
		except Exception as e:
			msg = "Please enter valid details."
			self._errors["first_name"] = self.error_class([msg])	
			del cleaned_data["first_name"]
			del cleaned_data["last_name"]
			del cleaned_data["college_name"]	
		return cleaned_data
		
class authorForm(userForm):
	file = forms.FileField()
