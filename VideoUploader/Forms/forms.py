from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=15, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    clave = forms.CharField(label='clave', required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Clave', 'type': 'password'}))


class UploadForm(forms.Form):

    titulo = forms.CharField(label='titulo', required=True,
                               widget=forms.TextInput(attrs={'id' : 'titulo', 'class': 'form-control', 'placeholder': 'Titulo'}))

    tags = forms.CharField(label='Post Tags', required=True,
                           widget=forms.TextInput(attrs={'id' : 'tags', 'class': 'form-control', 'placeholder': 'Tags'}))

    video = forms.CharField(label='Video', required=True,
                               widget=forms.FileInput(attrs={ 'id': 'video', 'class': 'form-control file', 'placeholder': 'Video'}))

    descripcion = forms.CharField(label="Descripcion", required=False,
                                  widget=forms.Textarea(attrs={ 'id' : 'descripcion', 'class': 'form-control',
                                                                'placeholder': 'Pequeña reseña del video', 'rows': '4'}))

    privado = forms.CharField(label="privado", required=False,
                              widget=forms.TextInput(attrs={'class': 'checkbox', 'type': 'checkbox',
                                                                             'id': 'privado'}))

    usuarios = forms.CharField(label='usuarios', required=False,
                               widget=forms.Textarea(attrs={'id' : 'usuarios' ,'class': 'form-control usuarios-permitidos hidden',
                                                            'placeholder': 'Usernames de los usuarios permitidos.',
                                                            'name': 'usuarios', 'rows': '1'}))

    thumbnail = forms.CharField(label='thumbnail', required=False,
                           widget=forms.FileInput(attrs={'class': 'form-control file'}))

