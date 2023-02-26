# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferListingScenarioTest(PartnerCenterScenarioTest):

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_listing(self):
        command_root = "partnercenter marketplace offer listing"
        command_show = command_root + ' show --offer-id {offer_id}'
        command_update = command_root + ' update --offer-id {offer_id} --summary {summary} --short-description {short_description} --description {description}'
        
        initial_checks = [
            self.check('description', ''),
            self.check('shortDescription', ''),
            self.check('summary', ''),
        ]
        update_checks = [
            self.check('description', '{description}'),
            self.check('shortDescription', '{short_description}'),
            self.check('summary', '{summary}'),
        ]
        show_checks = [
            self.check('description', '{description}'),
            self.check('shortDescription', '{short_description}'),
            self.check('summary', '{summary}'),
            self.check('contacts', []), self.check('uris', []),
        ]

        self.cmd(command_show, checks=initial_checks)
        self.cmd(command_update, checks=update_checks)     
        self.cmd(command_show, checks=show_checks, delay=5)

    def init_args(self):
        self.kwargs.update({
            'summary': self.create_random_name('summary-', 20),
            'short_description': self.create_random_name('short-desc-', 20),
            'description': self.create_random_name('desc-', 20),
        })
