from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    rs_observations = fields.Char(string='Description')

    @api.model
    def create(self, values):
        # Add code here
        #import wdb;wdb.set_trace()
        return super(ClassName, self).create(values)
