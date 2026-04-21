from django.shortcuts import render, redirect
from django.contrib import messages
from django.templatetags.static import static
from .forms import ContactForm
from .data import experencies, journeys_cards,courses, education, projects, data_cv
import json

def home(request):
    journey_cards = journeys_cards.journeys_cards()
    return render(request, 'home.html' , {'journey_cards': journey_cards}) 

def experiencia(request):

    experiences = experencies.data_experiences()
    return render(request, 'experiencia.html', {'experiences': experiences})

def formacao(request):

    educations_raw = education.educations_final()

    educations = []
    for edu in educations_raw:
        edu["conquistas_json"] = json.dumps(edu["conquistas"], ensure_ascii=False)
        edu["projetos_json"]   = json.dumps(edu["projetos"],   ensure_ascii=False)
        edu["certificado_pdf_url"] = static(edu["certificado_pdf"]) if edu["certificado_pdf"] else ""
        edu["historico_pdf_url"]   = static(edu["historico_pdf"])   if edu["historico_pdf"]   else ""
        educations.append(edu)

    return render(request, 'formacao.html', {'educations': educations})


def cursos(request):
    coursess = courses.courses()
    return render(request, 'cursos.html' , {'courses': coursess})


def projetos(request):
    projec = projects.projects()
    return render(request, 'projetos.html', {'projects': projec})


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def cv(request):
    return render(request, 'cv.html')


# views.py

def cv_view(request):

    return render(request, 'cv.html', {'cv': data_cv.data_cv()})
