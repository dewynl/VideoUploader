from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from zeep import Client

from VideoUploader.Forms.forms import LoginForm, UploadForm

url = "http://localhost:7777/ws/VideoWebService?wsdl"
client = Client(url)

@csrf_exempt
def index(request):
    if request.method == 'GET':
        template = loader.get_template('home.html')
        return HttpResponse(template.render({},request))

@csrf_exempt
def login(request):
    if request.method == 'GET':
        if 'sessionUsername' not in request.session:
            template = loader.get_template("log-in.html")
            form = LoginForm()
            return HttpResponse(template.render({"form": form}, request))
        else:
            del request.session['sessionUsername']
            return HttpResponseRedirect("/")
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.data.get("username")
            clave = form.data.get("clave")
            logged = client.service.logInClient(usuario, clave)
            print(logged)
            if logged:
                request.session['sessionUsername'] = usuario
                return HttpResponseRedirect("/uploadVideo")
            else:
                return HttpResponse("Credenciales no válidos")


@csrf_exempt
def uploadVideo(request):
    if 'sessionUsername' in request.session:
        if request.method == 'GET':
            form = UploadForm()
            template = loader.get_template("upload-page.html")
            return HttpResponse(template.render({"form": form}), request)
        elif request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                titulo = form.data.get("titulo")
                tags = form.data.get("tags")
                video = request.FILES['video']
                descripcion = form.data.get('descripcion')
                privado = form.data.get('privado')
                usuarios = None
                if privado == 'on':
                    usuarios = privado = form.data.get('usuarios')
                thumbnail = request.FILES['thumbnail']

                ok = client.service.uploadVideo(titulo, tags, video.temporary_file_path(), descripcion, privado,
                                                        usuarios, thumbnail.temporary_file_path())
                if ok:
                    return HttpResponse("El video se subio jevi.")
                else:
                    return HttpResponse("No se ha podido subir el video")
            else:
                return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")