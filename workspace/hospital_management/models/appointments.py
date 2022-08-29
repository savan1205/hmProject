from odoo import fields, models,api
from datetime import date, datetime


class HospitalAppointments(models.Model):
    _name = "hospital.appointments"
    _description = "Hospital Appointments"
    # _rec_name="ref"

    name_id=fields.Many2one(comodel_name="hospital.patient",string="Patient Name:")
    date=fields.Datetime(string="Date")
    gender = fields.Selection(related="name_id.gender",string="Gender")
    doctor_id=fields.Many2one(comodel_name="doctor.name",string="With Doctor:")
    appId= fields.Integer(compute="_compute_refid",string="AppointID")
    stat=fields.Selection([
        ('active','Active'),
        ('inConsultation','InConsultation'),
        ('cancelled','Cancelled'),
        ('draft','Draft')
        ])


    def _compute_refid(self): 
        print("seeeeeeeeeeeeeeeellllllllffffffff",self)
        for value in self:
            print("---=-=-=-].[/]'.'/][./]'./][.]'/]./[.'/].[/=-=-=-=-",value)
            reffer=self.env["hospital.appointments"].browse(value.id)
            value.appId=reffer    


    

    
    