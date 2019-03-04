# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-04 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledgerlink', '0005_auto_20190304_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='AttendanceId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='datasubmission',
            old_name='SubmissionId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='financialinstitution',
            old_name='FinancialInstitutionId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='fine',
            old_name='FineId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='loanissue',
            old_name='LoanId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='loanrepayment',
            old_name='RepaymentId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='MeetingId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='MemberId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='outstandingwelfare',
            old_name='OutstandingWelfareId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='saving',
            old_name='SavingId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='technicaltrainer',
            old_name='Id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='vsla',
            old_name='VslaId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='vslabankinghistory',
            old_name='BankingHistoryId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='vslacycle',
            old_name='CycleId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='vsladbactivation',
            old_name='ActivationId',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='welfare',
            old_name='WelfareId',
            new_name='id',
        ),
    ]
