from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def message_post(self, **kwargs):
        """
        Interceptar message_post para evitar errores cuando se llama
        desde un onchange.
        
        En Odoo, message_post requiere que el registro esté guardado en la BD,
        pero durante un onchange el registro es "virtual" (NewId).
        
        Esta solución permite que action_update_prices se ejecute completamente
        (con toda su lógica de precios, descuentos, y herencias de otros módulos)
        pero evita el error al intentar publicar en el chatter.
        
        Cuando el usuario hace clic manualmente en "Actualizar precios",
        funciona normalmente y SÍ publica el mensaje en el chatter.
        """
        if self.env.context.get('from_onchange_auto_update'):
            # Si venimos de onchange, no publicar mensaje y retornar vacío
            # Esto evita el error: "Posting a message should be done on a business document"
            return self.env['mail.message']
        return super().message_post(**kwargs)
