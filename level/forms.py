from django import forms


class DateForm(forms.Form):
    start_date = forms.DateField(input_formats=['%Y-%m-%d'], label="Начальная дата")
    last_date = forms.DateField(input_formats=['%Y-%m-%d'], label="Конечная дата")

    def __init__(self, *args, **kwargs):
        super(DateForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update({'class': 'form-control start-date'})
        self.fields['last_date'].widget.attrs.update({'class': 'form-control last-date'})


class ImportFileForm(forms.Form):
    choices = [
        ('1', 'первый'),
        ('2', 'второй'),
        ('3', 'третий'),
        ('4', 'четвертый')
    ]
    choiceMachine = forms.ChoiceField(choices=choices, label="Выбери номер станка")
    importFile = forms.FileField(label="Загрузи файл с данным")
