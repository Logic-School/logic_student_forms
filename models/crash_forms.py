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


class CrashResultsForms(models.Model):
    _name = "logic.crash.result.forms"
    _rec_name = "student_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_name = fields.Char(string="Student Name")
    student_photo = fields.Binary(string="Student Photo")
    course = fields.Selection([('inter', 'Inter'), ('international', 'International')], string="Course")
    mobile_number = fields.Char( string="Mobile Number")
    group = fields.Selection([('first_group', 'First Group'), ('second_group', 'Second Group'), ('both', 'Both')],string="Group")
    remarks = fields.Char(string="Remarks")
