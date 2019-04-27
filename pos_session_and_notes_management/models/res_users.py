# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Users(models.Model):
    _inherit = 'res.users'

    is_waiter = fields.Boolean(string="Waiter")
    is_cashier = fields.Boolean(string="Cashier")
