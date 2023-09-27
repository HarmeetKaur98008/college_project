from django import forms
from .models import AddModel
from .models import UploadModel

class AddForm(forms.ModelForm):
	class Meta:
		model = AddModel
		fields = "__all__"

class UploadForm(forms.ModelForm):
	class Meta:
		model = UploadModel
		fields = "__all__"
