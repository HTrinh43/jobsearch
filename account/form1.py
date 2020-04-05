from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

	def clean(self):
		cleaned_data = super(RegisterForm, self).clean()
		email = cleaned_data.get('email')

		try:
			user = User.objects.get(email=email)		
			msg = "Email is already used"
			self.add_error('email', msg)
		except:
			pass


class CreateNewPost(forms.Form):
	job = forms.CharField(label="Job Name",max_length=255)
	workplace = forms.CharField(label='Workplace', max_length=255)
	fulltime = forms.BooleanField(label='Full Time', required=False)
	parttime = forms.BooleanField(label='Part Time', required=False)
	address = forms.CharField(label='Address')
	salary = forms.IntegerField(label='Salary')
	description = forms.CharField(label='Description', required=False)
	
class LogInForm(forms.Form):
	username = forms.CharField(max_length=255)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)