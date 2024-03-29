from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from zeep import Client

from VideoUploader.Forms.forms import LoginForm, UploadForm, dateForm
from VideoUploader import services

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
                return HttpResponseRedirect("/home")
            else:
                return HttpResponse("Credenciales no válidos")

@csrf_exempt
def uploadVideo(request):
    print(request.session['sessionUsername'])
    if 'sessionUsername' in request.session:
        if request.method == 'GET':
            form = UploadForm()
            template = loader.get_template("upload-page.html")
            return HttpResponse(template.render({"form": form, 'usuario' : request.session['sessionUsername']}), request)
        elif request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            form = UploadForm(request.POST, request.FILES)
            #if form.is_valid():
            titulo = form.data.get("titulo")
            tags = form.data.get("tags")
            video = request.FILES['video']
            descripcion = form.data.get('descripcion')
            privado = form.data.get('privado')
            usuarios = None
            if privado == 'on':
                usuarios = privado = form.data.get('usuarios')
            thumbnail = request.FILES['thumbnail']

            print(video.read())

            ok = client.service.uploadVideo(titulo, tags, video.read(), descripcion, privado,
                                                    usuarios, thumbnail.temporary_file_path())
            if ok:
                print("Se subió el video.")
                return HttpResponse("/home/")
            else:
                return HttpResponse("No se ha podido subir el video")
           # else:
            #    messages.error(request, "Error")
            #    return HttpResponse("Form no válido")
    else:
        return HttpResponseRedirect("/home/")

@csrf_exempt
def home(request):
    global form
    usuario = None
    videos_list = []
    template = loader.get_template("home-page.html")
    if request.method == 'POST':
        form = dateForm(request.POST)
        FROM = form.data.get("fromDate")
        TO = form.data.get("toDate")
        videos_list = services.get_videos(FROM, TO)
    elif request.method == 'GET':
        form = dateForm()

    if 'sessionUsername' in request.session:
        usuario = request.session['sessionUsername']

    return HttpResponse(template.render({'videos' : videos_list, 'form' : form,
                                         'usuario' : usuario, 'home' : True}, request))

@csrf_exempt
def ver(request, id):
    template = loader.get_template("watch-page.html")
    video = services.get_video(id)
    return HttpResponse(template.render({'video' : video}, request))