# Generated by Django 4.2.6 on 2023-10-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomCodeSolutions', '0003_alter_costos_directos_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=15)),
                ('producto', models.CharField(max_length=255)),
                ('cliente', models.CharField(max_length=255)),
                ('costos_directos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mano_de_obra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costos_indirectos', models.DecimalField(decimal_places=2, max_digits=10)),
                ('costo_total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'tabla_final',
            },
        ),
    ]
