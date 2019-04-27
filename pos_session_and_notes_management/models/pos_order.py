# -*- coding: utf-8 -*-

from odoo import api, models, fields


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    note = fields.Char(string='Note')

    @api.model
    def create(self, vals):
        pos_order_line = super(PosOrderLine, self).create(vals)
        pos_order_line.note = vals.get('note') or False
        return pos_order_line
