from odoo import fields, models,api

class HospitalEmployees(models.Model):
    _name = "hospital.employees"
    _description = "Hospital Employees"


    name = fields.Char(string="employees")
    

    