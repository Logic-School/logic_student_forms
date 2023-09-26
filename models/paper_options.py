from odoo import models,fields,api

class PaperOption(models.Model):
    _name = "logic.paper.options"
    def _compute_name(self):
        for record in  self:
            record.name=record.paper_name
            if record.abbr:
                record.name+= ' - ' + record.abbr
    name = fields.Char(string="Name",store=True,compute="_compute_name")
    paper_name = fields.Char(string="Paper Name",required=True)
    abbr = fields.Char(string="Abbreviation")

class PaperOptionsWithMode(models.Model):
    _name = "logic.paper.options.mode"
    def _compute_name(self):
        for record in self:
            if record.paper_id:
                record.name=record.paper_id.paper_name
                if record.paper_id.abbr:
                    record.name+= ' - ' + record.paper_id.abbr
            else:
                record.name=''
    name = fields.Char(string="Name",store=True,compute="_compute_name")
    # paper_name = fields.Char(string="Paper Name",required=True)
    # abbr = fields.Char(string="Abbreviation")  
    paper_id = fields.Many2one('logic.paper.options',string="Paper ID")
    class_mode = fields.Selection(selection=[('online','Online'),('offline','Offline'),('blended','Blended (Offline and Online)')])
