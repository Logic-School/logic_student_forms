from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
import logging


class CrashRegistrationForm(http.Controller):
    @http.route(['/crash_form/mentoring'], type='http', auth="public", website=True)
    def crash_mentoring_form(self, **kw):
        # decoded_bytes = base64.b64decode(batch_id)
        # batch_id = int.from_bytes(decoded_bytes, byteorder='big')
        # batch = request.env['logic.base.batch'].sudo().search([('id', '=', batch_id)])
        # values = {
        #     'batch_name': batch.name,
        #     'batch_id': batch_id,
        # }
        return request.render("logic_student_forms.crash_mentoring_form_template")

    @http.route(['/crash_form/mentoring/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def registration_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        try:
            student_photo = kw.get('student_photo')
            result_screenshot = kw.get('result_screenshot')
            request.env["logic.crash.mentoring.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('mobile_number'),

                'email': kw.get('mail_id'),
                'student_whatsapp': kw.get('whatsapp_number'),
                'how_do_you_know_about_us': kw.get('how_you_know_about_us'),
                'remarks': kw.get('remarks'),

            })

            return request.render("logic_student_forms.crash_student_form_submit_successful", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.crash_student_form_error", {})