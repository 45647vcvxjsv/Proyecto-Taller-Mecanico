# Generated by Django 5.1.1 on 2024-09-17 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_vehiculo_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reparacion',
            old_name='Vehiculo',
            new_name='vehiculo',
        ),
        migrations.AddField(
            model_name='cita',
            name='mecanico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.mecánico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='vehiculo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.vehiculo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='estado',
            field=models.CharField(choices=[('reparado', 'Reparado'), ('no_reparado', 'No reparado')], default='no_reparado', max_length=20),
        ),
    ]
