# -*- coding: utf-8 -*-
from odoo import api, fields, models
class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    patient_id = fields.Many2one(string = "Patient", comodel_name='hospital.patient')

