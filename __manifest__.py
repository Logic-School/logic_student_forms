{
    'name': "Student Forms",
    'author': 'Rizwaan',
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base','website','logic_base','faculty', 'logic_digital_tracker'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'controllers/winners_meet.xml',
        'controllers/hock_access.xml',
        'controllers/text_material.xml',
        'controllers/class_commencement.xml',
        'controllers/faculty_feedback.xml',
        'controllers/result_service_template.xml',
        'controllers/acca_results.xml',
        'views/student_forms.xml',
        'views/student_forms_2.xml',
        'views/paper_options.xml',
        'views/link_generation_views.xml',
        'data/paper_options.xml',
        'views/crash_form_links.xml',
        'controllers/crash_mentoring_form.xml',
        'controllers/crash_results.xml',
        'views/crash_registration_form.xml',
        'views/crash_result_form.xml',
        'views/crash_mentoring_form.xml',
        'controllers/crash_registration.xml',
    ],
    'demo': [],
    'summary': "Student Forms",
    'description': "",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}