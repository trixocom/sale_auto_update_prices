{
    'name': 'Sale Auto Update Prices',
    'version': '18.0.1.0.2',
    'category': 'Sales',
    'summary': 'Actualiza precios automáticamente al cambiar cantidades en líneas de venta',
    'description': """
Sale Auto Update Prices
=======================

Este módulo ejecuta la acción "Actualizar precios" automáticamente
cuando se cambia la cantidad de una línea de pedido de venta.

Características:
----------------
* Actualización automática de precios al cambiar cantidades
* Mantiene la actualización de descuentos según la lista de precios
* Compatible con módulos que heredan action_update_prices (como sale_ux)
* No genera mensajes en el chatter durante el onchange
* Solo funciona en estados draft y sent

Funcionamiento:
---------------
Cuando cambias la cantidad en una línea de orden de venta, el módulo:
1. Detecta el cambio en product_uom_qty
2. Llama a action_update_prices() con un contexto especial
3. Actualiza precios y descuentos según la lista de precios actual
4. Evita publicar mensajes en el chatter (que causaría error en onchange)

Autor: Trixocom
    """,
    'author': 'Trixocom',
    'website': 'https://www.trixocom.com',
    'depends': ['sale_management'],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
