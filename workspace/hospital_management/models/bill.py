from odoo import fields, models,api

class PatientBill(models.Model):
    _name = "patient.bill"
    _description = "patient Bill"


    name = fields.Char(string="for patient")
    

    