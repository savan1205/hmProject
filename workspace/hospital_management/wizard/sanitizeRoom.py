from odoo import fields, models,api
from odoo.exceptions import ValidationError

class CancelAppointWizard(models.TransientModel):
    _name = "sanitize.room"
    _description = "Sanitize Room"
    _rec_name="patient_id"

    room_num_ids = fields.Many2many(comodel_name="hospital.roomnum", string="Room Number",compute="get_room")
    

    def _get_room(self);
        for rec in self:
            for res in rec.room_num_ids:
                res.Sanitized='Yes'
                