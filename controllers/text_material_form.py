from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
import logging

class TextMaterialForm(http.Controller):
    @http.route(['/text_material/<string:batch_id>'], type='http', auth="public", website=True)
    def text_material_form(self, batch_id, **kw):
        decoded_bytes = base64.b64decode(batch_id)
        batch_id = int.from_bytes(decoded_bytes, byteorder='big')
        batch = request.env['logic.base.batch'].sudo().search([('id','=',batch_id)])
        values = {
            'batch_name': batch.name,
            'batch_id': batch_id,

        }
        return request.render("logic_student_forms.text_material_form_template", values)
    
    @http.route(['/text_material/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def text_material_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')

        try:
            receipt_screenshot = kw.get('receipt_screenshot')

            request.env["logic.text.material"].sudo().create({
                'first_name': kw.get('first_name'),
                'last_name': kw.get('last_name'),
                'email': kw.get('email'),
                'batch_id': kw.get('batch_id'),
                'campus_name': kw.get('campus_name'),
                'class_teacher': kw.get('class_teacher'),
                'mobile': kw.get('mobile'),
                'receipt_screenshot': base64.b64encode(receipt_screenshot.read()) if type(receipt_screenshot)!=str else False,

            })
            # products = request.env['product.product'].search([])
            # values = {
            #     'products': products
            # }
            return request.render("logic_student_forms.student_form_submit_successful", {})
        except Exception as e:
            logger.error(e)
            return request.render("logic_student_forms.student_form_error", {})