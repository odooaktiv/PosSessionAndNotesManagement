# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PosConfig(models.Model):
    _inherit = 'pos.config'

    user_id = fields.Many2one('res.users', string="Users")
