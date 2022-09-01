from odoo import fields, models, api
from datetime import date, datetime

class PatientBill(models.Model):
    _name = "patient.bill"
    _description = "patient Bill"


    name_id = fields.Many2one(comodel_name="hospital.patient", string="Of patient")
    billDate = fields.Datetime(string="Bill Date")
    charge=fields.Integer(string="Charge")
    bill = fields.Integer(compute="get_charge",string="Amount")
    
    # @api.depends('name_id')
    def get_charge(self):
        for rec in self:
            pricee=self.env['patient.room'].search([('name','=',rec.name_id.id)])
            print("____=========////////@@@@@@@@@@@",pricee)
            rec.bill=pricee.price 