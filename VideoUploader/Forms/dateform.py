from django import forms


class dateForm(forms.Form):
    from_ = forms.DateField(label='Fromdate',  required=True,
                               widget=forms.DateField(attrs={'class': 'form-control', 'placeholder': 'FromDate'}))
    to = forms.DateField(label='Todate', required=True,
                            widget=forms.DateField(attrs={'class': 'form-control', 'placeholder': 'ToDate'}))

