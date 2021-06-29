from odoo import models, fields, api

class Authors(models.Model): 
    _inherit = 'op.author'

    active = fields.Boolean(string="Active")

