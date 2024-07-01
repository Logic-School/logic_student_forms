from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
import logging


class CrashResultsForm(http.Controller):
    @http.route(['/crash_form/results'], type='http', auth="public", website=True)
    def results_form(self, **kw):
        # decoded_bytes = base64.b64decode(batch_id)
        # batch_id = int.from_bytes(decoded_bytes, byteorder='big')
        # batch = request.env['logic.base.batch'].sudo().search([('id', '=', batch_id)])
        # values = {
        #     'batch_name': batch.name,
        #     'batch_id': batch_id,
        # }
        return request.render("logic_student_forms.crash_results_form_template")

    @http.route(['/crash_form/results/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def winners_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        try:
            print(kw)
            student_photo = kw.get('student_photo')
            result_screenshot = kw.get('result_screenshot')
            request.env["logic.crash.result.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('contact_number'),
                # 'email_from': post.get('email'),
                'group': kw.get('part_group'),
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,
                'level': kw.get('part'),
                'remarks': kw.get('remarks'),

            })
            # products = request.env['product.product'].search([])
            # values = {
            #     'products': products
            # }
            return request.render("logic_student_forms.student_form_submit_successful_crash_results", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.student_form_error", {})