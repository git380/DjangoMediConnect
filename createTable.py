import os
import django

# Django設定をロード
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoMediConnect.settings')
django.setup()

# DB作成
from MediConnect import models

# Create Shiiregyosha entries
shiiregyosha_data = [
    {"shiireid": "1111", "shiiremei": "1111", "shiireaddress": "1111", "shiiretel": "111-000-1111", "shihonkin": 1111, "nouki": 11},
    {"shiireid": "58274354", "shiiremei": "483658", "shiireaddress": "358436", "shiiretel": "6347", "shihonkin": 4758, "nouki": 64},
]

for data in shiiregyosha_data:
    models.Shiiregyosha.objects.create(**data)

# Create Employee entries
employee_data = [
    {"empid": "1", "empfname": "a", "emplname": "a", "emppasswd": "a", "emprole": 2},
    {"empid": "2", "empfname": "c", "emplname": "c", "emppasswd": "a", "emprole": 2},
    {"empid": "3", "empfname": "b", "emplname": "b", "emppasswd": "a", "emprole": 3},
    {"empid": "4", "empfname": "a", "emplname": "a", "emppasswd": "a", "emprole": 3},
    {"empid": "admin", "empfname": "admin", "emplname": "admin", "emppasswd": "a", "emprole": 1},
]

for data in employee_data:
    models.Employee.objects.create(**data)

# Create Patient entries
patient_data = [
    {"patid": "3", "patfname": "a", "patlname": "z", "hokenmei": "111", "hokenexp": "2024-01-09"},
    {"patid": "0003", "patfname": "0003", "patlname": "0003", "hokenmei": "0003", "hokenexp": "2024-01-09"},
    {"patid": "1", "patfname": "fdas", "patlname": "fsa", "hokenmei": "fsa", "hokenexp": "2023-12-22"},
    {"patid": "2", "patfname": "あ", "patlname": "あ", "hokenmei": "12", "hokenexp": "2023-12-14"},
    {"patid": "3", "patfname": "a", "patlname": "z", "hokenmei": "111", "hokenexp": "2023-12-14"},
]

for data in patient_data:
    models.Patient.objects.create(**data)

# Create Medicine entries
medicine_data = [
    {"medicineid": "1", "medicinename": "オロナイン", "unit": "塗り"},
    {"medicineid": "2", "medicinename": "バンドエイド", "unit": "枚"},
    {"medicineid": "3", "medicinename": "湿布", "unit": "枚"},
]

for data in medicine_data:
    models.Medicine.objects.create(**data)

# Create Treatment entries
treatment_data = [
    {"patid": models.Patient.objects.get(patid="1"), "medicineid": models.Medicine.objects.get(medicineid="2"), "quantity": 1, "impdate": "2023-12-11"},
    {"patid": models.Patient.objects.get(patid="0003"), "medicineid": models.Medicine.objects.get(medicineid="1"), "quantity": 1, "impdate": "0003"},
]

for data in treatment_data:
    models.Treatment.objects.create(**data)
