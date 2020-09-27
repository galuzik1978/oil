from django import forms


class DateForm(forms.Form):
    start_date = forms.DateField(input_formats=['%Y-%m-%d'])
    last_date = forms.DateField(input_formats=['%Y-%m-%d'])


class ImportFileForm(forms.Form):
    choices = [
        ('1', 'первый'),
        ('2', 'второй'),
        ('3', 'третий'),
        ('4', 'четвертый')
    ]
    choiceMachine = forms.ChoiceField(choices=choices, label="Выбери номер станка")
    importFile = forms.FileField(label="Загрузи файл с данным")
