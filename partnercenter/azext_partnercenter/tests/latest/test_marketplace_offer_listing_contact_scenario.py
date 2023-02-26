# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferListingContactScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_listing_contact(self):
        command_root="partnercenter marketplace offer listing contact"
        parameters = """
    --offer-id {offer_id} \
    --type {contact_type} \
    --email {contact_email} \
    --name '{contact_name}' \
    --phone {contact_phone} \
    --uri {contact_uri}
"""

        create_checks = [
            self.check('[0].type', '{contact_type}'),
            self.check('[0].email', '{contact_email}'),
            self.check('[0].name', '{contact_name}'),
            self.check('[0].phone', '{contact_phone}'),
            self.check('[0].uri', '{contact_uri}')
        ]

        self._validate_create_delete(command_root, parameters, create_checks)
 
    def init_args(self):
        self.kwargs.update({
            'contact_type': 'Engineering',
            'contact_email': 'test@contoso.com',
            'contact_name': self.create_random_name('Jane Doe', 12),
            'contact_phone': '1230987654',
            'contact_uri': 'https://test.contact.uri',
        })
