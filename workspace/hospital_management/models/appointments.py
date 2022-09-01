from odoo import fields, models,api
from datetime import date, datetime
from odoo.exceptions import ValidationError


class HospitalAppointments(models.Model):
    _name = "hospital.appointments"
    _description = "Hospital Appointments"
    # _rec_name="ref"

    name_id=fields.Many2one(comodel_name="hospital.patient",string="Patient Name:")
    date=fields.Datetime(string="Date")
    gender = fields.Selection(related="name_id.gender",string="Gender")
    doctor_id=fields.Many2one(comodel_name="doctor.name",string="With Doctor:")
    
    appId= fields.Integer(compute="_compute_refid",string="Appointment number")
    progress= fields.Integer(compute="_compute_progress",string="progress")
    
    stat=fields.Selection([
        ('done','Done'),
        ('inConsultation','InConsultation'),
        ('cancelled','Cancelled'),
        ('draft','Draft')
        ])

    @api.depends('stat')
    def _compute_progress(self):
        for prog in self :
            # if self.stat:  
                if prog.stat=="cancelled":
                    progress=0
                elif prog.stat=="draft":
                    progress=25
                elif prog.stat=="inConsultation":
                    progress=50
                elif prog.stat=="done":
                    progress=100
                else:
                    progress=0
        prog.progress=progress            

    def _compute_refid(self): 
        # print("seeeeeeeeeeeelllllfffff",self)
        for value in self:
            # print("FFFFFFFFFFFFFFFFFFFFFFFFF ",value)
            reffer=self.env["hospital.appointments"].browse(value.id)
            value.appId=reffer    

   
    def unlink(self):
        if self.stat=='inConsultation':
            raise ValidationError(("You cannot delete an InConsultation appointment."))   
        else:
            return super(HospitalAppointments,self).unlink()


    @api.model        
    def default_get(self,fields):
        resss= super(HospitalAppointments,self).default_get(fields)
        return resss        