from django.db import models
from datetime import datetime
from datetime import timedelta
# Create your models here.

class Admin(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=45)  # Field name made lowercase.
    accountno = models.CharField(db_column='Accountno', max_length=45, null=True)  # Field name made lowercase.
    accountholdername = models.CharField(db_column='Accountholdername', max_length=45, null=True)  # Field name made lowercase.



class Adminpaid(models.Model):
    adminidf = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminidf', blank=True, null=True)
    pmidf = models.ForeignKey('Pm', models.DO_NOTHING, db_column='pmidf', blank=True, null=True)
    time = models.CharField(max_length=45, null=True)
    id = models.CharField(primary_key=True, max_length=45)

class Commission(models.Model):
    productidf = models.ForeignKey('Product', models.DO_NOTHING, db_column='productidf', blank=True, null=True)
    orderno = models.CharField(db_column='Orderno', max_length=45, primary_key=True)
    pmmidf = models.ForeignKey('Pmm', models.DO_NOTHING, db_column='pmmidf', blank=True, null=True)
    date = models.DateField(db_column='Date')
    paypal = models.CharField(db_column='Paypal', max_length=45 )
    commissionnn = models.IntegerField(db_column='Commision') 


class Order(models.Model):
    orderno = models.CharField(primary_key=True, max_length=45)
    status = models.CharField(max_length=45, null=True)
    paypal = models.CharField(max_length=45)
    orderimage = models.ImageField(blank=True ,null=True, upload_to= 'ordersimages')  # Field name made lowercase.
    Reviewimage = models.ImageField(blank=True ,null=True, upload_to= 'reviewimages')
    Refundimage = models.ImageField(blank=True ,null=True, upload_to= 'refundimages') # Field name made lowercase.
    pmidf = models.ForeignKey('Pm', models.DO_NOTHING, db_column='pmidf', blank=True, null=True)
    pmmidf = models.ForeignKey('Pmm', models.DO_NOTHING, db_column='pmmidf', blank=True, null=True)
    productidf = models.ForeignKey('Product', models.DO_NOTHING, db_column='productidf', blank=True, null=True)

class Pm(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno',  null=True, max_length=20)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=45)  # Field name made lowercase.
    accno = models.CharField(db_column='Accno', max_length=45)  # Field name made lowercase.
    accholdername = models.CharField(db_column='Acchodername', max_length=45, null=True)  # Field name made lowercase.


class Pmm(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno',  null=True, max_length=11) # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=45)  # Field name made lowercase.
    accno = models.CharField(db_column='Accno', max_length=45)  # Field name made lowercase.
    accholdername = models.CharField(db_column='Accholdername', max_length=45)  # Field name made lowercase.

class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='Keyword', max_length=45)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=45)  # Field name made lowercase.
    store = models.CharField(db_column='Store', max_length=45)  # Field name made lowercase.
    commissionn = models.IntegerField(db_column='Commissionn', null=True)  # Field name made lowercase.
    totalquantity = models.IntegerField(db_column='Totalquantity')  # Field name made lowercase.
    dailylimit = models.IntegerField(db_column='Dailylimit')  # Field name made lowercase.
    type = models.CharField(max_length=45)
    country = models.CharField(max_length=15, null=True)
    image = models.ImageField(blank=True ,null=True, upload_to= 'productimages') 

class Pmmreservation(models.Model):
    rid = models.IntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    duration = models.TimeField(db_column='Duration')
    image = models.ImageField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=45, blank=True, null=True)
    store = models.CharField(max_length=45, blank=True, null=True)
    commissionn = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    pmmidf = models.ForeignKey(Pmm, models.DO_NOTHING, db_column='PMMidf', blank=True, null=True)  # Field name made lowercase.
    productidf = models.ForeignKey('Product', models.DO_NOTHING, db_column='Productidf', blank=True, null=True)  # Field name made lowercase.
    keywordd = models.CharField(db_column='keyword', max_length=45, blank=True, null=True)





