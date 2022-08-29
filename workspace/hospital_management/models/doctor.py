from odoo import fields, models,api

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description="hospital doctor"

    name = fields.Char(string="Name")
    speciality = fields.Char(string="speciality")
    degree = fields.Char(string="Degree")