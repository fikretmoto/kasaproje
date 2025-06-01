from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .utils import gun_sonu_devir_ekle
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth import authenticate, login, logout

@login_required
def gun_sonu_devir_view(request):
    bugun = timezone.now().date()

    if request.method == 'POST':
        if gun_sonu_devir_ekle(bugun):
            messages.success(request, f"{bugun} tarihli gün sonu devir işlemi başarıyla eklendi.")
        else:
            messages.warning(request, f"{bugun + timezone.timedelta(days=1)} tarihli devir zaten var.")
        return redirect('gun_sonu_devir')

    return render(request, 'kasaapp/gun_sonu_devir.html', {'tarih': bugun})

@login_required
def transaction_list_view(request):
    islemler = Transaction.objects.order_by('-tarih', '-id')
    return render(request, 'kasaapp/islem_listesi.html', {'islemler': islemler})

@login_required
def islem_ekle_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "İşlem başarıyla kaydedildi.")
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'kasaapp/islem_ekle.html', {'form': form})

@login_required
def kasa_durumu(request):
    gelir = Transaction.objects.filter(islem_turu='GELİR').aggregate(total=Sum('tutar'))['total'] or 0
    gider = Transaction.objects.filter(islem_turu='GİDER').aggregate(total=Sum('tutar'))['total'] or 0
    bakiye = gelir - gider
    return render(request, 'kasaapp/kasa_durumu.html', {
        'gelir': gelir,
        'gider': gider,
        'bakiye': bakiye,
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('transaction_list')  # Zaten giriş yaptıysa yönlendir

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('transaction_list')  # Giriş başarılıysa
        else:
            messages.error(request, "Kullanıcı adı veya şifre yanlış")

    return render(request, 'kasaapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')