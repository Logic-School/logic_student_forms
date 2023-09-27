from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
from  datetime import date
import logging

def cleaned_list(data_list):
    for i in range(len(data_list)-1,-1,-1):
        if data_list[i]=='':
            data_list.pop(i)
    return data_list

class AccaResultsForm(http.Controller):
    @http.route(['/acca_results/<string:result_window_id>'], type='http', auth="public", website=True)
    def acca_results_form(self,result_window_id,**kw):
        paper_option_objs = request.env['logic.paper.options'].sudo().search([])
        paper_options = []
        for paper_obj in paper_option_objs:
            paper_option = {'id':paper_obj.id,'paper_name':paper_obj.name}
            paper_options.append(paper_option)

        decoded_bytes = base64.b64decode(result_window_id)
        result_window_id = int.from_bytes(decoded_bytes, byteorder='big')
        result_window = request.env['logic.acca.result.window'].sudo().browse(result_window_id)

        branches = request.env['logic.base.branches'].sudo().search([])

        return request.render("logic_student_forms.acca_results_form_template", {'paper_options':paper_options,'result_window':result_window,'branches':branches})
    
    @http.route(['/acca_results/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def class_commencement_form_submit(self, **kw):
        logger = logging.getLogger("Error Debugger")

        try:
            selected_paper_ids_1 = request.httprequest.form.getlist('paper_options_1')
            exam_marks_1 = cleaned_list(request.httprequest.form.getlist('exam_marks_1'))

            selected_paper_ids_2 = request.httprequest.form.getlist('paper_options_2')
            exam_marks_2 = cleaned_list(request.httprequest.form.getlist('exam_marks_2'))


            logger.error(selected_paper_ids_1)
            logger.error(exam_marks_1)

            logger.error(selected_paper_ids_2)
            logger.error(exam_marks_2)

            acca_result_obj = request.env["logic.acca.results"].sudo().create({
                'student_name': kw.get('student_name'),
                'acca_reg_no': kw.get('acca_reg_no'),
                'whatsapp_no': kw.get('whatsapp_no'),
                'branch': kw.get('branch'),
                'result_window': kw.get('result_window'),
            })

            for i in range(len(selected_paper_ids_1)):
                student_result_id = request.env["logic.acca.student.result"].sudo().create({
                    'paper_id': int(selected_paper_ids_1[i]),
                    'acca_result_id': acca_result_obj.id,
                    'marks': exam_marks_1[i],
                }).id
                acca_result_obj.write({
                    'exam1_results': [(4,int(student_result_id))]
                })

            for i in range(len(selected_paper_ids_2)):
                student_result_id = request.env["logic.acca.student.result"].sudo().create({
                    'paper_id': int(selected_paper_ids_2[i]),
                    'acca_result_id': acca_result_obj.id,
                    'marks': exam_marks_2[i],
                }).id
                acca_result_obj.write({
                    'exam2_results': [(4,int(student_result_id))]
                })
            return request.render("logic_student_forms.student_form_submit_successful", {})

        except Exception as e:
            logger.error(e)
            return request.render("logic_student_forms.student_form_error", {})