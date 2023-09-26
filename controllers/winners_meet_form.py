from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
import logging




class WinnersMeetForm(http.Controller):
    @http.route(['/winners_meet/<string:batch_id>'], type='http', auth="public", website=True)
    def winners_form(self, batch_id, **kw):
        decoded_bytes = base64.b64decode(batch_id)
        batch_id = int.from_bytes(decoded_bytes, byteorder='big')
        batch = request.env['logic.base.batch'].sudo().search([('id','=',batch_id)])
        values = {
            'batch_name': batch.name,
            'batch_id': batch_id,

        }
        return request.render("logic_student_forms.winners_meet_form_template", values)
    
    @http.route(['/winners_meet/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def winners_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        try:
            student_photo = kw.get('student_photo')
            result_screenshot = kw.get('result_screenshot')
            request.env["logic.winners.meet"].sudo().create({
                'student_name': kw.get('student_name'),
                'phone': kw.get('phone'),
                # 'email_from': post.get('email'),
                'group': kw.get('group'),
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo)!=str else False,
                'result_screenshot': base64.b64encode(result_screenshot.read()) if type(result_screenshot)!=str else False,
                'batch_id': kw.get('batch_id'),
                'campus_name': kw.get('campus_name'),
                'class_teacher': kw.get('class_teacher'),
                'mode_of_study': kw.get('mode_of_study'),
                'part': kw.get('part'),
                'qualification_status': kw.get('qualification_status')
            })
            # products = request.env['product.product'].search([])
            # values = {
            #     'products': products
            # }
            return request.render("logic_student_forms.student_form_submit_successful", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.student_form_error", {})