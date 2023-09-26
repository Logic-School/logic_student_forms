from odoo import models,fields,api

class ResultServiceTemplate(models.Model):
    _name = "logic.result.service"
    def _compute_name(self):
        for record in self:
            name = ''
            if record.first_name:
                name += record.first_name + " "
            if record.last_name:
                name += record.last_name
            record.name = name
    name = fields.Char(string="Name", compute = "_compute_name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    email = fields.Char(string="Email")
    acca_reg_no = fields.Char(string="ACCA Reg No")
    phone = fields.Char(string="Phone No")
    dob = fields.Date(string="Date of Birth")
    exam_papers_1 = fields.Many2many('logic.paper.options','result_serv_papers_rel1','result_serv_id','paper_id', string="Exam Papers 1")
    exam_papers_2 = fields.Many2many('logic.paper.options','result_serv_papers_rel2','result_serv_id','paper_id', string="Exam Papers 2")
    exam_papers_3 = fields.Many2many('logic.paper.options','result_serv_papers_rel3','result_serv_id','paper_id', string="Exam Papers 3")
