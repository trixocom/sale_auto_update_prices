# Sale Auto Update Prices

Módulo que actualiza automáticamente los precios de las líneas de venta cuando se cambia la cantidad.

## Descripción

Este módulo ejecuta la acción "Actualizar precios" automáticamente cuando el usuario cambia la cantidad (`product_uom_qty`) de una línea de pedido de venta.

### Características

- ✅ Actualización automática de precios al cambiar cantidades
- ✅ Mantiene la actualización de descuentos según la lista de precios
- ✅ Compatible con módulos que heredan `action_update_prices` (como `sale_ux` de ADHOC)
- ✅ No genera mensajes en el chatter durante el cambio automático
- ✅ Solo funciona en estados `draft` y `sent`
- ✅ No afecta el comportamiento manual del botón "Actualizar precios"

## Instalación

1. Clonar este repositorio en tu carpeta de addons de Odoo:
```bash
cd /ruta/a/tus/addons
git clone https://github.com/TU_USUARIO/sale_auto_update_prices.git
```

2. Reiniciar el servicio de Odoo:
```bash
sudo systemctl restart odoo
```

3. Actualizar la lista de aplicaciones en Odoo (Modo desarrollador > Apps > Actualizar lista de aplicaciones)

4. Buscar "Sale Auto Update Prices" e instalarlo

## Uso

Una vez instalado, el módulo funciona automáticamente:

1. Abre o crea una orden de venta en estado borrador
2. Agrega productos
3. Cambia la cantidad de cualquier línea
4. **Los precios y descuentos se actualizan automáticamente** según la lista de precios configurada

## Funcionamiento técnico

### Flujo del módulo

1. El usuario cambia `product_uom_qty` en una línea de venta
2. Se dispara el `@api.onchange` en `sale.order.line`
3. Se llama a `action_update_prices()` con contexto especial `from_onchange_auto_update=True`
4. El método `message_post()` es interceptado para evitar errores en onchange
5. Se actualizan todos los precios y descuentos
6. No se publica mensaje en el chatter (evita error de registro no guardado)

### Problema que resuelve

Por defecto, Odoo no permite llamar a `message_post()` durante un `onchange` porque el registro aún no está guardado en la base de datos (es un `NewId`). Esto causa el error:

```
ValueError: La publicación de un mensaje debe hacerse en un documento comercial.
```

Este módulo intercepta `message_post()` cuando detecta que viene de un onchange, permitiendo que toda la lógica de actualización de precios funcione correctamente sin generar errores.

## Compatibilidad

- **Odoo 18.0 Enterprise Edition**
- Compatible con módulos de ADHOC como `sale_ux`
- Compatible con cualquier módulo que herede `action_update_prices`

## Dependencias

- `sale_management`

## Autor

**Trixocom**
- Website: https://www.trixocom.com

## Licencia

LGPL-3

## Soporte

Para reportar bugs o solicitar funcionalidades, por favor crear un issue en GitHub.

## Changelog

### Version 18.0.1.0.2
- Solución mejorada usando interceptación de `message_post()`
- Compatible con módulos que heredan `action_update_prices`
- Mantiene funcionalidad completa de actualización de descuentos

### Version 18.0.1.0.1
- Primera versión para Odoo 18 EE
