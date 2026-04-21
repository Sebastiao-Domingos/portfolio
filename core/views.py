from django.shortcuts import render, redirect
from django.contrib import messages
from django.templatetags.static import static
from .forms import ContactForm
from .data import experencies, journeys_cards,courses, education
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
    return render(request, 'projetos.html')

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
    cv_data = {
        "name": "Sebastião Afonso Domingos",
        "contact": {
            "email": "domingossebastiao380@gmail.com",
            "phone": "+244 928 572 013 / +244 958 199 107",
            "location": "Rangel, Luanda / Angola",
            "linkedin": "Sebastião Domingos"
        },
        "profile": {
            "data_pt": "Sou um profissional de TI especializado em desenvolvimento web e tecnologias de networking, com uma forte background em sistemas de armazenamento. Apaixonado por resolver desafios e aprendizagem contínua, estou comprometido em melhorar meu conhecimento técnico e contribuir para projetos tecnológicos inovadores.",
            "data_en": "I am an IT professional specializing in web development and networking technologies, with a strong background in storage systems. Passionate about solving challenges and continuous learning, I am committed to improving my technical knowledge and contributing to innovative technological projects."
        },
        "profile_extra": {
            "data_pt": "Tenho uma forte paixão por programação, networking e soluções de armazenamento empresarial, que contribuíram significativamente para meu crescimento pessoal e profissional.",
            "data_en": "I have a strong passion for programming, networking, and enterprise storage solutions, which have greatly contributed to my personal and professional growth."
        },
        "experiences": [
            {
                "title": {"data_pt": "Desenvolvedor Full-stack – Projeto SIGUL", "data_en": "Full-stack Developer – SIGUL Project"},
                "company": {"data_pt": "Universidade de Luanda (Projeto Final) · 2025 – 2026", "data_en": "Universidade de Luanda (Final Year Project) · 2025 – 2026"},
                "bullets": [
                    {
                        "label": {"data_pt": "Desenvolvimento SIGUL", "data_en": "SIGUL Development"},
                        "body": {"data_pt": "Construiu Sistema de Gestão Integrado da Uniluanda, um sistema integrado de gestão para operações universitárias.", "data_en": "Built Sistema de Gestão Integrado da Uniluanda, an integrated management system for university operations."}
                    },
                    {
                        "label": {"data_pt": "Stack de Tecnologias", "data_en": "Tech Stack"},
                        "body": {"data_pt": "Next.js (frontend), Node.js + Express (backend), TypeORM (gestão de base de dados).", "data_en": "Next.js (frontend), Node.js + Express (backend), TypeORM (database management)."}
                    },
                    {
                        "label": {"data_pt": "Arquitetura Full-stack", "data_en": "Full-stack Architecture"},
                        "body": {"data_pt": "Projetou e implementou recursos completos de ponta a ponta para integração de sistema.", "data_en": "Designed and implemented complete end-to-end features for system integration."}
                    }
                ]
            },
            {
                "title": {"data_pt": "Desenvolvedor Front-end Mid-level", "data_en": "Mid-level Front-end Developer"},
                "company": {"data_pt": "Empresa DunorteJPP · 2023 – 2024", "data_en": "DunorteJPP Company · 2023 – 2024"},
                "bullets": []
            },
            {
                "title": {"data_pt": "Estagiário de Intervenção de Campo", "data_en": "Field Intervention Intern"},
                "company": {"data_pt": "Dell Technologies (via OMNIData) · 2025 – 2026", "data_en": "Dell Technologies (via OMNIData) · 2025 – 2026"},
                "bullets": [
                    {
                        "label": {"data_pt": "Dell Unity", "data_en": "Dell Unity"},
                        "body": {"data_pt": "Substituiu discos, configurou e manteve sistemas de armazenamento unificado.", "data_en": "Replaced disks, configured, and maintained unified storage systems."}
                    },
                    {
                        "label": {"data_pt": "Dell Data Domain", "data_en": "Dell Data Domain"},
                        "body": {"data_pt": "Substituiu discos, monitorou e otimizou soluções de backup e proteção de dados.", "data_en": "Replaced disks, monitored, and optimized backup & data protection solutions."}
                    },
                    {
                        "label": {"data_pt": "PowerMax", "data_en": "PowerMax"},
                        "body": {"data_pt": "Operou e gerenciou sistemas de armazenamento usando Unity para PowerMax.", "data_en": "Operated and managed storage systems using Unity for PowerMax."}
                    },
                    {
                        "label": {"data_pt": "Gestão de Projetos e Serviços", "data_en": "Project & Service Management"},
                        "body": {"data_pt": "Estudou e praticou metodologias de gestão de projetos e gestão de serviços de TI.", "data_en": "Studied and practiced project management and IT service management methodologies."}
                    }
                ]
            },
            {
                "title": {"data_pt": "Estagiário de Suporte de TI", "data_en": "IT Support Intern"},
                "company": {"data_pt": "Universidade de Luanda – INSTIC · 4 meses", "data_en": "Universidade de Luanda – INSTIC · 4 months"},
                "bullets": [
                    {
                        "label": {"data_pt": "Suporte de TI", "data_en": "IT Support"},
                        "body": {"data_pt": "Forneceu suporte de TI em toda a instituição, resolvendo problemas de rede e conectividade à internet.", "data_en": "Provided IT support across the entire institution, resolving network issues and internet connectivity problems."}
                    },
                    {
                        "label": {"data_pt": "Gestão de Sistemas", "data_en": "System Management"},
                        "body": {"data_pt": "Monitorou e manteve sistemas de PC e infraestrutura.", "data_en": "Monitored and maintained PC systems and infrastructure."}
                    }
                ]
            }
        ],
        "education": [
            {
                "title": {"data_pt": "Engenharia de Computadores", "data_en": "Computer Engineering"},
                "institution": "Universidade de Luanda – INSTIC",
                "period": {"data_pt": "Concluído 2026", "data_en": "Graduated 2026"},
                "bullets": [
                    {"data_pt": "Participante em AOCPC (Angola Collegiate Programming Contest) 2022", "data_en": "Participant in AOCPC (Angola Collegiate Programming Contest) 2022"},
                    {"data_pt": "Huawei Seeds for the Future 2025 – Equipa premiada com 3º lugar geral", "data_en": "Huawei Seeds for the Future 2025 – Team awarded 3rd place overall"},
                    {"data_pt": "Estágio na OMNIData (2025–2026)", "data_en": "Internship at OMNIData (2025–2026)"}
                ]
            }
        ],
        "huawei_tags": [
            "5G Technologies", "Artificial Intelligence", "Cloud Computing",
            "Digital Power", "Leadership & Cross-Cultural Communication"
        ],
        "certifications": [
            "Dell Technologies – Information Storage & Management (ISM)",
            "Dell Unity Deploy 2023 (D-UN-DE-23)",
            "PowerMax-Operate-Version 2 (D-PVM-OE-01)"
        ],
        "technical_courses": [
            "CCNA 1–3 (Cisco Certified Network Associate)",
            "Web Programming",
            "ISC2 – Cybersecurity"
        ],
        "languages": [
            {"name": "Portuguese", "level": {"data_pt": "Nativo", "data_en": "Native"}, "pct": 100},
            {"name": "English", "level": {"data_pt": "Básico–Intermédio", "data_en": "Basic–Intermediate"}, "pct": 55}
        ],
        "hard_skills": [
            "HTML / CSS / JS", "Next.js", "Node.js", "Express", "TypeORM",
            "Networking", "Dell Unity", "Data Domain", "PowerMax",
            "Storage Systems", "CCNA", "Cybersecurity", "Cloud Computing"
        ],
        "soft_skills": [
            {"data_pt": "Resolução de Problemas", "data_en": "Problem Solving"},
            {"data_pt": "Liderança", "data_en": "Leadership"},
            {"data_pt": "Comunicação", "data_en": "Communication"},
            {"data_pt": "Trabalho em Equipa", "data_en": "Teamwork"},
            {"data_pt": "Adaptabilidade", "data_en": "Adaptability"},
            {"data_pt": "Gestão do Tempo", "data_en": "Time Management"}
        ]
    }

    return render(request, 'cv.html', {'cv': cv_data})
