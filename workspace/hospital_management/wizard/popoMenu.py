from odoo import fields, models,api

class WizardPopoMenu(models.TransientModel):
    _name = "popoMenu.wizard"
    _description = "Popo Menu"

    name = fields.Char(string="reason", required=True)
    

    