from odoo import fields, models,api

class HospitalDegrees(models.Model):
    _name = "hospital.degrees"
    _description = "hospital degrees"


    name = fields.Char(string="degrees")
    from_city=fields.Char(string="From city")
    # degree_count=fields.cha(string="degree count")

    