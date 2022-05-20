# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class Company(models.Model):
    _inherit = 'res.company'

    process_costing = fields.Selection([('manually', 'Manually'), ('workcenter', 'Work-Center')],
                                       string="Process Costing Method", default="manually")


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    process_costing = fields.Selection(string="Process Costing Method", related="company_id.process_costing",
                                       readonly=False)


class MrpWorkcenter(models.Model):
    _inherit = 'mrp.workcenter'

    labour_costs_hour = fields.Float(string='Labour Costs per hour', help="Specify cost of Labour per hour.",
                                     default=0.0)
    overhead_cost_hour = fields.Float(string="Overhead Costs per hour", help="Specify cost of Overhead per hour.",
                                      default=0.0)
