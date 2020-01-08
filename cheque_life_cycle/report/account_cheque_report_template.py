# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _

class account_cheque_template(models.AbstractModel):
    _name = 'report.bi_account_cheque.account_cheque_template'


    @api.multi
    def _get_report_values(self, docids, data=None):
            record_ids = self.env[data['model']].browse(data['form'])
            val = {
                                 'doc_ids': docids,
                                 'doc_model': 'account.cheque',
                                 'docs': record_ids,
                                 'data' : data,
                                 }
            return val

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
