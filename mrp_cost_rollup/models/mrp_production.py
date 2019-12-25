# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def _cal_price(self, consumed_moves):
        self.ensure_one()
        fp_move = self.move_finished_ids.filtered(
            lambda x: x.state not in ["done", "cancel"]
            and x.quantity_done != 0.0
            and x.product_id.cost_method in ["fifo", "average"]
        )
        if fp_move:
            fp_move.ensure_one()
            fp_move.value = sum(consumed_moves.mapped("value")) * -1
            qty_done = fp_move.product_uom._compute_quantity(
                fp_move.quantity_done, fp_move.product_id.uom_id
            )
            fp_move.price_unit = fp_move.value / qty_done
        return super(MrpProduction, self)._cal_price(consumed_moves)
