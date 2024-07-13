import base64
import io
import xlsxwriter

from odoo import models, fields,api, _
from odoo.exceptions import UserError



class CrashRegistrationForms(models.Model):
    _name = "logic.crash.forms"
    _rec_name = "student_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_name = fields.Char(string="Student Name")
    mobile_number = fields.Char(string="Mobile Number")
    email = fields.Char(string="Email")
    student_whatsapp = fields.Char(string="Student Whatsapp")
    how_do_you_know_about_us = fields.Char(string="How do you know about us")
    remarks = fields.Char(string="Remarks")
    batch_id = fields.Many2one('logic.base.batch', string="Batch")
    address = fields.Text(string="Address")
    admission_officer = fields.Char(string="Admission Officer")
    student_photo = fields.Binary(string="Student Photo")
    payment_screenshot = fields.Binary(string="Payment Screenshot")
    level = fields.Selection([('inter', 'Inter'), ('final', 'Final')], string="Level")
    other_subject = fields.Selection(
        [('group_2_audit_fm_sm_costing', 'Group 2 Audit FM SM Costing'), ('audit', 'Audit'), ('fm', 'FM'), ('sm', 'SM'),
         ('costing', 'Costing'), ('group_2_fm_sm_audit', 'Group 2 FM SM Audit'),
         ('full_course_group_1_group_2', 'Full Course Group 1 Group 2'),
         ('group_1_fr_audit_afm', 'Group 1 FR Audit AFM'), ('group_2_dt_idt', 'Group 2 DT IDT'), ('fr', 'FR'),
         ('afm', 'AFM'), ('audit', 'Audit'), ('dt', 'DT'), ('idt', 'IDT'),
         ('full_course_group_3_group_4', 'Full Course Group 3 Group 4'),
         ('group_3_dt_sfm_scm_law', 'Group 3 DT SFM SCM Law'),
         ('group_4_idt_cma_cfr_spm_bv', 'Group 4 IDT CMA CFR SPM BV'), ('dt', 'DT'), ('sfm', 'SFM'), ('scm', 'SCM'),
         ('law', 'Law'), ('idt', 'IDT'), ('cma', 'CMA'), ('cfr', 'CFR'), ('spm_bv', 'SPM BV'),
         ('financial_accounting', 'Financial Accounting'), ('cost_accounting', 'Cost Accounting'),
         ('operation_management', 'Operation Management'), ('auditing', 'Auditing'), ('corporate_accounting', 'Corporate Accounting'),
         ('auditing', 'Auditing'), ('bda', 'BDA'), ('fm', 'FM'), ('management_accounting', 'Management Accounting'),],
        string="Other Subject")

    subject = fields.Selection(
        [('full_course', 'Full Course'), ('group_1', 'Group 1'), ('group_2', 'Group 2'), ('other', 'Other')],
        string="Subject")


class CrashResultsForms(models.Model):
    _name = "logic.crash.result.forms"
    _rec_name = "student_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_name = fields.Char(string="Student Name")
    student_photo = fields.Binary(string="Student Photo")
    attach_result = fields.Binary(string="Attach Result")
    level = fields.Selection([('inter', 'Inter'), ('final', 'Final')], string="Level")
    mobile_number = fields.Char(string="Mobile Number")
    group = fields.Selection([('first_group', 'First Group'), ('second_group', 'Second Group'), ('both', 'Both')],
                             string="Group")
    remarks = fields.Char(string="Remarks")
    added_date = fields.Date(string="Added Date", default=lambda self: fields.Date.today())
    student_photo_download = fields.Binary(string="Student Photo Download")
    attach_result_download = fields.Binary(string="Attach Result Download")

    @api.model
    def create(self, vals):
        if not vals.get('added_date'):
            vals['added_date'] = fields.Date.context_today(self)
        return super(CrashResultsForms, self).create(vals)

    def print_xlsx_report(self):
        active_ids = self.env.context.get('active_ids', [])
        if not active_ids:
            return {'type': 'ir.actions.act_window_close'}  # Or handle no IDs case as needed
        for record in self:
            return {
                'type': 'ir.actions.act_url',
                'url': '/crash/results?ids=%s' % ','.join(map(str, active_ids)),
                'target': 'new',
            }

    def get_report_lines(self, active_ids):
        report_lines = []
        records = self.search([('id', 'in', active_ids)])
        for record in records:
            line = {
                'student_name': record.student_name,
                'student_photo': record.student_photo,
                'attach_result': record.attach_result,
                'level': record.level or '',
                'mobile_number': record.mobile_number or '',
                'group': dict(record._fields['group'].selection).get(record.group, ''),
                'remarks': record.remarks or '',
            }
            report_lines.append(line)
        return report_lines

    def add_created_date(self):
        active_ids = self.env.context.get('active_ids', [])
        rec = self.env['logic.crash.result.forms'].browse(active_ids)
        for record in rec:

            record.added_date = record.create_date


class CrashMentoringForms(models.Model):
    _name = "logic.crash.mentoring.forms"
    _rec_name = "student_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_name = fields.Char(string="Student Name")
    mobile_number = fields.Char(string="Mobile Number")
    email = fields.Char(string="Email")
    student_whatsapp = fields.Char(string="Student Whatsapp")
    how_do_you_know_about_us = fields.Char(string="How do you know about us")
    remarks = fields.Char(string="Remarks")
