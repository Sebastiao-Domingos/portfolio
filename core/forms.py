from django import forms
from .models import Contact   # Corrigido: import correto

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
        # Estilização completa com Tailwind
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full mt-3 px-4 py-3 bg-white border border-slate-300 rounded-2xl '
                        'focus:outline-none focus:border-teal-600 focus:ring-4 focus:ring-teal-100 '
                        'transition-all duration-300 placeholder-slate-400 translatable',
                'placeholder': 'O teu nome completo',"data-pt": "O teu nome completo", "data-en": "Your full name",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full mt-3 px-4 py-3 bg-white border border-slate-300 rounded-2xl '
                        'focus:outline-none focus:border-teal-600 focus:ring-4 focus:ring-teal-100 '
                        'transition-all duration-300 placeholder-slate-400 translatable',
                'placeholder': 'O teu endereço de email', "data-pt": "O teu endereço de email", "data-en": "Your email address",
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full mt-3 px-4 py-3 bg-white border border-slate-300 rounded-3xl '
                        'focus:outline-none focus:border-teal-600 focus:ring-4 focus:ring-teal-100 '
                        'transition-all duration-300 placeholder-slate-400 resize-y min-h-[160px]',
                'placeholder': 'Escreve a tua mensagem aqui...', "data-pt": "Escreve a tua mensagem aqui...", "data-en": "Write your message here...",
                'rows': 6,
            }),
        }

    # Labels mais bonitas (opcional mas recomendado)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome Completo"
        self.fields['email'].label = "Email"
        self.fields['message'].label = "Mensagem"

