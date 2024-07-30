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

    # @api.model
    # def get_action_based_on_role(self):
    #     user = self.env.user
    #     academic_group = self.env.ref('logic_student_forms.form_academic_department')
    #     if academic_group in user.groups_id:
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'name': 'Winners Meet',
    #             'res_model': 'logic.winners.meet',  # Replace with the actual model
    #             'view_mode': 'list',
    #             'target': 'new',
    #         }
    #     else:
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'name': 'Registration Form',
    #             'res_model': 'logic.crash.forms',  # Replace with the actual model
    #             'view_mode': 'form',
    #             'target': 'new',
    #         }