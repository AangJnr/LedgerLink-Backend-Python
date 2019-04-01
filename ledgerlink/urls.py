from ledgerlink.models import VslaRegion, Vsla, FinancialInstitution, TechnicalTrainer, VslaCycle, Meeting, Attendance, \
    Saving, Fine, LoanIssue
from ledgerlink.ui.attendance_list import AttendanceList
from ledgerlink.ui.financial_institution_form import FinancialInstitutionForm
from ledgerlink.ui.financial_institution_list import FinancialInstitutionList
from ledgerlink.ui.fine_list import FineList
from ledgerlink.ui.loan_issue_list import LoanIssueList
from ledgerlink.ui.meeting_list import MeetingList
from ledgerlink.ui.saving_list import Savinglist
from ledgerlink.ui.technical_trainer_form import TechnicalTrainerForm
from ledgerlink.ui.technical_trainer_list import TechnicalTrainerList
from ledgerlink.ui.vsla_cycle_list import VslaCycleList
from ledgerlink.ui.vsla_form import VslaForm
from ledgerlink.ui.vsla_list import VslaList
from ledgerlink.ui.vsla_region_form import VslaRegionForm
from ledgerlink.ui.vsla_region_list import VslaRegionList
from ledgerlink.views import VslaMasterChildView, VslaCycleMasterChildView, VslaCycleMeetingMasterChildView
from xf.xf_crud.crud_url_builder import XFCrudURLBuilder
from xf.xf_crud.xf_crud_helpers import crudurl

urlpatterns = []

#URL Builders

vsla_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-groups", model_type=Vsla)
vsla_cycle_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-cycle", model_type=VslaCycle)
vsla_cycle_meeting_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-cycle-meeting", model_type=Meeting)
vsla_cycle_meeting_attendance_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-cycle-meeting-attendance", model_type=Attendance)
vsla_cycle_meeting_saving_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-cycle-meeting-saving", model_type=Saving)
vsla_cycle_meeting_fine_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-cycle-meeting-fine", model_type=Fine)
vsla_cycle_meeting_loan_issue_builder = XFCrudURLBuilder(url_app_name="crud", url_model_name="savings-group-cycle-meeting-loan-issue", model_type=LoanIssue)
#
# #List of Cycles by VSLA
urlpatterns += [vsla_builder.get_list_related_url(list_class_type=VslaList, url_related_name="by-institution", foreign_key_name="financialinstitution")]
urlpatterns += [vsla_cycle_builder.get_list_related_url(list_class_type=VslaCycleList, url_related_name="by-vsla", foreign_key_name="vsla")]
urlpatterns += [vsla_cycle_meeting_builder.get_list_related_url(list_class_type=MeetingList, url_related_name="by-cycle", foreign_key_name="vsla_cycle")]
urlpatterns += [vsla_cycle_meeting_attendance_builder.get_list_related_url(list_class_type=AttendanceList, url_related_name="by-meeting-attendance", foreign_key_name="meeting")]
urlpatterns += [vsla_cycle_meeting_saving_builder.get_list_related_url(list_class_type=Savinglist, url_related_name="by-meeting-saving", foreign_key_name="meeting")]
urlpatterns += [vsla_cycle_meeting_fine_builder.get_list_related_url(list_class_type=FineList, url_related_name="by-meeting-fine", foreign_key_name="meeting")]
urlpatterns += [vsla_cycle_meeting_loan_issue_builder.get_list_related_url(list_class_type=LoanIssueList, url_related_name="by-meeting-loan-issue", foreign_key_name="meeting")]
#
# #Master Child pages
#
urlpatterns += [vsla_builder.get_overview_url(view_class_type=VslaMasterChildView)]
urlpatterns += [vsla_cycle_builder.get_overview_url(view_class_type=VslaCycleMasterChildView)]
urlpatterns += [vsla_cycle_meeting_builder.get_overview_url(view_class_type=VslaCycleMeetingMasterChildView)]

# urlpatterns += [vsla_cycle_instance_builder.get_overview_url(view_class_type=MeetingInstanceMasterChildView)]

## Basic CRUD pages

urlpatterns += crudurl("crud", "savings-group-cycle", VslaCycle, None, VslaCycleList)
urlpatterns += crudurl("crud", "savings-group-cycle-meeting", Meeting, None, MeetingList)
urlpatterns += crudurl("crud", "savings-group-cycle-meeting-attendance", Attendance, None, AttendanceList)
urlpatterns += crudurl("crud", "savings-group-cycle-meeting-saving", Saving, None, Savinglist)
urlpatterns += crudurl("crud", "savings-group-cycle-meeting-fine", Fine, None, FineList)
urlpatterns += crudurl("crud", "savings-group-cycle-meeting-loan-issue", LoanIssue, None, LoanIssueList)
urlpatterns += crudurl("crud", "savings-groups", Vsla, VslaForm, VslaList)
urlpatterns += crudurl("crud", "financial-institutions", FinancialInstitution, FinancialInstitutionForm, FinancialInstitutionList)
urlpatterns += crudurl("crud", "vsla-regions", VslaRegion, VslaRegionForm, VslaRegionList)
urlpatterns += crudurl("crud", "community-based-trainers", TechnicalTrainer, TechnicalTrainerForm, TechnicalTrainerList)