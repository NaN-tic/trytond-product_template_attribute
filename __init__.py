#This file is part product_template_attribute module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .product import *

def register():
    Pool.register(
        Template,
        module='product_template_attribute', type_='model')
