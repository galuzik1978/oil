from django import forms

class DateForm(forms.Form):
    start_date = forms.DateField(input_formats=['%d/%m/%Y'])
    last_date = forms.DateField(input_formats=['%d/%m/%Y'])