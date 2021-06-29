from odoo import models, fields, api

class Lib_card(models.Model): 
    _inherit = 'op.library.card'

    active = fields.Boolean(string="Active")
