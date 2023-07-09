# Generated by Django 4.2.2 on 2023-07-05 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_employer_rating_employer_post_num_and_more'),
        ('job', '0003_alter_job_post_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='employer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='account.employer'),
        ),
    ]
