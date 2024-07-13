from odoo import http
from odoo.http import request
from PIL import Image, UnidentifiedImageError
import base64
import io
import xlsxwriter
import logging
from odoo.http import Controller, request, route, content_disposition



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
            attach_result = kw.get('attach_result')
            request.env["logic.crash.result.forms"].sudo().create({
                'student_name': kw.get('student_name'),
                'mobile_number': kw.get('contact_number'),
                # 'email_from': post.get('email'),
                'group': kw.get('part_group'),
                'attach_result': base64.b64encode(attach_result.read()) if type(attach_result) != str else False,
                'student_photo': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,
                'level': kw.get('part'),
                # 'attach_result_download': base64.b64encode(attach_result.read()) if type(attach_result) != str else False,
                # 'student_photo_download': base64.b64encode(student_photo.read()) if type(student_photo) != str else False,
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


class InvoiceExcelReportController(http.Controller):
    @http.route([
        '/crash/results',
    ], type='http', auth="user", csrf=False)
    def get_crash_excel_report(self, **args):
        ids = args.get('ids', '')
        if not ids:
            return request.not_found()

        active_ids = list(map(int, ids.split(',')))
        response = request.make_response(
            None,
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition('Crash_Report' + '.xlsx'))
            ]
        )
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        header_format = workbook.add_format({
            'bold': True,
            'font_size': 12,
            'font_color': 'white',
            'bg_color': '#2C3E50',  # Background color
            'align': 'center',
            'valign': 'vcenter',
        })

        # Prepare excel sheet styles and formats
        sheet = workbook.add_worksheet("Crash Results")
        headers = [
            'No.', 'Student Name', 'Student Photo', 'Attach Result', 'Level', 'Mobile Number', 'Group', 'Remarks'
        ]
        for col_num, header in enumerate(headers):
            sheet.write(0, col_num, header, header_format)

        row = 1
        number = 1
        # Get data for the report
        Model = request.env['logic.crash.result.forms'].sudo()
        report_lines = Model.get_report_lines(active_ids)
        # Write the report lines to the excel document
        for line in report_lines:
            sheet.set_row(row, 100)  # Adjust the row height to fit images
            sheet.write(row, 0, number)
            sheet.write(row, 1, line['student_name'])

            # Manage the size of the student photo
            if line.get('student_photo'):
                try:
                    student_photo_data = io.BytesIO(base64.b64decode(line['student_photo']))
                    student_photo_image = Image.open(student_photo_data)
                    student_photo_path = f'/tmp/student_photo_{row}.png'
                    student_photo_image.save(student_photo_path)

                    # Set desired width and height for images
                    image_width = 100
                    image_height = 100
                    x_scale = image_width / student_photo_image.width
                    y_scale = image_height / student_photo_image.height

                    sheet.insert_image(row, 2, student_photo_path, {'x_scale': x_scale, 'y_scale': y_scale})
                except (base64.binascii.Error, UnidentifiedImageError):
                    # Handle invalid image data
                    sheet.write(row, 2, 'Invalid image')

            # Manage the size of the attached result image
            if line.get('attach_result'):
                try:
                    attach_result_data = io.BytesIO(base64.b64decode(line['attach_result']))
                    attach_result_image = Image.open(attach_result_data)
                    attach_result_path = f'/tmp/attach_result_{row}.png'
                    attach_result_image.save(attach_result_path)

                    # Set desired width and height for images
                    image_width = 100
                    image_height = 100
                    x_scale = image_width / attach_result_image.width
                    y_scale = image_height / attach_result_image.height

                    sheet.insert_image(row, 3, attach_result_path, {'x_scale': x_scale, 'y_scale': y_scale})
                except (base64.binascii.Error, UnidentifiedImageError):
                    # Handle invalid image data
                    sheet.write(row, 3, 'Invalid image')

            sheet.write(row, 4, line.get('level', ''))
            sheet.write(row, 5, line.get('mobile_number', ''))
            sheet.write(row, 6, line.get('group', ''))
            sheet.write(row, 7, line.get('remarks', ''))

            row += 1
            number += 1

        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
        return response
