# Generated by Django 2.0.13 on 2019-05-17 18:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bidg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchsRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_branch_role', models.IntegerField()),
                ('vacant_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CBranchs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_branch', models.IntegerField()),
                ('branch_name', models.CharField(max_length=500)),
                ('branch_short', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='branchsroles',
            name='id_Rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidg.CBranchs'),
        ),
        migrations.AddField(
            model_name='branchsroles',
            name='id_branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidg.Roles'),
        ),
    ]