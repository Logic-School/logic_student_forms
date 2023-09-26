from odoo import models,fields,api

class FacultyFeedback(models.Model):
    _name="logic.faculty.feedback"
    _rec_name = "student_name"
    student_name = fields.Char(string="Student Name")
    faculty = fields.Many2one('faculty.details',string="Faculty")
    class_id = fields.Many2one('logic.base.class',string="Class")
    feedback = fields.Text(string="Student Feedback")
    student_rating = fields.Selection(selection=[('0','No rating'),('1','Very Poor'),('2','Poor'),('3','Average'),('4','Good'),('5','Very Good')], string="Student Rating", default='0')