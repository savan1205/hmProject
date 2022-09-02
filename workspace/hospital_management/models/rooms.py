from odoo import fields, models, api
from datetime import date, datetime

class PatientRoom(models.Model):
    _name = "patient.room"
    _description = "patient Room"


    name = fields.Many2one(comodel_name="hospital.patient", string="Of patient")
    roomType = fields.Selection([
        ('C.T.V.S-ICU','C.T.V.S-ICU'),
        ('CCU','CCU'),
        ('BURN UNIT','BURN UNIT'),
        ('HDU ICU','HDU ICU'),
        ('PICU','PICU'),
        ('NURSERY','NURSERY'),
        ],string="Room Type")
    

    # costOf = fields. 
    price=fields.Integer(compute='_compute_price',string="Price: ")

    # bill = fields.Integer(string="Amount")

    # duration


    @api.depends('roomType')
    def _compute_price(self):
        for rec in self:
            rec.price=0
            if rec.roomType:
                if rec.roomType=='C.T.V.S-ICU':
                    rec.price=13250
                elif rec.roomType=='CCU':
                    rec.price=13250
                elif rec.roomType=='BURN UNIT':
                    rec.price=11250
                elif rec.roomType=='HDU ICU':
                    rec.price=11250
                elif rec.roomType=='PICU':
                    rec.price=9450
                elif rec.roomType=='NURSERY':
                    rec.price=6050
                # elif rec.roomType=='Spl. Economy (Four Bedded)':
                #     rec.price=4400
                # elif rec.roomType=='Economy':
                #     rec.price=3200
                # else:
                #     rec.price=0    



    

    