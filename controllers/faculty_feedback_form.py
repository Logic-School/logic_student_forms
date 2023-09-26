from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
import logging

class FacultyFeedbackForm(http.Controller):
    @http.route(['/faculty_feedback/<string:faculty_id>/<string:class_id>'], type='http', auth="public", website=True)
    def faculty_feedback_form(self, faculty_id,class_id, **kw):
        decoded_bytes = base64.b64decode(faculty_id)
        faculty_id = int.from_bytes(decoded_bytes, byteorder='big')   
        faculty = request.env['faculty.details'].sudo().browse(faculty_id)

        decoded_bytes = base64.b64decode(class_id)
        class_id = int.from_bytes(decoded_bytes, byteorder='big')  
        class_id = request.env['logic.base.class'].sudo().browse(class_id)

        values = {
            "faculty_name" : faculty.name.name,
            "faculty_id": faculty_id,
            "class_name": class_id.name,
            "class_id": class_id.id, 
        }
        return request.render("logic_student_forms.faculty_feedback_form_template", values)
    
    @http.route(['/faculty_feedback/submit'], type='http', auth="public", website=True, csrf=False)
    def faculty_feedback_form_submit(self, **kw):
        logger = logging.getLogger("Error Logger")
        try:
            request.env["logic.faculty.feedback"].sudo().create({
                'faculty': int(kw.get('faculty_id')),
                'student_name': kw.get('student_name'),
                'class_id': int(kw.get('class_id')),
                'student_rating': kw.get('student_rating'),
                'feedback': kw.get('feedback'),
            })  
            return request.render("logic_student_forms.student_form_submit_successful", {})
        except Exception as e:
            logger.error(e)
            return request.render("logic_student_forms.student_form_error", {})
                  
