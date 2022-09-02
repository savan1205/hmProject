from odoo import fields, models, api
from datetime import date, datetime

class PatientRoomNum(models.Model):
    _name = "hospital.roomnum"
    _description = "Hospital Room"


    # name = fields.Many2one(comodel_name="hospital.patient", string="Of patient")
    roomType = fields.Selection([
        ('001','001'),('002','002'),('003','003'),('004','004'),('005','005'),('006','006'),
        ('101','101'),('102','102'),('103','103'),('104','104'),('105','105'),('106','106'),
        ('101','101'),('102','102'),('103','103'),('104','104'),('105','105'),('106','106'),
        ('201','201'),('202','202'),('203','203'),('204','204'),('205','205'),('206','206')],
        string="Select Room")

    availability=fields.Selection([
        ('Available','Available'),('Not Available','Not Available')]
        ,string="Availablity: ")
    
    Sanitized=fields.Selection([('Yes','Yes'),('No','No')],string = "Sanitized: ") 

    airConditioned=fields.Selection([('Ac','Ac'),
        ('Non ac','Non ac')],string="Room Type")   


    