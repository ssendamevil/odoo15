# -*- coding: utf-8 -*-


{
    'name': 'Hospital',
    'version': '1.0.0',
    "author": "A. Orynbassar",
    'category': "Hospital",
    'summary': "Hospital management system",
    'description': """Hospital management system""",
    'depends': ["base"],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patient_view.xml",
    ],
    'license': 'LGPL-3',
    "application": True,
    "installable": True,
    "auto-install": False
}
