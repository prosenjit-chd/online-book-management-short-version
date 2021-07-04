from django.forms import ModelForm
from .models import *


class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = '__all__'


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class RentForm(ModelForm):
	class Meta:
		model = Rent
		fields = '__all__'