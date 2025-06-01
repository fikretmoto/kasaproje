from django.db import models

# Create your models here.


class Transaction(models.Model):
    TÜR_CHOICES = (
        ('GELİR', 'Gelir'),
        ('GİDER', 'Gider'),
        ('DEVİR', 'Gün Sonu Devir'),
    )

    tarih = models.DateField()
    aciklama = models.TextField()
    tutar = models.DecimalField(max_digits=10, decimal_places=2)
    islem_turu = models.CharField(max_length=10, choices=TÜR_CHOICES)

    def __str__(self):
        return f"{self.tarih} - {self.aciklama} ({self.tutar} TL)"
