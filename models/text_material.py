from odoo import models,fields,api

class TextMaterialRequest(models.Model):
    _name = "logic.text.material"
    name = fields.Char(string="Name",compute="_compute_name")
    def _compute_name(self):
        for record in self:
            name = ''
            if record.first_name:
                name += record.first_name + " "
            if record.last_name:
                name += record.last_name
            record.name = name
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    email = fields.Char(string="Email")
    batch_id = fields.Many2one('logic.base.batch',string="Batch")
    campus_name = fields.Char(string="Campus Name")
    admission_no = fields.Char(string="Admission No")
    class_teacher = fields.Char(string="Class Teacher")
    mobile = fields.Char(string="Mobile")
    receipt_screenshot = fields.Binary(string="Receipt Screenshot")