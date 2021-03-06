# Generated by Django 3.0.4 on 2020-03-29 06:54

from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DeptManage', '0001_initial'),
        ('JurisdictionManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=254)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='DeptManage.Department')),
                ('jurisdiction', models.ManyToManyField(related_name='u_jurisdictions', to='JurisdictionManage.Jurisdiction')),
            ],
            options={
                'db_table': 'user',
                'ordering': ['-create_time'],
            },
        ),
    ]
