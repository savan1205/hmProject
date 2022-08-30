from odoo import fields, models,api

class PatientLoan(models.Model):
    _name = "patient.loan"
    _description = "patient Loan"


    name = fields.Char(string="for patient")
    pAmount=fields.Integer(string="Principal Amount")
    duration=fields.Integer(string="duration ")
    roi=fields.Char(string="rate of interest",default='%5')
    total_amount=fields.Integer(compute="_compute_amount",string="Total Amount")
    
    def _compute_amount(self):
        total_amount=0
        for i in self:
            x=1+((i.roi)*(i.duration))
            i.total_amount=(i.pAmount)*x
        return i.total_amount    

    