<<<<<<< HEAD
# Generated by Django 3.1.5 on 2024-04-15 23:58
=======
# Generated by Django 3.1.5 on 2023-03-15 18:53
>>>>>>> f980341a (added all migrations (#1431))

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosedHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(blank=True, default='', max_length=500)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected')], default='pending', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('extra_info', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_leaves', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveOffline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(blank=True, default='', max_length=500)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('application_date', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_leaves_offline', to=settings.AUTH_USER_MODEL)),
                ('leave_user_select', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('max_in_year', models.IntegerField(default=2)),
                ('requires_proof', models.BooleanField(default=False)),
                ('authority_forwardable', models.BooleanField(default=False)),
                ('for_faculty', models.BooleanField(default=True)),
                ('for_staff', models.BooleanField(default=True)),
                ('for_student', models.BooleanField(default=False)),
                ('requires_address', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RestrictedHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='VacationHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ReplacementSegmentOffline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement_type', models.CharField(choices=[('academic', 'Academic Replacement'), ('administrative', 'Administrative Replacement')], default='academic', max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replace_segments_offline', to='leave.leaveoffline')),
                ('replacer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rep_requests_offline', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReplacementSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replacement_type', models.CharField(choices=[('academic', 'Academic Replacement'), ('administrative', 'Administrative Replacement')], default='academic', max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected')], default='pending', max_length=20)),
                ('remark', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replace_segments', to='leave.leave')),
                ('replacer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rep_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveSegmentOffline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(null=True, upload_to='leave/leave_documents/')),
                ('start_date', models.DateField()),
                ('start_half', models.BooleanField(default=False)),
                ('end_date', models.DateField()),
                ('end_half', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='segments_offline', to='leave.leaveoffline')),
                ('leave_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leave.leavetype')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(null=True, upload_to='leave/leave_documents/')),
                ('start_date', models.DateField()),
                ('start_half', models.BooleanField(default=False)),
                ('end_date', models.DateField()),
                ('end_half', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='segments', to='leave.leave')),
                ('leave_type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leave.leavetype')),
            ],
        ),
        migrations.CreateModel(
            name='LeavesCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2019)),
                ('remaining_leaves', models.FloatField(default=2.0)),
                ('leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.leavetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_balance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(blank=True, max_length=50, null=True)),
                ('permission', models.CharField(choices=[('intermediary', 'Intermediary Staff'), ('sanc_auth', 'Leave Sanctioning Authority'), ('sanc_off', 'Leave Sanctioning Officer')], default='sanc_auth', max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected')], default='pending', max_length=20)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to='leave.leave')),
                ('requested_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_leave_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveMigration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_migration', models.CharField(choices=[('revert', 'Revert Responsibilities'), ('transfer', 'Transfer Responsibilities')], default='transfer', max_length=10)),
                ('on_date', models.DateField()),
                ('replacement_type', models.CharField(choices=[('academic', 'Academic Replacement'), ('administrative', 'Administrative Replacement')], default='academic', max_length=20)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_migrations', to='leave.leave')),
                ('replacee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacee_migrations', to=settings.AUTH_USER_MODEL)),
                ('replacer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacer_migrations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveAdministrators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sanc_authority_of', to='globals.designation')),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sanc_officer_of', to='globals.designation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leave_admins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
