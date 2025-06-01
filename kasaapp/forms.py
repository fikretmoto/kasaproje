from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['tarih', 'aciklama', 'tutar', 'islem_turu']
        widgets = {
            'tarih': forms.DateInput(attrs={'type': 'date'}),
            'aciklama': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'tarih': 'Tarih',
            'aciklama': 'Açıklama',
            'tutar': 'Tutar (TL)',
            'islem_turu': 'İşlem Türü',
        }