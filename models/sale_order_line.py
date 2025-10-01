from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_uom_qty')
    def _onchange_product_uom_qty_auto_update(self):
        """
        Cuando se cambia la cantidad, se actualizan los precios y descuentos
        automáticamente sin generar mensaje en el chatter.
        
        Este método se ejecuta en el cliente (onchange) y marca el contexto
        para que action_update_prices no intente publicar en el chatter.
        """
        if self.order_id and self.order_id.state in ['draft', 'sent']:
            # Marcar en el contexto que venimos de onchange para evitar message_post
            self.order_id.with_context(
                from_onchange_auto_update=True
            ).action_update_prices()
