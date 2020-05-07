from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from post.models import Post

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


class CreateNewPost(ModelForm):
	class Meta:
		model = Post
		fields =['job','workplace','address','worktime','salary','description']
	
class LogInForm(forms.Form):
	username = forms.CharField(max_length=255)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
