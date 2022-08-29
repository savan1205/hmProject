
{
    'name': 'Hospital Management',
    'sequence':-500,
    'version': '1.0',
    'category': 'hospital',
    'summary': 'hospital management',
    'description': """
This module contains all the common features of Hospital Management.
    """,
    'depends': [],
    'data':[
    'security/ir.model.access.csv',
    'views/menu.xml',
    'views/appointments.xml',
    'views/patientView.xml',
    'views/doctorView.xml',
    'views/departmentView.xml',
    'views/docName.xml',
    'views/degrees.xml',

    # 'views/hospital.xml',
    ],

    'demo':[],
    'installable':True,
    'auto-install':False,

    'license': 'LGPL-3',
}
