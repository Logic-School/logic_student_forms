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

class ResultServiceForm(http.Controller):
    @http.route(['/result_service_template'], type='http', auth="public", website=True)
    def result_service_form(self, **kw):
        paper_option_objs = request.env['logic.paper.options'].sudo().search([])
        paper_options = []
        for paper_obj in paper_option_objs:
            paper_option = {'id':paper_obj.id,'paper_name':paper_obj.name}
            paper_options.append(paper_option)

        return request.render("logic_student_forms.result_service_form_template", {'paper_options':paper_options})
    
    @http.route(['/result_service_template/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def result_service_form_submit(self, **kw):
        logger = logging.getLogger("Error Logger")
        try:
            selected_paper_ids_1 = request.httprequest.form.getlist('paper_options_1')
            selected_modes_1 = cleaned_list(request.httprequest.form.getlist('class_modes_1'))

            selected_paper_ids_2 = request.httprequest.form.getlist('paper_options_2')
            selected_modes_2 = cleaned_list(request.httprequest.form.getlist('class_modes_2'))

            selected_paper_ids_3 = request.httprequest.form.getlist('paper_options_3')
            selected_modes_3 = cleaned_list(request.httprequest.form.getlist('class_modes_3'))

            logger.error("First Exam")
            logger.error(selected_paper_ids_1)
            logger.error(selected_modes_1)

            # logger.error("Second Exam")
            # logger.error(selected_paper_ids_2)
            # logger.error(selected_modes_2)

            # logger.error("Third Exam")
            # logger.error(selected_paper_ids_3)
            # logger.error(selected_modes_3)
            dob = kw.get('dob').split('-')
            dob = date(year=int(dob[0]),month=int(dob[1]), day=int(dob[2]))

            result_service_obj = request.env["logic.result.service"].sudo().create({
                'first_name': kw.get('first_name'),
                'last_name': kw.get('last_name'),
                'email': kw.get('email'),
                'phone': kw.get('phone'),
                'acca_reg_no': kw.get('acca_reg_no'),
                'dob': dob,
            })

            for i in range(len(selected_paper_ids_1)):
                paper_mode_option = request.env["logic.paper.options.mode"].sudo().search([('paper_id','=',int(selected_paper_ids_1[i])),('class_mode','=',selected_modes_1[i])])
                if paper_mode_option:
                    paper_moded_id = paper_mode_option[0].id
                else:
                    paper_moded_id = request.env["logic.paper.options.mode"].sudo().create({
                        'name': request.env['logic.paper.options'].browse(int(selected_paper_ids_1[i])).name ,
                        'paper_id': int(selected_paper_ids_1[i]),
                        'class_mode': selected_modes_1[i],
                    }).id
                result_service_obj.write({
                    'exam_papers_1': [(4,int(paper_moded_id))]
                })

            for i in range(len(selected_paper_ids_2)):
                paper_mode_option = request.env["logic.paper.options.mode"].sudo().search([('paper_id','=',int(selected_paper_ids_2[i])),('class_mode','=',selected_modes_2[i])])
                if paper_mode_option:
                    paper_moded_id = paper_mode_option[0].id
                else:
                    paper_moded_id = request.env["logic.paper.options.mode"].sudo().create({
                        'name': request.env['logic.paper.options'].browse(int(selected_paper_ids_2[i])).name ,
                        'paper_id': int(selected_paper_ids_2[i]),
                        'class_mode': selected_modes_2[i],
                    }).id
                result_service_obj.write({
                    'exam_papers_2': [(4,int(paper_moded_id))]
                })

            for i in range(len(selected_paper_ids_3)):
                paper_mode_option = request.env["logic.paper.options.mode"].sudo().search([('paper_id','=',int(selected_paper_ids_3[i])),('class_mode','=',selected_modes_3[i])])
                if paper_mode_option:
                    paper_moded_id = paper_mode_option[0].id
                else:
                    paper_moded_id = request.env["logic.paper.options.mode"].sudo().create({
                        'name': request.env['logic.paper.options'].browse(int(selected_paper_ids_3[i])).name ,
                        'paper_id': int(selected_paper_ids_3[i]),
                        'class_mode': selected_modes_3[i],
                    }).id
                result_service_obj.write({
                    'exam_papers_3': [(4,int(paper_moded_id))]
                })
            return request.render("logic_student_forms.student_form_submit_successful", {})

        except Exception as e:
            logger.error(e)
            return request.render("logic_student_forms.student_form_error", {})

