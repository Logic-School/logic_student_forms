from odoo import models,fields,api

class WinnersMeet(models.Model):
    _name = "logic.winners.meet"
    _rec_name = "student_name"
    student_name = fields.Char(string="Name")
    phone = fields.Char(string="Phone No")
    group = fields.Selection(selection=[('group1','Group 1'),('group2','Group 2'),('both','Both')],string="Group")
    result_screenshot = fields.Binary(string="Result Screenshot")
    student_photo = fields.Binary(string="Updated Photo")
    class_teacher = fields.Char(string="Class Teacher")
    batch_id = fields.Many2one('logic.base.batch',string="Batch Name")
    campus_name = fields.Char(string="Campus Name")
    mode_of_study = fields.Selection(selection=[('online','Online'),('offline','Offline')],string="Mode of Study")
    part = fields.Selection(selection=[('part1','Part 1'),('part2','Part 2'),('both','Both')])
    qualification_status = fields.Selection(selection=[('semi','Semi Qualified'),('full','Fully Qualified'),('both','Both Qualified in Single Window')])
