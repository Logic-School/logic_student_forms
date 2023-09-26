from odoo import models,fields,api

class ClassCommencement(models.Model):
    _name = "logic.class.commencement"
    _rec_name="student_name"
    student_name = fields.Char(string="Student Name")
    email = fields.Char(string="Email")
    acca_reg_no = fields.Char(string="ACCA Reg No")
    dob = fields.Date(string="Date of Birth")
    student_whatsapp = fields.Char(string="Student Whatsapp")
    parent_whatsapp = fields.Char(string="Parent Whatsapp")
    batch = fields.Selection(selection=[('regular','Logic Regular Student'),('paper_wise','Paper Wise')], string="Batch")
    paper_options = fields.Many2many('logic.paper.options.mode',string="Paper Options")
    attempt = fields.Selection(string="Attempt",selection=[('first','First'),('resit','Resit')])



