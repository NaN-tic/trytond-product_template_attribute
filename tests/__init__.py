# This file is part product_template_attribute module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.product_template_attribute.tests.test_product_template_attribute import suite
except ImportError:
    from .test_product_template_attribute import suite

__all__ = ['suite']
