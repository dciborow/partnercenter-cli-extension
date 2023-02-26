# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
from dataclasses import dataclass
import os
import time
from azure.cli.testsdk import ScenarioTest


class PartnerCenterScenarioTest(ScenarioTest):
    def __init__(self, method_name, config_file=None, recording_name=None, recording_processors=None, replay_processors=None, recording_patches=None, replay_patches=None):
        super().__init__(method_name, config_file, recording_name, recording_processors, replay_processors, recording_patches, replay_patches)
        self.cmd_delay = 0
        self.test_data = TestData()

    def setUp(self):
        self.init_args()
        super().setUp()

    def cmd(self, command, checks=None, expect_failure=False, delay=0):
        """cmd that supports adding a delay into the execution of a command."""
        if delay > 0 or self.cmd_delay > 0:
            if delay > 0:
                time.sleep(delay)
            else:
                time.sleep(self.cmd_delay)
        return super().cmd(command, checks=checks, expect_failure=expect_failure)

    @abstractmethod
    def init_args(self):
        """initialize all the args needed for the test. Called on setUp by the test scaffolding."""

    def _validate_create_delete(self, command_root, parameters, create_checks=[], list_checks=[]):
        commands = {
            "create": command_root + " add " + parameters,
            "delete": command_root + " delete --yes " + parameters,
            "list": command_root + " list --offer-id {offer_id}" 
        }

        self.cmd(commands['create'], checks=create_checks)
        self.cmd(commands['delete'])
        result = self.cmd(commands['list'], checks=list_checks).get_output_in_json()
        self.assertEqual(len(result), 0)

@dataclass
class MarketplaceTest(ScenarioTest):

    @abstractmethod
    def _command_root(self) -> str:
        """Command root for Partner Center CLI Commands"""

    @abstractmethod
    def _command_parameters(self) -> str:
        """Command parameters for Partner Center CLI Commands"""

    def _create_command(self):
        """Command to create a Marketplace Offer"""
        return self._command_root() + ' create --id {offer_id} ' + self._command_parameters()

    def _show_command(self):
        """Command to show a Marketplace Offer"""
        return self._command_root() + ' show --id {offer_id}'
    
    def _list_command(self):
        """Command to list Marketplace Offers"""
        return self._command_root() + ' list'
    
    def _delete_command(self):
        """Command to delete a Marketplace Offer"""
        return self._command_root() + ' delete --id {offer_id} --yes'

    def _marketplace_offer_test(self):
        self._create_offer()
        self._show_offer()
        self._list_offers_with_created_offer_in_result()
        self._delete_offer()

    def _create_checks(self):
        """Checks to perform after creating a Marketplace Offer"""
        return []
    
    def _show_checks(self):
        """Checks to perform after showing a Marketplace Offer"""
        return []
    
    def _list_checks(self):
        """Checks to perform after listing Marketplace Offers"""
        return []

    def _create_offer(self):
        """Create Marketplace Offer"""
        self.cmd(self._create_command, checks=self._create_checks())

    def _show_offer(self):
        """Show Marketplace Offer"""
        self.cmd(self._show_command, checks=self._show_checks())

    def _list_offers_with_created_offer_in_result(self):
        self.cmd(self._list_command, checks=self._list_checks())

    def _delete_offer(self):
        """Delete Marketplace Offer"""
        self.cmd(self._delete_command)
        list = self.cmd(self._command_root() + ' list --query \'[?id==`{offer_id}`]\'').get_output_in_json()
        assert len(list) == 0

class TestData:
    """Test Data from the file system"""

    TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))
    """The root test directory path"""

    def __init__(self, test_data_dir='data'):
        self.test_data_dir = os.path.join(self.TEST_DIR, test_data_dir).replace('\\', '\\\\')
        self._ensure_dir(self.test_data_dir)

        self.data = {}

    def list(self):
        """Returns the list of data files that have been added"""
        return self.data.items()

    def clear(self):
        """Clears all test data"""
        self.data.clear()

    def add(self, file_path):
        """Adds the test data file to the set of test data and returns the absolute path for the test data file"""
        abs_file_path = os.path.join(self.test_data_dir, file_path).replace('\\', '\\\\')
        self.data[file_path] = abs_file_path

        return abs_file_path

    def _ensure_dir(self, dirpath):
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
