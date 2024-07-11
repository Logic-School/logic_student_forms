from odoo import models, fields, api


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
