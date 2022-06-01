# Generated by Django 4.0.4 on 2022-06-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_rename_research_facultymodel_researchtypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultymodel',
            name='customIMG',
        ),
        migrations.RemoveField(
            model_name='facultymodel',
            name='heading',
        ),
        migrations.AlterField(
            model_name='facultymodel',
            name='pic',
            field=models.ImageField(blank=True, default='images/default_profile.png', null=True, upload_to='images/'),
        ),
    ]