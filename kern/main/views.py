from django.shortcuts import render
from .models import kern_db, kern_db_2, acc_kern_db, acc_kern_not_stat
from plotly.offline import plot
import plotly.graph_objects as go

def index(request):
    code = request.GET.get('code')
    if code is None:
        code=""
    dlina_gr=request.GET.get('dlina_gr')
    if dlina_gr is None:
        dlina_gr=''
    dlina_ls=request.GET.get('dlina_ls')
    if dlina_ls is None:
        dlina_ls=''
    kern=kern_db.objects.all()

    if code != '' and code is not None:
        kern=kern.filter(Код=code)

    if dlina_gr !='' and dlina_gr is not None:
        kern=kern.filter(Длина_см__gt=dlina_gr)

    if dlina_ls !='' and dlina_ls is not None:
        kern=kern.filter(Длина_см__lt=dlina_ls)

    context={
        'kern':kern,
        'code':code,
        'dlina_gr':dlina_gr,
        'dlina_ls':dlina_ls
    }

    return render(request, 'main/index.html', context)

def kern_graph(request):
    labels=[]
    data=[]
    query=kern_db.objects.all()
    for el in query:
        labels.append(el.Длина_см)
        data.append(el.Газопроницаемость_стац_мД)
    return render(request, 'main/kern_chart.html', {
        'labels': labels,
        'data': data,
    })
    return render(request, 'main/kern_chart.html',context)

def kern2(request):
    kern2=kern_db_2.objects.all()[:50]
    return render(request,'main/kern_2.html',{'kern2':kern2})

def acc(request):
    acc=acc_kern_db.objects.all()
    return render(request, 'main/acc.html',{'acc':acc})

def acc2(request):
    num = request.GET.get('ff')
    acc = acc_kern_db.objects.all()
    acc1= acc.filter(num_Образца=num)
    acc2=acc_kern_not_stat.objects.filter(num_Образца=num)


    context = {
        'acc2':acc2,
        'acc':acc,
        'acc1':acc1
    }
    return render(request, 'main/acc2.html', context)
