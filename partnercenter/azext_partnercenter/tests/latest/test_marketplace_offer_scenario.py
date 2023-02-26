# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from dataclasses import dataclass
from ..base import MarketplaceTest

@dataclass
class PartnerCenterMarketplaceOfferScenarioTest(MarketplaceTest):

    def test_marketplace_offer(self):
        self._marketplace_offer_test()

    def _command_root(self):
        return 'partnercenter marketplace offer'

    def _create_checks(self):
        return [
            self.check('id', '{offer_id}'),
            self.check('alias', '{offer_alias}')
        ]
    
    def _show_checks(self):
        return self._create_checks() + [
            self.check('type', 'AzureContainer')
        ]

    def _list_checks(self):
        return [
            self.check("[?id=='{offer_id}'].id | [0]", '{offer_id}'),
        ]

    def setUp(self):
        self._initialize_variables()
        super().setUp()

    def _initialize_variables(self):
        self.offer_id = self.create_random_name('offertest-', 15)

        # api variables
        self.kwargs.update({
            'offer_id': self.offer_id,
            'offer_alias': f'{self.offer_id}-alias',
        })
