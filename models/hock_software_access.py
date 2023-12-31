from odoo import models,fields,api

class HockAccess(models.Model):
    _name = "logic.hock.access"
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