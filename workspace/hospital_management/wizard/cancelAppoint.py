from odoo import fields, models,api
from odoo.exceptions import ValidationError

class CancelAppointWizard(models.TransientModel):
    _name = "cancel.appointment"
    _description = "Cancel Appointment"
    _rec_name="patient_id"

    patient_id = fields.Many2one(comodel_name="hospital.appointments", string="patient",compute="cal_pat")
    reason = fields.Char(string="reason")
    
   
    # def cal_pat(self):



    def cancel_appointment(self):
        print("________________",self.patient_id.stat)
        print("________________",self.patient_id)
        if self.patient_id.stat == 'draft':
            self.patient_id.stat = 'cancelled'
        else:
            raise ValidationError(("You can only cancel an Draft appointment."))



        return{
        'type':'ir.actions.act_window',
        'name':'Appointments',
        'res_model':'hospital.appointments',
        # 'domain':[('doctor_id','=',self.name)],
        'view_mode':'tree,form',
        'target':'current',
        # 'context': {'parent_obj': self.id}
         }