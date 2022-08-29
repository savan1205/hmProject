from odoo import fields, models,api

class HospitalDepartment(models.Model):
    _name = "hospital.department"
    _description = "hospital department"

    department = fields.Char(string="department")
    # doctor_id=fields.Char(depends="hospital.doctor",string="Doctor")
    head = fields.Char(string="head")
    floor = fields.Char(string="floor")