from odoo import fields, models,api

class PatientLoan(models.Model):
    _name = "patient.loan"
    _description = "patient Loan"


    name = fields.Many2one(comodel_name="hospital.patient",string="for patient")
    pAmount=fields.Float(string="Principal Amount")
    duration=fields.Float(string="Duration (in Years)")
    roi=fields.Integer(string="rate of interest",default=5,readonly=True)
    total_amount=fields.Float(compute="_compute_amount",string="Total Amount")
    
    state=fields.Selection([
        ('active','Active'),
        ('inConsultation','InConsultation'),
        ('cancelled','Cancelled'),
        ('draft','Draft')
        ])
    def _compute_amount(self):
        total_amount=0
        for i in self:
            x=1+(((i.roi)*(i.duration))/100)
            final_amount=(i.pAmount)*x
        i.total_amount=final_amount    

        # i.total_amount=x
        # print("----------_________---_---___",x)    

    