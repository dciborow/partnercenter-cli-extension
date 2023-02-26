# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferListingMediaScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_listing_media_large_logo(self):
        command_root="partnercenter marketplace offer listing media"
        parameters="""
    --offer-id {offer_id} \
    --type {large_logo_media_type} \
    --file {large_logo_file}
"""

        create_checks = [
            self.check('state', '{add_cmd_state}'),
            self.check('type', '{large_logo_media_type}'),
        ]
     
        self._validate_create_delete(command_root, parameters, create_checks)

    def init_args(self):
        large_logo_abs_path = self.test_data.add("marketplace_offer_listing_media/largelogo.png")

        self.kwargs.update({
            'add_cmd_state': 'Uploaded',
            'large_logo_media_type': 'AzureLogoLarge',
            'large_logo_file': large_logo_abs_path
        })
