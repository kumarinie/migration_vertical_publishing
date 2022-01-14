# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2016 Magnus - Willem Hulshof - www.magnus.nl
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company like Veritos.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
##############################################################################
#


{
    'name' : 'Reverse Billing Module - Accounting',
    'version' : '10.0.1.0',
    'category': 'purchasing/supplier invoices',
    'description': """
This is the module to manage reverse billing of supplier services/deliveries.
===================================================================================================================
This module creates a model, in which the written articles/ photoshoots for a specific issue
of a magazine are listed, related to the freelancer/photographer, who created te material, to the analytic_account
representing the Issue and to the products representing the type and price of the created material.

    """,
    'author'  : 'Magnus - Willem Hulshof',
    'website' : 'http://www.magnus.nl',
    'depends' : ['partner_firstname',
                 'sale_advertising_order',
    ],
    'data' : ["data/reverse_billing_data.xml",
              "data/product_category_revbil.xml",
              "security/security.xml",
              'security/ir.model.access.csv',
              'wizard/revbil_line_invoice.xml',
#              "wizard/portal_back_view.xml",
              'views/account_invoice_view.xml',
              "views/reverse_billing.xml",
              "views/company_view.xml",
              "views/product_view.xml",
            #   "views/account_invoice_report.xml",
              "views/account_analytic_view.xml",

    ],
    'demo' : [],
    'installable': True,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

