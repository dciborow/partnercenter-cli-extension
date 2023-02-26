# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferPlanScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_plan(self):
        command_root = "partnercenter marketplace offer plan"

        create_command = command_root + ' create --offer-id {offer_id} --id {plan_id} -n \'{plan_name}\''
        show_command = command_root + ' show --offer-id {offer_id} --id {plan_id}'
        delete_command = command_root + ' delete --offer-id {offer_id} --id {plan_id}'
        list_command = command_root + ' list --offer-id {offer_id} '
        
        parameter_checks = [
            self.check('id', '{plan_id}'),
            self.check('name', '{plan_name}'),
        ]

        self.cmd(create_command, checks=parameter_checks)
        self.cmd(show_command, checks=parameter_checks)
        self.cmd(delete_command)
        result = self.cmd(list_command).get_output_in_json()
        self.assertEqual(len(result), 0)

    def init_args(self):
        self.plan_id = self.create_random_name('plantest-', 15)
        self.kwargs.update({
            'plan_id': self.plan_id,
            'plan_name': f"{self.plan_id} Friendly Name"
        })
