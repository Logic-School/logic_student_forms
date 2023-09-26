from odoo import models,fields,api
import base64

class FormLinkGenerationWizard(models.TransientModel):
    _name = "form.link.generation.wizard"
    winners_batch_id = fields.Many2one("logic.base.batch",string="Winners Meet")
    hock_batch_id = fields.Many2one("logic.base.batch",string="Hock Access")
    material_batch_id = fields.Many2one("logic.base.batch",string="Text Material")
    
    faculty_id = fields.Many2one("faculty.details",string="Faculty Feedback")
    class_id = fields.Many2one("logic.base.class", string="Class")
    winners_link = fields.Char(string="Winners Meet Form",default="")
    hock_link = fields.Char(string="Hock Access Form")
    material_link = fields.Char(string="Study Material Form")
    faculty_feedback_link = fields.Char(string="Faculty Feedback Form",default="")


    def generate_link(self,batch,form_type):
        int_bytes = batch.id.to_bytes((batch.id.bit_length() + 7) // 8, 'big')
        base64_string = base64.b64encode(int_bytes).decode('utf-8')
        company_website = self.env.company.website
        link = company_website + "/"+ form_type + "/" + base64_string
        return link

    @api.onchange('winners_batch_id')
    def generate_winners_link(self):
        if not self.winners_batch_id:
            self.winners_link = False
        else:
            self.winners_link = self.generate_link(self.winners_batch_id,'winners_meet')

    @api.onchange('hock_batch_id')
    def generate_hock_link(self):
        if not self.hock_batch_id:
            self.hock_link = False
        else:
            self.hock_link = self.generate_link(self.hock_batch_id,'hock_access')


    @api.onchange('material_batch_id')
    def generate_material_link(self):
        if not self.material_batch_id:
            self.material_link = False
        else:
            self.material_link = self.generate_link(self.material_batch_id,'text_material')


    @api.onchange('faculty_id','class_id')
    def generate_faculty_feedback_link(self):
        if not self.faculty_id:
            self.faculty_feedback_link = False
        else:
            self.faculty_feedback_link = self.generate_link(self.faculty_id,'faculty_feedback')

            int_bytes = self.class_id.id.to_bytes((self.class_id.id.bit_length() + 7) // 8, 'big')
            base64_string = base64.b64encode(int_bytes).decode('utf-8')
            self.faculty_feedback_link+="/"+str(base64_string)

    def show_copy_successful(self):
        # for record in self:
            return  {
                        'type': 'ir.actions.client',
                        'tag': 'display_notification',
                        'params': {
                            'title': ('Link Copied Successfully'),
                            'message': 'The form link has been copied to your clipboard',
                            # 'sticky': False,
                            }
                    }


