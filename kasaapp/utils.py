# kasaapp/utils.py

from .models import Transaction
from django.db.models import Sum
from datetime import date, timedelta

def gun_sonu_bakiye_hesapla(tarih: date):
    """
    Verilen tarihteki kasa işlemlerine göre bakiye hesaplar.
    """
    toplam_gelir = Transaction.objects.filter(
        tarih=tarih, islem_turu='L'
    ).aggregate(Sum('tutar'))['tutar__sum'] or 0

    toplam_gider = Transaction.objects.filter(
        tarih=tarih, islem_turu='G'
    ).aggregate(Sum('tutar'))['tutar__sum'] or 0

    onceki_gun = tarih - timedelta(days=1)
    onceki_devir = Transaction.objects.filter(
        tarih=onceki_gun, islem_turu='D'
    ).aggregate(Sum('tutar'))['tutar__sum'] or 0

    bakiye = onceki_devir + toplam_gelir - toplam_gider
    return bakiye

# kasaapp/utils.py içine ekleyebilirsin

def gun_sonu_devir_ekle(tarih: date):
    bakiye = gun_sonu_bakiye_hesapla(tarih)
    ertesi_gun = tarih + timedelta(days=1)

    # Aynı tarihe daha önce devir eklenmiş mi kontrol et
    if not Transaction.objects.filter(tarih=ertesi_gun, islem_turu='D').exists():
        Transaction.objects.create(
            tarih=ertesi_gun,
            aciklama="Otomatik gün sonu devir",
            tutar=bakiye,
            islem_turu='D'
        )
        return True
    return False
