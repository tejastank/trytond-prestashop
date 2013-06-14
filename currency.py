# -*- coding: utf-8 -*-
"""
    currency

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: GPLv3, see LICENSE for more details.
"""
from trytond.model import ModelSQL, fields
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta


__all__ = [
    'CurrencyPrestashop', 'Currency'
]
__metaclass__ = PoolMeta


class CurrencyPrestashop(ModelSQL):
    """Prestashop currency cache

    This model keeps a store of tryton currency corresponding to the currency
    on prestashop as per prestashop site.
    This model is used to prevent extra API calls to be sent to prestashop
    to get the currency.
    Everytime a currency has to be looked up, it is first looked up in this
    model. If not found, a new record is created here.
    """
    __name__ = 'currency.currency.prestashop'

    currency = fields.Many2One('currency.currency', 'Currency', required=True)
    site = fields.Many2One('prestashop.site', 'Site', required=True)
    prestashop_id = fields.Integer('Prestashop ID', required=True)

    @staticmethod
    def default_site():
        "Return default site from context"
        return Transaction().context.get('prestashop_site')

    @classmethod
    def __setup__(cls):
        super(CurrencyPrestashop, cls).__setup__()
        cls._error_messages.update({
            'currency_not_found': 'Currency with code %s not found',
        })
        cls._sql_constraints += [
            ('prestashop_id_site_uniq',
                'UNIQUE(prestashop_id, site)',
                'Currency must be unique by prestashop id and site'
            )
        ]


class Currency:
    "Currency"
    __name__ = 'currency.currency'

    @classmethod
    def get_using_ps_id(cls, prestashop_id):
        """Return the currency corresponding to the prestashop_id for the
        current site in context
        If the currency is not found in the cache model, it is fetched from
        remote and a record is created in the cache for future references.

        :param prestashop_id: Prestashop ID for the currency
        :returns: Active record of the currency
        """
        pass

    def cache_prestashop_id(self, prestashop_id):
        """Cache the value of currency corresponding to the prestashop_id
        by creating a record in the cache model

        :param prestashop_id: Prestashop ID
        :returns: Active record of the currency cached
        """
        pass
