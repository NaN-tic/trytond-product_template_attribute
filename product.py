# This file is part product_template_attribute module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval
from trytond.transaction import Transaction
from trytond import backend

__all__ = ['Template', 'Product']


class Template(metaclass=PoolMeta):
    __name__ = 'product.template'
    template_attributes = fields.Dict('product.attribute', 'Attributes',
        domain=[
            ('sets', '=',
                Eval('attribute_set', -1)),
            ], depends=['attribute_set'])

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().connection.cursor()
        table = cls.__table_handler__(module_name)
        sql_table = cls.__table__()

        super(Template, cls).__register__(module_name)

        # Migration 5.2: delete template_attribute_set field
        if table.column_exist('template_attribute_set'):
            cursor.execute(*sql_table.update(
                columns=[sql_table.attribute_set],
                values=[sql_table.template_attribute_set]))

            table.drop_column('template_attribute_set')


class Product(metaclass=PoolMeta):
    __name__ = 'product.product'

    @classmethod
    def __setup__(cls):
        super(Product, cls).__setup__()
        cls.attributes.states['invisible'] = True
