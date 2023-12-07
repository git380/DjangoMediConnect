import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('empfname', models.CharField(max_length=64)),
                ('emplname', models.CharField(max_length=64)),
                ('emppasswd', models.CharField(max_length=256)),
                ('emprole', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicineid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('medicinename', models.CharField(max_length=64)),
                ('unit', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('patfname', models.CharField(max_length=64)),
                ('patlname', models.CharField(max_length=64)),
                ('hokenmei', models.CharField(max_length=64)),
                ('hokenexp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Shiiregyosha',
            fields=[
                ('shiireid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('shiiremei', models.CharField(max_length=64)),
                ('shiireaddress', models.CharField(max_length=64)),
                ('shiiretel', models.CharField(max_length=13)),
                ('shihonkin', models.IntegerField()),
                ('nouki', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tabyouin',
            fields=[
                ('tabyouinid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('tabyouinmei', models.CharField(max_length=64)),
                ('tabyouinaddres', models.CharField(max_length=64)),
                ('tabyouintel', models.CharField(max_length=13)),
                ('tabyouinshihonkin', models.IntegerField()),
                ('kyukyu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('impdate', models.DateField()),
                ('medicineid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediConnect.medicine')),
                ('patid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediConnect.patient')),
            ],
        ),
    ]
