from odoo import fields, models

class HospitalProfile(models.Model):
    _name = "hospital.profile"

    name = fields.Char("Hospital Name", required=True)
    email = fields.Char('Email', required=True)
    phone = fields.Char("Phone", required=True)