from odoo import fields, models,api
from datetime import date, datetime

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description="hospital patient"


    name = fields.Char(string="Name")
    birthdate=fields.Date(string="birthdate")
    age = fields.Integer(compute="_compute_age",string="Age",store=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    city = fields.Char(string="City")
    age_group=fields.Char(string="Age Group",compute="_set_age",store=True)
    catagory=fields.Char(compute="_set_catagory", string="age group")
    

    tockenID=fields.Integer(comodel_name="hospital.appointments",string='Your Appoint ID is: ')
    pAppID=fields.Integer(related="tockenID.appId" ,string="appID")
    
    females= fields.Char(compute="_compute_patients",string="meaningful")
 
    mo_number=fields.Char(string="Mobile number:")
    doc_id=fields.Many2one(comodel_name="doctor.name",string="With Doctor")
    
    # symptoms_ids=fields.Many2many('hospital.symptoms',string="symptoms")
    # name_id=fields.One2many(comodel_name="doctor.name",string="Reference")
    # age_group=fields.Char(string="age_group",compute="_set_age",store=True)
    # ref=fields.Many2one(comodel_name="hospital.appointments",string="appointment id")


    def unlink(self):
        for Del in self:
            patients = self.env["hospital.appointments"].search([('name_id','=',Del.name)]) 
            res = super(HospitalPatient,self).unlink()
            patients.unlink()
            return res 



    def _compute_patients(self):
        # print('Self---------',self)
        for rec in self:
            # print('Current record---Data computed for',rec)
            # print('Doctor name---Data computed for',rec.name)
            # rec.no_of_patients_count = 0
            patients = self.env['hospital.patient'].search([('gender','=','female')])
            for a in patients:
                print("_____________",a.name)
            # doctors = rec.search_count([('type_id','=',self.env.ref('hospital_Managment.type_oncologist').id)])
            # print(doctors,"---------doctors--------\n\n")
            # rec.no_of_patients = patients
            print('Number of  female Patients-----',patients)
        rec.testName=patients



    @api.depends('birthdate')
    def _compute_age(self):
        for rec in self:
            rec.age=0
            # rec.age='demo'
            if rec.birthdate:
                birthdate=rec.birthdate
                today=date.today()
                age= today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                print("ss",age)
                rec.age=age

    @api.depends("age")               
    def _set_catagory(self):
        catagory=""
        for catag in self:
            if catag.age<18:
                catag.catagory="Minor"
            else:
                catag.catagory="major"

    @api.model
    def create(self,vals):
        if vals['mo_number']==False:
            vals['mo_number']=' '
        vals['mo_number']="+91 "+str(vals['mo_number'])
        return super(HospitalPatient,self).create(vals)

   
    def write(self,vals):
        if self.mo_number:
            vals['mo_number']="+91 "+str(vals['mo_number'])
            return super(HospitalPatient,self).write(vals)
        else:
            return super(HospitalPatient,self).write(vals)

    # def confirm(self):
    #     for test in self:
    #         patients=self.env["hospital.patient"].search([]) 
    #         print("-----patients----",patients)                


    def _compute_patients_count(self):
        print('Self---------',self)
        for rec in self:
            print('Current record---Data computed for',rec)
            print('Doctor name---Data computed for',rec.name)
            rec.no_of_patients_count = 0
            # rec.degree_count = len(rec.degree_ids.ids)
            patients = self.env['hospital.patient'].search_count([('doctor_id','=',rec.id)])
            # doctors = rec.search_count([('type_id','=',self.env.ref('hospital_Managment.type_oncologist').id)])
            # print(doctors,"---------doctors--------\n\n")
            rec.no_of_patients_count = patients
            print('Number of Patients-----',rec.no_of_patients_count)


    # def _compute_doctors(self):
    #     print('Self---------',self)
    #     for record in self:
    #         print('Current record---Data computed for',record)
    #         print('Doctor name---Data computed for',record.name)
    #         rec.no_of_patients_count = 0
    #         # # rec.degree_count = len(rec.degree_ids.ids)
    #         # patients = self.env['hospital.patient'].search_count([('doctor_id','=',rec.id)])
    #         # # doctors = rec.search_count([('type_id','=',self.env.ref('hospital_Managment.type_oncologist').id)])
    #         # # print(doctors,"---------doctors--------\n\n")
    #         # rec.no_of_patients_count = patients
    #         # print('Number of Patients-----',rec.no_of_patients_count) 
    #         record.testName="demo"       