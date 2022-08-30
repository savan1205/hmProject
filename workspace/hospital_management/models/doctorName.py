from odoo import fields, models,api

class HospitalDoctorName(models.Model):
    _name = "doctor.name"
    _description="doctor name"

    name = fields.Char(string="Name")
    # speciality_id = fields.Many2one(comodel_name="",string="speciality")
    degrees_ids = fields.Many2many(comodel_name="hospital.degrees",string="Degree")
    belongsTo = fields.Selection([('Yes','yes'),('No','no')],string="Belongs to this Hospital") 

    no_of_apps=fields.Integer(compute="_compute_appointments",string ="No of Appointments")


    def _compute_appointments(self):
        no_of_apps=0
        for appoints in self:
            # print("_________________",self)
            appointments=self.env["hospital.appointments"].search_count([("doctor_id","=",appoints.name)])
            appoints.no_of_apps=appointments


    def action_open_patients(self):
        return {
            'type':'ir.actions.act_window',
            'name':'Patients',
            'res_model':'hospital.appointments',
            'domain':[('doctor_id','=',self.name)],
            'view_mode':'tree,form',
            'target':'current'

        }            


    def action_count_degrees(self):
        for i in self:
            # totalDegree=0
            degcount= len(i.degrees_ids.ids)
            print('==============,------------',degcount)
            # i.totalDegree=degcount    
        






