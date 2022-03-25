import requests

from odoo import http
from odoo.http import request
from datetime import datetime
from num2words import num2words
import urllib.parse as urlparse
from urllib.parse import parse_qs
from odoo import models, fields, api
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    basic_synch_partner = fields.Char(string="Basic Synch Partner")


class ExecutiveAreaWise(models.Model):
    _inherit = 'executive.area.wise'

    basic_synch_area = fields.Char(string="Sync Area")


class ProductTemplate(models.Model):
    _inherit = "product.template"
    basic_synch_product = fields.Char(string='Sync Product')


class PinInformation(models.Model):
    _inherit = "pin.information"
    basic_synch_pin = fields.Char(string='Sync Pin')


class TransportationDeatails(models.Model):
    _inherit = "transportation.details"
    basic_synch_transporter = fields.Char(string='Sync Transporter')


class EwayConfiguration(models.Model):
    _inherit = "eway.configuration"
    basic_synch_eway = fields.Char(string='Sync Eway')


class EInvoiceConfiguration(models.Model):
    _inherit = "einvoice.configuration"
    basic_synch_einvoice = fields.Char(string='Sync Einvoice')


class ResUsers(models.Model):
    _inherit = "res.users"
    basic_synch_users = fields.Char(string='Sync Users')


class CompanyBranches(models.Model):
    _inherit = "company.branches"
    basic_synch_branch = fields.Char(string='Sync Branch')


class ResCompany(models.Model):
    _inherit = "res.company"
    basic_synch_company = fields.Char(string='Sync Company')


# class ResSubPartners(models.Model):
#     _inherit = "res.sub.partner"
#
#     basic_synch_sub_partner = fields.Char(string='Sync Company')


class SaleEstimate(models.Model):
    _inherit = 'sale.estimate'

    basic_synch_estimate = fields.Char(string='Sync estimate')
    basic_synch_estimate_approve = fields.Boolean(default=False)
    basic_synch_estimate_send_owner = fields.Boolean(default=False)
    basic_synch_estimate_cancel = fields.Boolean(default=False)
    basic_synch_estimate_approved = fields.Boolean(default=False)
    basic_synch_estimate_rejected = fields.Boolean(default=False)

    @api.constrains('basic_synch_estimate_approve')
    def basic_synch_estimate_approve_but(self):
        if self.basic_synch_estimate_approve:
            self.action_approve()
    @api.constrains('basic_synch_estimate_send_owner')
    def basic_basic_synch_estimate_send_owner(self):
        if self.basic_synch_estimate_send_owner:
            self.action_send_owner()
    @api.constrains('basic_synch_estimate_cancel')
    def basic_basic_synch_estimate_cancel(self):
        if self.basic_synch_estimate_cancel:
            self.action_cancel()
    @api.constrains('basic_synch_estimate_rejected')
    def basic_basic_synch_estimate_rejected(self):
        if self.basic_synch_estimate_rejected:
            self.action_send_rejected()

    @api.constrains('basic_synch_estimate_approved')
    def basic_basic_synch_estimate_approved(self):
        if self.basic_synch_estimate_approved:
            self.action_send_approved()



class EstimateDippo(models.Model):
    _inherit = 'estimate.dippo'

    basic_synch_dippo = fields.Char(string='Sync Dippo')



class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    basic_synch_vehicle = fields.Char(string='Sync vehicle')
    basic_synch_vehicle_mark = fields.Boolean(default=False)

    @api.constrains('basic_synch_vehicle_mark')
    def basic_basic_synch_vehicle_mark(self):
        if self.basic_synch_vehicle_mark:
            self.mark_vehicle()



class SalesExecutiveCollections(models.Model):
    _inherit = "executive.collection"

    basic_synch_collection = fields.Char(string='Sync Collection')
    basic_synch_cash_colled = fields.Boolean(string='Sync Collection')
    basic_synch_cash_confirm = fields.Boolean(string='Sync Collection')
    basic_synch_cash_reversed = fields.Boolean(string='Sync Collection')

    @api.constrains('basic_synch_cash_colled')
    def basic_action_exe_confirm(self):
        if self.basic_synch_cash_colled:
            self.action_exe_confirm()
    @api.constrains('basic_synch_cash_confirm')
    def basic_basic_synch_cash_confirm(self):
        if self.basic_synch_cash_confirm:
            self.action_confirm()

    @api.constrains('basic_synch_cash_reversed')
    def basic_basic_synch_cash_reversed(self):
        if self.basic_synch_cash_reversed:
            self.action_reverse()

class SalesExecutiveCheque(models.Model):
    _inherit = "executive.cheque.collection"


    basic_synch_check_collection = fields.Char(string='Sync Collection')
    basic_synch_check_colled = fields.Boolean(string='Sync Collection')

    @api.constrains('basic_synch_check_colled')
    def basic_basic_synch_check_collection(self):
        if self.basic_synch_check_colled:
            self.action_deposit()

class TodayCheques(models.Model):
    _inherit = "today.cheques"

    basic_synch_today_cheques = fields.Char(string='Sync Collection')
    basic_synch_tocheques_button = fields.Boolean(string='Sync Collection')

    @api.constrains('basic_synch_tocheques_button')
    def basic_basic_synch_tocheques_button(self):
        if self.basic_synch_tocheques_button:
            if self.state =='draft':
               self.action_confirm()




class AmountWithdraw(models.Model):
    _inherit = "amount.withdraw"

    basic_synch_withdraw = fields.Char(string='Sync withdraw')
    basic_synch_withdraw_button = fields.Boolean(string='Sync Collection')
    basic_synch_withdreverse_button = fields.Boolean(string='Sync Collection')

    @api.constrains('basic_synch_withdraw_button')
    def basic_basic_synch_withdraw_button(self):
        if self.basic_synch_withdraw_button:
            self.action_confirm()

    @api.constrains('basic_synch_withdreverse_button')
    def basic_synch_withdreverse_button(self):
        if self.basic_synch_withdreverse_button:
            if self.state == 'done':
               self.action_reverse()

class CashToBank(models.Model):
    _inherit = 'cash.to.bank'

    basic_synch_to_bank = fields.Char(string='Sync to Bank')
    basic_synch_to_bank_button = fields.Boolean(string='Sync to bank')
    basic_synch_to_reverbutton = fields.Boolean(string='Sync Collection')

    @api.constrains('basic_synch_to_reverbutton')
    def basic_synch_basic_synch_to_reverbutton(self):
        if self.basic_synch_to_reverbutton:
            if self.state == 'done':
               self.action_reverse()
    @api.constrains('basic_synch_to_bank_button')
    def basic_basic_synch_to_bank_button(self):
        if self.basic_synch_to_bank_button:
            self.action_confirm()

class InternalAmountTransfer(models.Model):
    _inherit = 'internal.amount.transfer'

    basic_synch_bank_transf = fields.Char(string='Sync to Bank')
    basic_synch_bank_transf_button = fields.Boolean(string='Sync to bank')
    basic_synch_to_reverbutton = fields.Boolean(string='Sync Collection')


    @api.constrains('basic_synch_bank_transf_button')
    def basic_basic_synch_bank_transf_button(self):
        if self.basic_synch_bank_transf_button:
            self.action_post()

    @api.constrains('basic_synch_to_reverbutton')
    def basic_basic_synch_to_reverbutton(self):
        if self.basic_synch_to_reverbutton:
            if self.state == 'done':
                self.action_reverse()



class FundTransferBTCompanies(models.Model):
    _inherit = "fund.transfer.companies"

    basic_synch_fund_transf = fields.Char(string='Sync to Bank')
    basic_synch_fund_transf_button = fields.Boolean(string='Sync to bank')
    basic_synch_fund_t_ref_button = fields.Boolean(string='Sync to bank')

    @api.constrains('basic_synch_fund_transf_button')
    def basic_basic_synch_fund_transf_button(self):
        if self.basic_synch_fund_transf_button:
            self.action_post()

    @api.constrains('basic_synch_fund_t_ref_button')
    def basic_basic_synch_fund_t_ref_button(self):
        if self.basic_synch_fund_t_ref_button:
            if self.send == 'done':
                self.action_reverse()


class CashBookClosing(models.Model):
    _inherit = "cash.book.closing"

    basic_synch_closing = fields.Char(string='Sync to closing')
    basic_synch_closing_button = fields.Boolean(string='Sync to closing')

    @api.constrains('basic_synch_closing_button')
    def basic_basic_synch_closing_button(self):
        if self.basic_synch_closing_button:
            self.action_cash_book_close()

    @api.constrains('basic_synch_closing')
    def basic_basic_synch_closing(self):
            if self.basic_synch_closing:
                self.onchange_date()




class FreightDiscount(models.Model):
    _inherit = 'freight.disc'

    basic_synch_freight = fields.Char(string='Sync to freight')
    basic_synch_freight_button = fields.Boolean(string='Sync to freight')
    basic_synch_fund_t_ref_button = fields.Boolean(string='Sync to bank')


    @api.constrains('basic_synch_freight_button')
    def basic_basic_synch_freight_button(self):
        if self.basic_synch_freight_button:
            self.action_post()


    @api.constrains('basic_synch_fund_t_ref_button')
    def basic_basic_synch_fund_t_ref_button(self):
        if self.basic_synch_fund_t_ref_button:
            if self.state == 'done':
                self.action_reverse()

class PartyAdvanceLedger(models.Model):
    _inherit = "party.advance.ledger"

    basic_synch_advance= fields.Char(string='Sync to advance')
    basic_synch_advance_button = fields.Boolean(string='Sync to advance')

    @api.constrains('basic_synch_advance_button')
    def basic_basic_synch_advance_button(self):
        if self.basic_synch_advance_button:
            self.action_confirm()



class CashierDirectCollection(models.Model):
    _inherit = "cashier.direct.collection"

    basic_synch_direct = fields.Char(string='Sync to direct')
    basic_synch_direct_button = fields.Boolean(string='Sync to direct')
    basic_synch_direct_rev_button = fields.Boolean(string='Sync to direct')



    @api.constrains('basic_synch_direct_rev_button')
    def basic_basic_synch_direct_rev_button(self):
        if self.basic_synch_direct_rev_button:
            if self.state == 'validate':
                self.action_reverse()


    @api.constrains('basic_synch_direct_button')
    def basic_basic_synch_direct_button(self):
        if self.basic_synch_direct_button:
            self.action_confirm()


class RtgsNeftCollections(models.Model):
    _inherit = "neft.rtgs.collection"

    basic_synch_neft = fields.Char(string='Sync to direct')
    basic_synch_neft_button = fields.Boolean(string='Sync to direct')
    basic_synch_direct_rev_button = fields.Boolean(string='Sync to direct')

    @api.constrains('basic_synch_direct_rev_button')
    def basic_basic_synch_direct_rev_button(self):
        if self.basic_synch_direct_rev_button:
            if self.state == 'validate':
                self.action_reverse()

    @api.constrains('basic_synch_neft_button')
    def basic_basic_synch_neft_button(self):
        if self.basic_synch_neft_button:
            self.action_confirm()


class ExpensesDiscount(models.Model):
    _inherit = 'expenses.disc'

    basic_synch_expen = fields.Char(string='Sync to expenses')
    basic_synch_expen_button = fields.Boolean(string='Sync to expenses')
    basic_synch_direct_rev_button = fields.Boolean(string='Sync to direct')

    @api.constrains('basic_synch_direct_rev_button')
    def basic_basic_synch_direct_rev_button(self):
        if self.basic_synch_direct_rev_button:
            if self.state == 'done':
                self.action_reverse()

    @api.constrains('basic_synch_expen_button')
    def basic_basic_synch_expen_button(self):
        if self.basic_synch_expen_button:
            self.action_post()



class PartyAdvanceLedger(models.Model):
    _inherit = "party.advance.ledger"

    basic_synch_party_advance = fields.Char(string='Sync to Advance')
    basic_synch_party_advance_button = fields.Boolean(string='Sync to Advance')

    @api.constrains('basic_synch_party_advance_button')
    def basic_basic_synch_expen_button(self):
        if self.basic_synch_party_advance_button:
            self.action_confirm()



class AccountAccount(models.Model):
    _inherit = "account.account"

    basic_synch_account = fields.Char(string='Sync to Advance')
    basic_synch_account_button = fields.Boolean(string='Sync to Advance')




class EstimateOrders(models.Model):
    _inherit = 'estimate.orders'

    basic_synch_order = fields.Char(string='Sync to Order')
    basic_synch_order_button = fields.Boolean(string='Sync to Order')


    @api.constrains('basic_synch_order_button')
    def basic_basic_synch_order_button(self):
        if self.basic_synch_order_button:
            self.action_oder_confirm()



class CompanySoPOTransfer(models.Model):
    _inherit = 'company.sopo.transfer'

    basic_synch_sopo = fields.Char(string='Sync to sopo')
    basic_synch_sopo_button = fields.Boolean(string='Sync to sopo')

    @api.constrains('basic_synch_sopo_button')
    def basic_basic_synch_sopo_button(self):
        if self.basic_synch_sopo_button:
            self.send_other_location()


class Location(models.Model):
    _inherit = "stock.location"

    basic_synch_location = fields.Char(string='Sync to location')
    # basic_synch_sopo_button = fields.Boolean(string='Sync to sopo')



class InterBranchTransfer(models.Model):
    _inherit = 'inter.branch.transfer'

    basic_synch_transfer = fields.Char(string='Sync to transfer')
    basic_synch_transfer_button = fields.Boolean(string='Sync to transfer')

    @api.constrains('basic_synch_transfer_button')
    def basic_basic_synch_transfer_button(self):
        if self.basic_synch_transfer_button:
            self.send_other_location()

class OpeningBalanceCustomers(models.Model):
    _inherit = "opening.balance.customers"



    basic_synch_opening = fields.Char(string='Sync to Opening')
    basic_synch_opening_button = fields.Boolean(string='Sync to Opening')

    @api.constrains('basic_synch_opening_button')
    def basic_basic_synch_opening_button(self):
        if self.basic_synch_opening_button:
            self.action_opening_bal_all()



class OpenAccountBalance(models.Model):
    _inherit = 'open.account.balance'


    basic_synch_ac_balance = fields.Char(string='Sync to Balance')
    basic_synch_ac_balance_button = fields.Boolean(string='Sync to Balance')

    @api.constrains('basic_synch_ac_balance_button')
    def basic_basic_synch_ac_balance_button(self):
        if self.basic_synch_ac_balance_button:
            self.op_create()


class SalesReturn(models.Model):
    _inherit = 'sales.return'

    basic_synch_return = fields.Char(string='Sync to return')
    basic_synch_return_button = fields.Boolean(string='Sync to return')

    @api.constrains('basic_synch_return_button')
    def basic_basic_synch_return_button(self):
        if self.basic_synch_return_button:
            self.credit_note_validation()

class SalesInvoiceCancel(models.Model):
    _inherit = 'sales.invoice.cancel'

    basic_synch_cancel = fields.Char(string='Sync to return')
    basic_synch_cancel_button = fields.Boolean(string='Sync to return')

    @api.constrains('basic_synch_cancel_button')
    def basic_basic_synch_cancel_button(self):
        if self.basic_synch_cancel_button:
            self.action_cancel_create()

class CreditLimitRecord(models.Model):
    _inherit = "credit.limit.record"

    basic_synch_credit_limit = fields.Char(string='Sync to return')
    basic_synch_credit_limit_button = fields.Boolean(string='Sync to return')

    # @api.constrains('basic_synch_credit_limit_button')
    # def basic_basic_synch_credit_limit_button(self):
    #     if self.basic_synch_credit_limit_button:
    #         self.action_cancel_create()



class SalesIncentives(models.Model):
    _inherit = "sales.person.incentives"

    basic_synch_incentives = fields.Char(string='Sync to return')
    basic_synch_incentives_button = fields.Boolean(string='Sync to return')

    @api.constrains('basic_synch_incentives_button')
    def basic_basic_synch_incentives_button(self):
        if self.basic_synch_incentives_button:
            self.action_incentives()


class AccountJournal(models.Model):
    _inherit = "account.journal"

    basic_synch_journal = fields.Char(string='Sync to journal')
    basic_synch_journal_button = fields.Boolean(string='Sync to journal')






class SetupBarBankConfigWizard(models.TransientModel):
    _inherit = 'account.setup.bank.manual.config'

    basic_synch_bank = fields.Char(string='Sync to bank')
    basic_synch_bank_button = fields.Boolean(string='Sync to bank')

    @api.constrains('basic_synch_bank_button')
    def basic_basic_synch_bank_button(self):
        if self.basic_synch_bank_button:
            self.validate()




class ResBank(models.Model):
    _inherit = "res.bank"

    basic_synch_res_bank = fields.Char(string='Sync to bank')
    basic_synch_res_bank_button = fields.Boolean(string='Sync to bank')

    @api.constrains('basic_synch_res_bank')
    def basic_basic_synch_bank_button(self):
        if self.basic_synch_res_bank:
            self.validate()



class PdcConfiguration(models.Model):
    _inherit = "pdc.configuration"

    basic_synch_pdc_bank = fields.Char(string='Sync to pdc')
    basic_synch_pdc_button = fields.Boolean(string='Sync to pdc')

class FreightDiscountConfig(models.Model):
    _inherit = 'freight.disc.config'



class BounceCheques(models.Model):
    _inherit = "bounce.cheques"

    basic_synch_bounce = fields.Char(string='Sync to bounce')
    basic_synch_bounce_button = fields.Boolean(string='Sync to bounce')



class AreaOffers(models.Model):
    _inherit = "area.offers"


    basic_synch_offers = fields.Char(string='Sync to offers')
    basic_synch_offers_button = fields.Boolean(string='Sync to offers')


class PurchaseOrderCustom(models.Model):
    _inherit = 'purchase.order.custom'


    basic_synch_purchase_req = fields.Char(string='Sync to Purchase Request')
    basic_synch_purchase_req_button = fields.Boolean(string='Sync to Purchase Request')

    @api.constrains('basic_synch_purchase_req_button')
    def basic_basic_synch_purchase_req_button(self):
        if self.basic_synch_purchase_req_button:
            self.action_oder_confirm()



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    basic_synch_purchase_order = fields.Char(string='Sync to Purchase Order')
    basic_synch_purchase_order_button = fields.Boolean(string='Sync to Purchase Order')

    @api.constrains('basic_synch_purchase_order_button')
    def basic_basic_synch_purchase_order_button(self):
        if self.basic_synch_purchase_order_button:
            self.action_confirm_ezp()



class AccountInvoice(models.Model):
    _inherit = "account.move"

    basic_synch_account_move = fields.Char(string='Sync to Purchase Order')
    basic_synch_account_move_button = fields.Boolean(string='Sync to Purchase Order')

    @api.constrains('basic_synch_account_move_button')
    def basic_basic_synch_account_move_button(self):
        if self.basic_synch_account_move_button:
            self.action_post()
