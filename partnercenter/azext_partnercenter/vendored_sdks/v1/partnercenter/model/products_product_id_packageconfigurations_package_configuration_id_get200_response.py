"""
    https://api.partner.microsoft.com/v1.0/ingestion

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ..model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from ..exceptions import ApiAttributeError


def lazy_import():
    from ..model.microsoft_ingestion_api_models_common_type_value_pair import MicrosoftIngestionApiModelsCommonTypeValuePair
    from ..model.microsoft_ingestion_api_models_packages_azure_application_package_configuration import MicrosoftIngestionApiModelsPackagesAzureApplicationPackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_azure_managed_application_package_configuration import MicrosoftIngestionApiModelsPackagesAzureManagedApplicationPackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_azure_policy import MicrosoftIngestionApiModelsPackagesAzurePolicy
    from ..model.microsoft_ingestion_api_models_packages_azure_resource_manager_test_drive_package_configuration import MicrosoftIngestionApiModelsPackagesAzureResourceManagerTestDrivePackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_azure_solution_template_package_configuration import MicrosoftIngestionApiModelsPackagesAzureSolutionTemplatePackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_dynamics365_business_central_package_configuration import MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralPackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_dynamics365_business_central_test_drive_package_configuration import MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralTestDrivePackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_dynamics365_customer_engagement_package_configuration import MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementPackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_dynamics365_customer_engagement_test_drive_package_configuration import MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementTestDrivePackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_dynamics365_operations_package_configuration import MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_dynamics365_operations_test_drive_package_configuration import MicrosoftIngestionApiModelsPackagesDynamics365OperationsTestDrivePackageConfiguration
    from ..model.microsoft_ingestion_api_models_packages_package_region_availability import MicrosoftIngestionApiModelsPackagesPackageRegionAvailability
    from ..model.microsoft_ingestion_api_models_packages_role_authorization import MicrosoftIngestionApiModelsPackagesRoleAuthorization
    globals()['MicrosoftIngestionApiModelsCommonTypeValuePair'] = MicrosoftIngestionApiModelsCommonTypeValuePair
    globals()['MicrosoftIngestionApiModelsPackagesAzureApplicationPackageConfiguration'] = MicrosoftIngestionApiModelsPackagesAzureApplicationPackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesAzureManagedApplicationPackageConfiguration'] = MicrosoftIngestionApiModelsPackagesAzureManagedApplicationPackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesAzurePolicy'] = MicrosoftIngestionApiModelsPackagesAzurePolicy
    globals()['MicrosoftIngestionApiModelsPackagesAzureResourceManagerTestDrivePackageConfiguration'] = MicrosoftIngestionApiModelsPackagesAzureResourceManagerTestDrivePackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesAzureSolutionTemplatePackageConfiguration'] = MicrosoftIngestionApiModelsPackagesAzureSolutionTemplatePackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralPackageConfiguration'] = MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralPackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralTestDrivePackageConfiguration'] = MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralTestDrivePackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementPackageConfiguration'] = MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementPackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementTestDrivePackageConfiguration'] = MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementTestDrivePackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration'] = MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesDynamics365OperationsTestDrivePackageConfiguration'] = MicrosoftIngestionApiModelsPackagesDynamics365OperationsTestDrivePackageConfiguration
    globals()['MicrosoftIngestionApiModelsPackagesPackageRegionAvailability'] = MicrosoftIngestionApiModelsPackagesPackageRegionAvailability
    globals()['MicrosoftIngestionApiModelsPackagesRoleAuthorization'] = MicrosoftIngestionApiModelsPackagesRoleAuthorization


class ProductsProductIDPackageconfigurationsPackageConfigurationIDGet200Response(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('resource_type',): {
            'AZURERESOURCEMANAGERTESTDRIVEPACKAGECONFIGURATION': "AzureResourceManagerTestDrivePackageConfiguration",
        },
        ('package_type',): {
            'ADDON': "AddOn",
            'CONNECT': "Connect",
        },
        ('base_license_model',): {
            'RESOURCE': "Resource",
            'USER': "User",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'resource_type': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'odata_etag': (str,),  # noqa: E501
            'package_type': (str,),  # noqa: E501
            'application_installation_uri': (str,),  # noqa: E501
            'package_references': ([MicrosoftIngestionApiModelsCommonTypeValuePair],),  # noqa: E501
            'base_license_model': (str,),  # noqa: E501
            'require_s2_s_outbound_and_crm_secure_store_access': (bool, none_type,),  # noqa: E501
            'application_configuration_uri': (str,),  # noqa: E501
            'package_location_uri': (str,),  # noqa: E501
            'package_region_availabilities': ([MicrosoftIngestionApiModelsPackagesPackageRegionAvailability],),  # noqa: E501
            'multiple_packages_in_package_file': (bool, none_type,),  # noqa: E501
            'release_version': (str,),  # noqa: E501
            'solution_identifier': (str,),  # noqa: E501
            'azure_active_directory_application_id': (str,),  # noqa: E501
            'azure_active_directory_application_key': (str,),  # noqa: E501
            'azure_active_directory_tenant_id': (str,),  # noqa: E501
            'test_drive_duration': (int, none_type,),  # noqa: E501
            'azure_active_directory_tenant_name': (str,),  # noqa: E501
            'max_concurrent_test_drives': (int, none_type,),  # noqa: E501
            'instance_uri': (str,),  # noqa: E501
            'role_name': (str,),  # noqa: E501
            'instance_web_api_uri': (str,),  # noqa: E501
            'trial_legal_entity': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'allow_jit_access': (bool, none_type,),  # noqa: E501
            'can_enable_customer_actions': (bool, none_type,),  # noqa: E501
            'allowed_customer_actions': ([str],),  # noqa: E501
            'public_azure_tenant_id': (str,),  # noqa: E501
            'public_azure_authorizations': ([MicrosoftIngestionApiModelsPackagesRoleAuthorization],),  # noqa: E501
            'azure_government_tenant_id': (str,),  # noqa: E501
            'azure_government_authorizations': ([MicrosoftIngestionApiModelsPackagesRoleAuthorization],),  # noqa: E501
            'policies': ([MicrosoftIngestionApiModelsPackagesAzurePolicy],),  # noqa: E501
            'regions': ([str],),  # noqa: E501
            'hot_instances': (int, none_type,),  # noqa: E501
            'warm_instances': (int, none_type,),  # noqa: E501
            'cold_instances': (int, none_type,),  # noqa: E501
            'azure_subscription_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'resource_type': 'resourceType',  # noqa: E501
        'id': 'ID',  # noqa: E501
        'odata_etag': '@odata.etag',  # noqa: E501
        'package_type': 'packageType',  # noqa: E501
        'application_installation_uri': 'applicationInstallationUri',  # noqa: E501
        'package_references': 'packageReferences',  # noqa: E501
        'base_license_model': 'baseLicenseModel',  # noqa: E501
        'require_s2_s_outbound_and_crm_secure_store_access': 'requireS2SOutboundAndCrmSecureStoreAccess',  # noqa: E501
        'application_configuration_uri': 'applicationConfigurationUri',  # noqa: E501
        'package_location_uri': 'packageLocationUri',  # noqa: E501
        'package_region_availabilities': 'packageRegionAvailabilities',  # noqa: E501
        'multiple_packages_in_package_file': 'multiplePackagesInPackageFile',  # noqa: E501
        'release_version': 'releaseVersion',  # noqa: E501
        'solution_identifier': 'solutionIdentifier',  # noqa: E501
        'azure_active_directory_application_id': 'azureActiveDirectoryApplicationID',  # noqa: E501
        'azure_active_directory_application_key': 'azureActiveDirectoryApplicationKey',  # noqa: E501
        'azure_active_directory_tenant_id': 'azureActiveDirectoryTenantID',  # noqa: E501
        'test_drive_duration': 'testDriveDuration',  # noqa: E501
        'azure_active_directory_tenant_name': 'azureActiveDirectoryTenantName',  # noqa: E501
        'max_concurrent_test_drives': 'maxConcurrentTestDrives',  # noqa: E501
        'instance_uri': 'instanceUri',  # noqa: E501
        'role_name': 'roleName',  # noqa: E501
        'instance_web_api_uri': 'instanceWebApiUri',  # noqa: E501
        'trial_legal_entity': 'trialLegalEntity',  # noqa: E501
        'version': 'version',  # noqa: E501
        'allow_jit_access': 'allowJitAccess',  # noqa: E501
        'can_enable_customer_actions': 'canEnableCustomerActions',  # noqa: E501
        'allowed_customer_actions': 'allowedCustomerActions',  # noqa: E501
        'public_azure_tenant_id': 'publicAzureTenantID',  # noqa: E501
        'public_azure_authorizations': 'publicAzureAuthorizations',  # noqa: E501
        'azure_government_tenant_id': 'azureGovernmentTenantID',  # noqa: E501
        'azure_government_authorizations': 'azureGovernmentAuthorizations',  # noqa: E501
        'policies': 'policies',  # noqa: E501
        'regions': 'regions',  # noqa: E501
        'hot_instances': 'hotInstances',  # noqa: E501
        'warm_instances': 'warmInstances',  # noqa: E501
        'cold_instances': 'coldInstances',  # noqa: E501
        'azure_subscription_id': 'azureSubscriptionID',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):    # noqa: E501
        """ProductsProductIDPackageconfigurationsPackageConfigurationIDGet200Response - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            resource_type (str): [optional] if omitted the server will use the default value of "AzureResourceManagerTestDrivePackageConfiguration"  # noqa: E501
            id (str): [optional]  # noqa: E501
            odata_etag (str): [optional]  # noqa: E501
            package_type (str): [optional]  # noqa: E501
            application_installation_uri (str): [optional]  # noqa: E501
            package_references ([MicrosoftIngestionApiModelsCommonTypeValuePair]): [optional]  # noqa: E501
            base_license_model (str): [optional]  # noqa: E501
            require_s2_s_outbound_and_crm_secure_store_access (bool, none_type): [optional]  # noqa: E501
            application_configuration_uri (str): [optional]  # noqa: E501
            package_location_uri (str): [optional]  # noqa: E501
            package_region_availabilities ([MicrosoftIngestionApiModelsPackagesPackageRegionAvailability]): [optional]  # noqa: E501
            multiple_packages_in_package_file (bool, none_type): [optional]  # noqa: E501
            release_version (str): [optional]  # noqa: E501
            solution_identifier (str): [optional]  # noqa: E501
            azure_active_directory_application_id (str): [optional]  # noqa: E501
            azure_active_directory_application_key (str): [optional]  # noqa: E501
            azure_active_directory_tenant_id (str): [optional]  # noqa: E501
            test_drive_duration (int, none_type): [optional]  # noqa: E501
            azure_active_directory_tenant_name (str): [optional]  # noqa: E501
            max_concurrent_test_drives (int, none_type): [optional]  # noqa: E501
            instance_uri (str): [optional]  # noqa: E501
            role_name (str): [optional]  # noqa: E501
            instance_web_api_uri (str): [optional]  # noqa: E501
            trial_legal_entity (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            allow_jit_access (bool, none_type): [optional]  # noqa: E501
            can_enable_customer_actions (bool, none_type): [optional]  # noqa: E501
            allowed_customer_actions ([str]): [optional]  # noqa: E501
            public_azure_tenant_id (str): [optional]  # noqa: E501
            public_azure_authorizations ([MicrosoftIngestionApiModelsPackagesRoleAuthorization]): [optional]  # noqa: E501
            azure_government_tenant_id (str): [optional]  # noqa: E501
            azure_government_authorizations ([MicrosoftIngestionApiModelsPackagesRoleAuthorization]): [optional]  # noqa: E501
            policies ([MicrosoftIngestionApiModelsPackagesAzurePolicy]): [optional]  # noqa: E501
            regions ([str]): [optional]  # noqa: E501
            hot_instances (int, none_type): [optional]  # noqa: E501
            warm_instances (int, none_type): [optional]  # noqa: E501
            cold_instances (int, none_type): [optional]  # noqa: E501
            azure_subscription_id (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs |= arg
                else:
                    raise ApiTypeError(
                        f"Invalid positional arguments={args} passed to {self.__class__.__name__}. Remove those invalid positional arguments.",
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                            self._configuration is not None and \
                            self._configuration.discard_unknown_keys and \
                            self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):    # noqa: E501
        """ProductsProductIDPackageconfigurationsPackageConfigurationIDGet200Response - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            resource_type (str): [optional] if omitted the server will use the default value of "AzureResourceManagerTestDrivePackageConfiguration"  # noqa: E501
            id (str): [optional]  # noqa: E501
            odata_etag (str): [optional]  # noqa: E501
            package_type (str): [optional]  # noqa: E501
            application_installation_uri (str): [optional]  # noqa: E501
            package_references ([MicrosoftIngestionApiModelsCommonTypeValuePair]): [optional]  # noqa: E501
            base_license_model (str): [optional]  # noqa: E501
            require_s2_s_outbound_and_crm_secure_store_access (bool, none_type): [optional]  # noqa: E501
            application_configuration_uri (str): [optional]  # noqa: E501
            package_location_uri (str): [optional]  # noqa: E501
            package_region_availabilities ([MicrosoftIngestionApiModelsPackagesPackageRegionAvailability]): [optional]  # noqa: E501
            multiple_packages_in_package_file (bool, none_type): [optional]  # noqa: E501
            release_version (str): [optional]  # noqa: E501
            solution_identifier (str): [optional]  # noqa: E501
            azure_active_directory_application_id (str): [optional]  # noqa: E501
            azure_active_directory_application_key (str): [optional]  # noqa: E501
            azure_active_directory_tenant_id (str): [optional]  # noqa: E501
            test_drive_duration (int, none_type): [optional]  # noqa: E501
            azure_active_directory_tenant_name (str): [optional]  # noqa: E501
            max_concurrent_test_drives (int, none_type): [optional]  # noqa: E501
            instance_uri (str): [optional]  # noqa: E501
            role_name (str): [optional]  # noqa: E501
            instance_web_api_uri (str): [optional]  # noqa: E501
            trial_legal_entity (str): [optional]  # noqa: E501
            version (str): [optional]  # noqa: E501
            allow_jit_access (bool, none_type): [optional]  # noqa: E501
            can_enable_customer_actions (bool, none_type): [optional]  # noqa: E501
            allowed_customer_actions ([str]): [optional]  # noqa: E501
            public_azure_tenant_id (str): [optional]  # noqa: E501
            public_azure_authorizations ([MicrosoftIngestionApiModelsPackagesRoleAuthorization]): [optional]  # noqa: E501
            azure_government_tenant_id (str): [optional]  # noqa: E501
            azure_government_authorizations ([MicrosoftIngestionApiModelsPackagesRoleAuthorization]): [optional]  # noqa: E501
            policies ([MicrosoftIngestionApiModelsPackagesAzurePolicy]): [optional]  # noqa: E501
            regions ([str]): [optional]  # noqa: E501
            hot_instances (int, none_type): [optional]  # noqa: E501
            warm_instances (int, none_type): [optional]  # noqa: E501
            cold_instances (int, none_type): [optional]  # noqa: E501
            azure_subscription_id (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs |= arg
                else:
                    raise ApiTypeError(
                        f"Invalid positional arguments={args} passed to {self.__class__.__name__}. Remove those invalid positional arguments.",
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                            self._configuration is not None and \
                            self._configuration.discard_unknown_keys and \
                            self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
          ],
          'oneOf': [
              MicrosoftIngestionApiModelsPackagesAzureApplicationPackageConfiguration,
              MicrosoftIngestionApiModelsPackagesAzureManagedApplicationPackageConfiguration,
              MicrosoftIngestionApiModelsPackagesAzureResourceManagerTestDrivePackageConfiguration,
              MicrosoftIngestionApiModelsPackagesAzureSolutionTemplatePackageConfiguration,
              MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralPackageConfiguration,
              MicrosoftIngestionApiModelsPackagesDynamics365BusinessCentralTestDrivePackageConfiguration,
              MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementPackageConfiguration,
              MicrosoftIngestionApiModelsPackagesDynamics365CustomerEngagementTestDrivePackageConfiguration,
              MicrosoftIngestionApiModelsPackagesDynamics365OperationsPackageConfiguration,
              MicrosoftIngestionApiModelsPackagesDynamics365OperationsTestDrivePackageConfiguration,
          ],
        }
