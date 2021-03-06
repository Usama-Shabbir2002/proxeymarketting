# Generated by Django 4.0.2 on 2022-04-23 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('phone', models.CharField(db_column='Phone', max_length=45, null=True)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('bankname', models.CharField(db_column='Bankname', max_length=45)),
                ('accountno', models.CharField(db_column='Accountno', max_length=45, null=True)),
                ('accountholdername', models.CharField(db_column='Accountholdername', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pm',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('phoneno', models.CharField(db_column='Phoneno', max_length=20, null=True)),
                ('bankname', models.CharField(db_column='Bankname', max_length=45)),
                ('accno', models.CharField(db_column='Accno', max_length=45)),
                ('accholdername', models.CharField(db_column='Acchodername', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pmm',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('phoneno', models.CharField(db_column='Phoneno', max_length=11, null=True)),
                ('bankname', models.CharField(db_column='Bankname', max_length=45)),
                ('accno', models.CharField(db_column='Accno', max_length=45)),
                ('accholdername', models.CharField(db_column='Accholdername', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('keyword', models.CharField(db_column='Keyword', max_length=45)),
                ('brand', models.CharField(db_column='Brand', max_length=45)),
                ('store', models.CharField(db_column='Store', max_length=45)),
                ('commissionn', models.IntegerField(db_column='Commissionn', null=True)),
                ('totalquantity', models.IntegerField(db_column='Totalquantity')),
                ('dailylimit', models.IntegerField(db_column='Dailylimit')),
                ('type', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=15, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='productimages')),
            ],
        ),
        migrations.CreateModel(
            name='Pmmreservation',
            fields=[
                ('rid', models.IntegerField(db_column='RID', primary_key=True, serialize=False)),
                ('time', models.DateTimeField(db_column='Time')),
                ('duration', models.TimeField(db_column='Duration')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('brand', models.CharField(blank=True, max_length=45, null=True)),
                ('store', models.CharField(blank=True, max_length=45, null=True)),
                ('commissionn', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('keywordd', models.CharField(blank=True, db_column='keyword', max_length=45, null=True)),
                ('pmmidf', models.ForeignKey(blank=True, db_column='PMMidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.pmm')),
                ('productidf', models.ForeignKey(blank=True, db_column='Productidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderno', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=45, null=True)),
                ('paypal', models.CharField(max_length=45)),
                ('orderimage', models.ImageField(blank=True, null=True, upload_to='ordersimages')),
                ('Reviewimage', models.ImageField(blank=True, null=True, upload_to='reviewimages')),
                ('Refundimage', models.ImageField(blank=True, null=True, upload_to='refundimages')),
                ('pmidf', models.ForeignKey(blank=True, db_column='pmidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.pm')),
                ('pmmidf', models.ForeignKey(blank=True, db_column='pmmidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.pmm')),
                ('productidf', models.ForeignKey(blank=True, db_column='productidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.product')),
            ],
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('orderno', models.CharField(db_column='Orderno', max_length=45, primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date')),
                ('paypal', models.CharField(db_column='Paypal', max_length=45)),
                ('commissionnn', models.IntegerField(db_column='Commision')),
                ('pmmidf', models.ForeignKey(blank=True, db_column='pmmidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.pmm')),
                ('productidf', models.ForeignKey(blank=True, db_column='productidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.product')),
            ],
        ),
        migrations.CreateModel(
            name='Adminpaid',
            fields=[
                ('time', models.CharField(max_length=45, null=True)),
                ('id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('adminidf', models.ForeignKey(blank=True, db_column='adminidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.admin')),
                ('pmidf', models.ForeignKey(blank=True, db_column='pmidf', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PMM.pm')),
            ],
        ),
    ]
