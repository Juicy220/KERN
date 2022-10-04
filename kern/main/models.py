from django.db import models

class kern_db(models.Model):
    Код=models.IntegerField(primary_key=True)
    Дата=models.DateField()
    Недропользователь_ДО=models.FloatField()
    Месторождение=models.FloatField()
    Скважина=models.FloatField()
    образца=models.IntegerField()
    Глубина_отбора_м=models.FloatField()
    Длина_см=models.FloatField()
    Диаметр_см=models.FloatField()
    Объем_пор_см3=models.FloatField()
    Пористость=models.FloatField()
    Газопроницаемость_мД=models.FloatField()
    Газопроницаемость_Кл_мД=models.FloatField()
    Газопроницаемость_стац_мД=models.FloatField()
    Масса_образца_гр=models.FloatField()
    Эксперимент=models.TextField()
    Результат_эксперимента_да_нет=models.TextField()
    Томография_да_нет=models.TextField()

    class Meta:
        managed = False
        db_table = 'kern_db'

class kern_db_2(models.Model):
    SourceName=models.TextField(primary_key=True)
    Sample=models.TextField()
    Date=models.TextField()
    Time=models.TextField()
    Length=models.FloatField()
    Diam=models.FloatField()
    V_bulk=models.FloatField()
    V_grain=models.FloatField()
    Weight=models.FloatField()
    GrDens=models.FloatField()
    Depth=models.FloatField()
    P_conf=models.FloatField()
    V_pore=models.FloatField()
    Porosity=models.FloatField()
    K_air=models.FloatField()
    K_klink=models.FloatField()
    Slip=models.FloatField()
    Alpha=models.FloatField()
    Beta=models.FloatField()

    class Meta:
        managed = False
        db_table = 'kern_db_2'

class acc_kern_db(models.Model):
    Код=models.IntegerField(primary_key=True)
    Дата=models.TextField()
    Недропользователь_ДО=models.TextField()
    Месторождение=models.FloatField()
    Скважина=models.FloatField()
    num_Образца=models.FloatField()
    Длина_см=models.FloatField()
    Диаметр_см=models.FloatField()
    Масса_сух_гр=models.FloatField()
    Кг_Кл_не_стационарный_мД=models.FloatField()
    Кг_стационарный_мД=models.FloatField()
    Пористость=models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_kern_db'
