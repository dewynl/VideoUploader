from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from zeep import Client

from VideoUploader.Forms.LoginForm import LoginForm, UploadForm

url = "http://localhost:7777/ws/AcademicoWebService?wsdl"
client = Client(url)


def index(request):
    template = loader.get_template("log-in.html")
    form = LoginForm()
    return HttpResponse(template.render({"form": form}, request))


@csrf_exempt
def authenticate(request):
    ok = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.data.get("username")
            clave = form.data.get("clave")
            ok = client.service.logInClient(usuario, clave)
            print(ok)
    if ok:
        return HttpResponseRedirect("/uploadVideo")
    else:
        return HttpResponse("Credenciales no válidos")


@csrf_exempt
def uploadVideo(request):

    if request.method == 'GET':
        form = UploadForm()
        template = loader.get_template("upload-page.html")
        return HttpResponse(template.render({"form" : form}), request)
    elif request.method == 'POST':
        print(request.POST)
        form = UploadForm(request.POST)
        if form.is_valid():
            titulo = form.data.get("titulo")
            tags = form.data.get("tags")
            video = form.data.get("video")
            descripcion = form.data.get('descripcion')
            privado = form.data.get('privado')
            thumbnail = form.data.get('thumbnail')

            return HttpResponse("Validongo")
        else:
            return HttpResponse("No validongo")