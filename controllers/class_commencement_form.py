from odoo import http
from odoo.http import request
import base64
from odoo.exceptions import UserError
from  datetime import date
import logging


class ClassCommencementForm(http.Controller):
    @http.route(['/class_commencement'], type='http', auth="public", website=True)
    def class_commencement_form(self, **kw):
        paper_option_objs = request.env['logic.paper.options'].sudo().search([])
        paper_options = []
        for paper_obj in paper_option_objs:
            paper_option = {'id':paper_obj.id,'paper_name':paper_obj.name}
            paper_options.append(paper_option)

        return request.render("logic_student_forms.class_commencement_form_template", {'paper_options':paper_options})

    @http.route(['/class_commencement/submit'], type='http', auth="public", website=True, csrf=False, method=['POST'])
    def class_commencement_form_submit(self, **kw):
        logger = logging.getLogger("Error Logger")

        try:
            selected_paper_ids = request.httprequest.form.getlist('paper_options')
            selected_modes = request.httprequest.form.getlist('class_modes')
            logger.error(selected_paper_ids)
            logger.error(selected_modes)
            dob = kw.get('dob').split('-')
            dob = date(year=int(dob[0]),month=int(dob[1]), day=int(dob[2]))
            commence_obj = request.env["logic.class.commencement"].sudo().create({
                'student_name': kw.get('student_name'),
                'email': kw.get('email'),
                'batch': kw.get('batch'),
                'acca_reg_no': kw.get('acca_reg_no'),
                'dob': dob,
                'student_whatsapp': kw.get('student_whatsapp'),
                'parent_whatsapp': kw.get('parent_whatsapp'),
                'attempt': kw.get('attempt'),
            })
            for i in range(len(selected_modes)-1,-1,-1):
                if selected_modes[i]=='':
                    selected_modes.pop(i)
            for i in range(len(selected_paper_ids)):
                paper_mode_option = request.env["logic.paper.options.mode"].sudo().search([('paper_id','=',int(selected_paper_ids[i])),('class_mode','=',selected_modes[i])])
                if paper_mode_option:
                    paper_moded_id = paper_mode_option[0].id
                else:
                    paper_moded_id = request.env["logic.paper.options.mode"].sudo().create({
                        'name': request.env['logic.paper.options'].browse(int(selected_paper_ids[i])).name ,
                        'paper_id': int(selected_paper_ids[i]),
                        'class_mode': selected_modes[i],
                    }).id
                commence_obj.write({
                    'paper_options': [(4,int(paper_moded_id))]
                })

            return request.render("logic_student_forms.student_form_submit_successful", {})
        except Exception as e:
            logger.error(e)
            return request.render("logic_student_forms.student_form_error", {})