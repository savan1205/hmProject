from odoo import fields, models,api

class HospitalReference(models.Model):
    _name = "hospital.reference"
    _description = "Reference"

    ref_id=fields.Many2one(comodel_name="doctor.name",string="Ref Name:")
    

    