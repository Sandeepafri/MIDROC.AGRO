# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################

from odoo import models,fields


class mrp_production(models.Model):
    _inherit = 'mrp.production'

    def calculate_report_data(self):
        data_dict = {}
        for move in self.move_raw_ids:
            data_dict.setdefault(move.product_id,{'product_uom':'','product_uom_qty':0.00,'quantity_done':0.00,'move_actual_qty':0.00,'product_name':''})
            data_dict[move.product_id]['product_uom'] = move.product_uom.name
            data_dict[move.product_id]['product_uom_qty'] += move.product_uom_qty
            data_dict[move.product_id]['quantity_done'] += move.quantity_done
            data_dict[move.product_id]['move_actual_qty'] += move.move_actual_qty
            data_dict[move.product_id]['product_name'] = move.product_id.display_name
        return data_dict.values()

    def _get_move_raw_values(self, product_id, product_uom_qty, product_uom, operation_id=False, bom_line=False):
        res = super(mrp_production,self)._get_move_raw_values(product_id, product_uom_qty, product_uom, operation_id, bom_line)
        if self.state and self.state in ['draft','confirmed']:
            res['move_actual_qty'] = product_uom_qty
        return res


class stock_move(models.Model):
    _inherit = 'stock.move'

    move_actual_qty = fields.Float('Move actual Qty',digits='Product Unit of Measure',copy=False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: