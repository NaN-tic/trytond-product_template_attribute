# This file is part product_template_attribute module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Template']


class Template(metaclass=PoolMeta):
    __name__ = 'product.template'
    template_attributes = fields.Dict('product.attribute', 'Attributes',
        domain=[
            ('sets', '=',
                Eval('attribute_set', -1)),
            ], depends=['attribute_set'])
