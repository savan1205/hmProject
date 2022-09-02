from odoo import fields, models,api
from datetime import date, datetime

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description="hospital patient"


    name = fields.Char(string="Name")
    
    birthdate = fields.Date(string="birthdate")
    
    age = fields.Integer(compute="_compute_age",string="Age",store=True)

    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')],string="Gender")
    city = fields.Char(string="City")
    
    age_group = fields.Char(string="Age Group",compute="_set_age",store=True)
    
    catagory = fields.Char(compute="_set_catagory", string="age group")
    
   
    females = fields.Char(compute="_compute_patients",string="meaningful")
 
    # mob with create method   
    mo_number = fields.Char(string="Mobile number:")
    doc_id = fields.Many2one(comodel_name="doctor.name",string="With Doctor")
        
   # appointment number from appointments table
    # pAppID = fields.Integer(compute="get_ID" ,string="Appointment Number")
    
    refBy_ids = fields.Many2many(comodel_name="doctor.name", string="Refered By: ")

    blood = fields.Selection([
        ('a+','A+'),
        ('a-','A-'),
        ('b+','B+'),
        ('b-','B-'),
        ('o+','O+'),
        ('o-','O-'),
        ('ab+','AB+'),
        ('ab-','AB-'),
        ],string="Blood group")



                            # Functions

    def get_ID(self):
        for rec in self:
            idNumber=self.env['hospital.appointments'].search([('name_id','=',rec.id)])
            rec.pAppID=idNumber.appId 


    def unlink(self):
        for Del in self:
            patients = self.env["hospital.appointments"].search([('name_id','=',Del.name)]) 
            print("----------======/////////@@@@@@",patients)
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



       
