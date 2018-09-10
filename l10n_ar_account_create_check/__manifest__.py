###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2013 Eynes/E-MIPS (http://www.e-mips.com.ar)
#    Copyright (c) 2014-2018 Aconcagua Team
#    All Rights Reserved. See readme/CONTRIBUTORS.rst for details.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name" : "Checkbook Management",
    "version" : "11.0.1.0.0",
    "author" : "eynes.com.ar,Odoo Community Association (OCA)",
    "website" : "www.eynes.com.ar",
    "category" : "Localisation/Argentine",
    "description": """Checkbook management for Own Checks""",
    "license": "AGPL-3",
    "depends": ["base", "l10n_ar_account_check"],
    "init_xml": [],
    "data": [
        "security/ir.model.access.csv",
        "wizard/annull_checks_view.xml",
        "views/checkbook_view.xml",
        "views/account_voucher_view.xml",
        "wizard/create_checkbook_view.xml",
    ],
    "demo": [
        # "demo/account_check_demo.xml",
    ],
    "active": False,
    "installable": True
}
