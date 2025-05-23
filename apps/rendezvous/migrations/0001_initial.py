# Generated by Django 5.1.7 on 2025-05-16 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePriseRendevous', models.DateTimeField()),
                ('service', models.CharField(max_length=100)),
                ('date_rdv', models.DateTimeField()),
                ('statut', models.CharField(choices=[('En attente', 'En attente'), ('Confirmé', 'Confirmé'), ('Annulé', 'Annulé'), ('Terminé', 'Terminé')], default='En attente', max_length=20)),
                ('rappel_envoye', models.BooleanField(default=False)),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous_en_tant_que_medecin', to='patients.patientprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous_en_tant_que_patient', to='patients.patientprofile')),
            ],
        ),
    ]
