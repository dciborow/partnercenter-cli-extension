# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferListingUriScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_listing_uri(self):
        command_root="partnercenter marketplace offer listing uri"
        parameters="""
    --offer-id {offer_id} \
    --type {uri_type} \
    --subtype {uri_sub_type} \
    --display-text {uri_display_text} \
    --uri {uri}
"""
    
        create_checks = [
            self.check('[0].type', '{uri_type}'),
            self.check('[0].subtype', '{uri_sub_type}'),
            self.check('[0].displayText', '{uri_display_text}'),
            self.check('[0].uri', '{uri}'),
        ]
        list_checks = [self.check('uris', [])]

        self._validate_create_delete(command_root, parameters, create_checks, list_checks=list_checks)

    def init_args(self):
        self.kwargs.update({
            'uri': 'https://testuri',
            'uri_display_text': self.create_random_name('dt-', 10),
            'uri_type': 'PrivacyUri',
            'uri_sub_type': 'SubTypeUri'
        })
