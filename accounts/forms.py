from django import forms

class teamForm(forms.Form):
	pname = forms.CharField();
	tname = forms.CharField();
	pnum = forms.IntegerField();