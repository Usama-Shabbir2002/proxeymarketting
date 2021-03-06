# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=45)  # Field name made lowercase.
    accountno = models.CharField(db_column='Accountno', max_length=45)  # Field name made lowercase.
    accountholdername = models.CharField(db_column='Accountholdername', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Adminpaid(models.Model):
    adminidf = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminidf', blank=True, null=True)
    pmidf = models.ForeignKey('Pm', models.DO_NOTHING, db_column='pmidf', blank=True, null=True)
    time = models.CharField(max_length=45)
    id = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'adminpaid'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Commission(models.Model):
    productidf = models.ForeignKey('Product', models.DO_NOTHING, db_column='productidf', blank=True, null=True)
    ordernof = models.ForeignKey('Order', models.DO_NOTHING, db_column='ordernof', blank=True, null=True)
    pmmidf = models.ForeignKey('Pmm', models.DO_NOTHING, db_column='pmmidf', blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'commission'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Order(models.Model):
    orderno = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=45)
    paypal = models.CharField(max_length=45)
    orderimage = models.CharField(max_length=45)
    reviewimage = models.CharField(db_column='Reviewimage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    refundimage = models.CharField(db_column='Refundimage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pmidf = models.ForeignKey('Pm', models.DO_NOTHING, db_column='pmidf', blank=True, null=True)
    pmmidf = models.ForeignKey('Pmm', models.DO_NOTHING, db_column='pmmidf', blank=True, null=True)
    productidf = models.ForeignKey('Product', models.DO_NOTHING, db_column='productidf', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Pm(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=45)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=45)  # Field name made lowercase.
    accno = models.CharField(db_column='Accno', max_length=45)  # Field name made lowercase.
    acchodername = models.CharField(db_column='Acchodername', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pm'


class Pmm(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=45)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=45)  # Field name made lowercase.
    accno = models.CharField(db_column='Accno', max_length=45)  # Field name made lowercase.
    accholdername = models.CharField(db_column='Accholdername', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmm'


class PmmAdmin(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=11)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=15)  # Field name made lowercase.
    accno = models.CharField(db_column='Accno', max_length=20)  # Field name made lowercase.
    accholdername = models.CharField(db_column='Accholdername', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmm_admin'


class PmmAdminpaid(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    adminidf = models.ForeignKey(PmmAdmin, models.DO_NOTHING, db_column='Adminidf', blank=True, null=True)  # Field name made lowercase.
    pmidf = models.ForeignKey('PmmPm', models.DO_NOTHING, db_column='PMidf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmm_adminpaid'


class PmmCommission(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordernof = models.ForeignKey('PmmOrder', models.DO_NOTHING, db_column='Ordernof', blank=True, null=True)  # Field name made lowercase.
    pmmidf = models.ForeignKey('PmmPmm', models.DO_NOTHING, db_column='Pmmidf', blank=True, null=True)  # Field name made lowercase.
    productidf = models.ForeignKey('PmmProduct', models.DO_NOTHING, db_column='Productidf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmm_commission'


class PmmOrder(models.Model):
    orderno = models.CharField(db_column='Orderno', primary_key=True, max_length=18)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paypal = models.CharField(db_column='Paypal', max_length=25)  # Field name made lowercase.
    pmidf = models.ForeignKey('PmmPm', models.DO_NOTHING, db_column='Pmidf', blank=True, null=True)  # Field name made lowercase.
    pmmidf = models.ForeignKey('PmmPmm', models.DO_NOTHING, db_column='Pmmidf', blank=True, null=True)  # Field name made lowercase.
    productidf = models.ForeignKey('PmmProduct', models.DO_NOTHING, db_column='Productidf', blank=True, null=True)  # Field name made lowercase.
    refundimage = models.CharField(db_column='Refundimage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reviewimage = models.CharField(db_column='Reviewimage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orderimage = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmm_order'


class PmmPm(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='Phonenumber', max_length=11)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=15)  # Field name made lowercase.
    accno = models.CharField(db_column='Accno', max_length=20)  # Field name made lowercase.
    accholdername = models.CharField(db_column='Accholdername', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmm_pm'


class PmmPmm(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    phoneno = models.CharField(db_column='Phoneno', max_length=11)  # Field name made lowercase.
    bankname = models.CharField(db_column='Bankname', max_length=15)  # Field name made lowercase.
    accno = models.CharField(db_column='Accno', max_length=20)  # Field name made lowercase.
    accholdername = models.CharField(db_column='Accholdername', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmm_pmm'


class PmmPmmreservation(models.Model):
    rid = models.IntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    image = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=45, blank=True, null=True)
    store = models.CharField(max_length=45, blank=True, null=True)
    commissionn = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    pmmidf = models.ForeignKey(PmmPmm, models.DO_NOTHING, db_column='PMMidf', blank=True, null=True)  # Field name made lowercase.
    productidf = models.ForeignKey('PmmProduct', models.DO_NOTHING, db_column='Productidf', blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmm_pmmreservation'


class PmmProduct(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='Keyword', max_length=45)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=15)  # Field name made lowercase.
    store = models.CharField(db_column='Store', max_length=15)  # Field name made lowercase.
    commissionn = models.IntegerField(db_column='Commissionn')  # Field name made lowercase.
    image = models.CharField(max_length=100, blank=True, null=True)
    totalquantity = models.IntegerField(db_column='TotalQuantity')  # Field name made lowercase.
    dailylimit = models.IntegerField(db_column='Dailylimit')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    country = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmm_product'


class Product(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='Keyword', max_length=45)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=45)  # Field name made lowercase.
    store = models.CharField(db_column='Store', max_length=45)  # Field name made lowercase.
    commission = models.IntegerField(db_column='Commission')  # Field name made lowercase.
    totalquantity = models.IntegerField(db_column='Totalquantity')  # Field name made lowercase.
    dailylimit = models.IntegerField(db_column='Dailylimit')  # Field name made lowercase.
    type = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    image = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'product'


class ProductsBoat(models.Model):
    bid = models.IntegerField(db_column='Bid', primary_key=True)  # Field name made lowercase.
    bname = models.CharField(db_column='Bname', max_length=15, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_boat'


class Resrvation(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    pmmidf = models.ForeignKey(Pmm, models.DO_NOTHING, db_column='Pmmidf', blank=True, null=True)  # Field name made lowercase.
    productidf = models.ForeignKey(Product, models.DO_NOTHING, db_column='productidf', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resrvation'
