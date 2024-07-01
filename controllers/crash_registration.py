from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
import logging


class CrashRegistrationForm(http.Controller):
    @http.route(['/crash_form/<string:course_level>/registration/<string:batch_id>'], type='http', auth="public", website=True)
    def registration_form(self, batch_id, course_level, **kw):
        decoded_bytes = base64.b64decode(batch_id)
        batch_id = int.from_bytes(decoded_bytes, byteorder='big')

        batch = request.env['logic.base.batch'].sudo().search([('id', '=', batch_id)])
        values = {
            'batch_name': batch.name,
            'batch_id': batch_id,
            'course_level': course_level
        }
        print(values, 'values')
        return request.render("logic_student_forms.crash_registration_form_template", values)

    @http.route(['/crash_form/full_course'], type='http', auth="public", website=True)
    def registration_full_course_form(self, **kw):
        print('hii')
        # decoded_bytes = base64.b64decode(batch_id)
        # batch_id = int.from_bytes(decoded_bytes, byteorder='big')
        # batch = request.env['logic.base.batch'].sudo().search([('id', '=', batch_id)])
        # values = {
        #     'batch_name': batch.name,
        #     'batch_id': batch_id,
        # }
        return request.render("logic_student_forms.crash_registration_full_course_form_template", )

    @http.route(['/crash_form/ca_inter/other_course'], type='http', auth="public", website=True)
    def registration_ca_inter_course_form(self, **kw):
        print('hii')

        return request.render("logic_student_forms.crash_registration_other_course_ca_inter_form_template", )

    @http.route(['/crash_form/cma_inter/other_course'], type='http', auth="public", website=True)
    def registration_cma_inter_course_form(self, **kw):
        print('hii')

        return request.render("logic_student_forms.crash_registration_other_course_cma_inter_form_template", )

    @http.route(['/crash_form/ca_final/other_course'], type='http', auth="public", website=True)
    def registration_ca_final_course_form(self, **kw):
        print('hii')

        return request.render("logic_student_forms.crash_registration_other_course_ca_final_form_template", )

    @http.route(['/crash_form/cma_final/other_course'], type='http', auth="public", website=True)
    def registration_cma_final_course_form(self, **kw):
        print('hii')

        return request.render("logic_student_forms.crash_registration_other_course_cma_final_form_template", )

    @http.route(['/crash_form/full_course/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def registration_full_course_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        print(kw)
        try:
            student_photo = kw.get('student_photo')
            payment_screenshot = kw.get('payment_screenshot')
            request.env["logic.crash.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('mobile_number'),
                'subject': kw.get('group'),
                'batch_id': kw.get('batch_id'),
                'address': kw.get('address'),
                'email': kw.get('mail_id'),
                'student_whatsapp': kw.get('whatsapp_number'),
                'how_do_you_know_about_us': kw.get('how_did_you_know'),
                'remarks': kw.get('remarks'),
                'level': kw.get('level_id'),
                'admission_officer': kw.get('admission_officer'),
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,
                'payment_screenshot': base64.b64encode(payment_screenshot.read()) if type(payment_screenshot) != str else False,

            })

            return request.render("logic_student_forms.crash_student_form_submit_successful", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.crash_student_form_error", {})

    @http.route(['/crash_form/ca_inter/other_course/submit'], type='http', auth="public", website=True, csrf=False,
                method=['POST'])
    def registration_other_ca_inter_course_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        print(kw)
        try:
            student_photo = kw.get('student_photo')
            result_screenshot = kw.get('result_screenshot')
            request.env["logic.crash.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('mobile_number'),
                'subject': kw.get('group'),
                'batch_id': kw.get('batch_id'),
                'address': kw.get('address'),
                'email': kw.get('mail_id'),
                'other_subject': kw.get('sub_group'),
                'student_whatsapp': kw.get('whatsapp_number'),
                'how_do_you_know_about_us': kw.get('how_did_you_know'),
                'remarks': kw.get('remarks'),
                'level': kw.get('level_id'),
                'admission_officer': kw.get('admission_officer'),
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,



            })

            return request.render("logic_student_forms.crash_student_form_submit_successful", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.crash_student_form_error", {})

    @http.route(['/crash_form/cma_inter/other_course/submit'], type='http', auth="public", website=True, csrf=False,
                method=['POST'])
    def registration_other_cma_inter_course_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        print(kw)
        try:
            student_photo = kw.get('student_photo')
            result_screenshot = kw.get('result_screenshot')
            request.env["logic.crash.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('mobile_number'),
                'subject': kw.get('group'),
                'batch_id': kw.get('batch_id'),
                'address': kw.get('address'),
                'email': kw.get('mail_id'),
                'other_subject': kw.get('sub_group'),
                'student_whatsapp': kw.get('whatsapp_number'),
                'how_do_you_know_about_us': kw.get('how_did_you_know'),
                'remarks': kw.get('remarks'),
                'level': kw.get('level_id'),
                'admission_officer': kw.get('admission_officer'),
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,

            })

            return request.render("logic_student_forms.crash_student_form_submit_successful", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.crash_student_form_error", {})

    @http.route(['/crash_form/ca_final/other_course/submit'], type='http', auth="public", website=True, csrf=False,
                method=['POST'])
    def registration_other_ca_final_course_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        print(kw)
        try:
            student_photo = kw.get('student_photo')
            result_screenshot = kw.get('result_screenshot')
            request.env["logic.crash.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('mobile_number'),
                'subject': kw.get('group'),
                'batch_id': kw.get('batch_id'),
                'address': kw.get('address'),
                'email': kw.get('mail_id'),
                'other_subject': kw.get('sub_group'),
                'student_whatsapp': kw.get('whatsapp_number'),
                'how_do_you_know_about_us': kw.get('how_did_you_know'),
                'remarks': kw.get('remarks'),
                'level': kw.get('level_id'),
                'admission_officer': kw.get('admission_officer'),
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,

            })

            return request.render("logic_student_forms.crash_student_form_submit_successful", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.crash_student_form_error", {})

    @http.route(['/crash_form/cma_final/other_course/submit'], type='http', auth="public", website=True, csrf=False,
                method=['POST'])
    def registration_other_cma_final_course_form_submit(self, **kw):
        logger = logging.getLogger('Error Logger')
        print(kw)
        try:
            student_photo = kw.get('student_photo')
            result_screenshot = kw.get('result_screenshot')
            request.env["logic.crash.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('mobile_number'),
                'subject': kw.get('group'),
                'batch_id': kw.get('batch_id'),
                'address': kw.get('address'),
                'email': kw.get('mail_id'),
                'other_subject': kw.get('sub_group'),
                'student_whatsapp': kw.get('whatsapp_number'),
                'how_do_you_know_about_us': kw.get('how_did_you_know'),
                'remarks': kw.get('remarks'),
                'level': kw.get('level_id'),
                'admission_officer': kw.get('admission_officer'),
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,

            })

            return request.render("logic_student_forms.crash_student_form_submit_successful", {})
        except Exception as e:
            print(logger.error(e))
            return request.render("logic_student_forms.crash_student_form_error", {})