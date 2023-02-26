# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import MarketplaceTest


class PartnerCenterMarketplaceOfferListingContactScenarioTest(MarketplaceTest):

    def test_marketplace_offer_listing_contact(self):
        self._marketplace_offer_test()

    def _command_root(self):
        return "partnercenter marketplace offer listing contact"
    
    def _command_parameters(self) -> str:
        return """
    --offer-id {offer_id} \
    --type {contact_type} \
    --email {contact_email} \
    --name '{contact_name}' \
    --phone {contact_phone} \
    --uri {contact_uri}
"""
 
    def _create_checks(self):
        return [
            self.check('[0].type', '{contact_type}'),
            self.check('[0].email', '{contact_email}'),
            self.check('[0].name', '{contact_name}'),
            self.check('[0].phone', '{contact_phone}'),
            self.check('[0].uri', '{contact_uri}')
        ]

    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    def init_args(self):
        self.kwargs.update({
            'contact_type': 'Engineering',
            'contact_email': 'test@contoso.com',
            'contact_name': self.create_random_name('Jane Doe', 12),
            'contact_phone': '1230987654',
            'contact_uri': 'https://test.contact.uri',
        })
