from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
import logging


class HockAccessForm(http.Controller):
    @http.route(['/hock_access/<string:batch_id>'], type='http', auth="public", website=True)
    def hock_access_form(self, batch_id, **kw):
        decoded_bytes = base64.b64decode(batch_id)
        batch_id = int.from_bytes(decoded_bytes, byteorder='big')
        batch = request.env['logic.base.batch'].sudo().search([('id','=',batch_id)])
        values = {
            'batch_name': batch.name,
            'batch_id': batch_id,

        }
        return request.render("logic_student_forms.hock_access_form_template", values)
    
    @http.route(['/hock_access/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def hock_access_form_submit(self, **kw):
        try:
            logger = logging.getLogger("Error Logger")
            request.env["logic.hock.access"].sudo().create({
                'first_name': kw.get('first_name'),
                'last_name': kw.get('last_name'),
                'email': kw.get('email'),
                'batch_id': kw.get('batch_id'),
                'campus_name': kw.get('campus_name'),
            })
            # products = request.env['product.product'].search([])
            # values = {
            #     'products': products
            # }
            return request.render("logic_student_forms.student_form_submit_successful", {})
        except Exception as e:
            logger.error(e)
            return request.render("logic_student_forms.student_form_error", {})