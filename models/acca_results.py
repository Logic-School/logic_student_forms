from odoo import models,api,fields

class AccaResults(models.Model):
    _name="logic.acca.results"
    _rec_name = "student_name"
    result_window = fields.Many2one('logic.acca.result.window')
    student_name = fields.Char(string="Student Name")
    acca_reg_no = fields.Char(string="ACCA Reg No")
    whatsapp_no = fields.Char(string="Whatsapp No")
    branch = fields.Many2one('logic.base.branches',string="Branch")
    exam1_results = fields.Many2many('logic.acca.student.result','acca_result_exam1_rel',string="Exam 1 Results")
    exam2_results = fields.Many2many('logic.acca.student.result','acca_result_exam2_rel',string="Exam 2 Results")


class AccaStudentResult(models.Model):
    _name = "logic.acca.student.result"
    acca_result_id = fields.Many2one('logic.acca.results',string="ACCA Result")
    paper_id = fields.Many2one('logic.paper.options', string="Paper ID")
    marks = fields.Integer(string="Marks")

class AccaWindow(models.Model):
    _name="logic.acca.result.window"
    name = fields.Char(string="Window")