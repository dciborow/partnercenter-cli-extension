"""
    https://api.partner.microsoft.com/v1.0/ingestion

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ..api_client import ApiClient, Endpoint as _Endpoint
from ..model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_variants_base_variant import (
    MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsVariantsBaseVariant,
)
from ..model.products_product_id_variants_get_request import ProductsProductIDVariantsGetRequest


class VariantClient(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.products_product_id_variants_get_endpoint = _Endpoint(
            settings={
                "response_type": (
                    MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsVariantsBaseVariant,
                ),
                "auth": [],
                "endpoint_path": "/products/{productID}/variants",
                "operation_id": "products_product_id_variants_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "product_id",
                    "authorization",
                    "skip_token",
                    "client_request_id",
                ],
                "required": [
                    "product_id",
                    "authorization",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "product_id": (str,),
                    "authorization": (str,),
                    "skip_token": (str,),
                    "client_request_id": (str,),
                },
                "attribute_map": {
                    "product_id": "productID",
                    "authorization": "Authorization",
                    "skip_token": "$skipToken",
                    "client_request_id": "Client-Request-ID",
                },
                "location_map": {
                    "product_id": "path",
                    "authorization": "header",
                    "skip_token": "query",
                    "client_request_id": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.products_product_id_variants_post_endpoint = _Endpoint(
            settings={
                "response_type": (ProductsProductIDVariantsGetRequest,),
                "auth": [],
                "endpoint_path": "/products/{productID}/variants",
                "operation_id": "products_product_id_variants_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "product_id",
                    "authorization",
                    "client_request_id",
                    "products_product_id_variants_get_request",
                ],
                "required": [
                    "product_id",
                    "authorization",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "product_id": (str,),
                    "authorization": (str,),
                    "client_request_id": (str,),
                    "products_product_id_variants_get_request": (ProductsProductIDVariantsGetRequest,),
                },
                "attribute_map": {
                    "product_id": "productID",
                    "authorization": "Authorization",
                    "client_request_id": "Client-Request-ID",
                },
                "location_map": {
                    "product_id": "path",
                    "authorization": "header",
                    "client_request_id": "header",
                    "products_product_id_variants_get_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )
        self.products_product_id_variants_variant_id_delete_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": [],
                "endpoint_path": "/products/{productID}/variants/{variantID}",
                "operation_id": "products_product_id_variants_variant_id_delete",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "product_id",
                    "variant_id",
                    "authorization",
                    "client_request_id",
                ],
                "required": [
                    "product_id",
                    "variant_id",
                    "authorization",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "product_id": (str,),
                    "variant_id": (str,),
                    "authorization": (str,),
                    "client_request_id": (str,),
                },
                "attribute_map": {
                    "product_id": "productID",
                    "variant_id": "variantID",
                    "authorization": "Authorization",
                    "client_request_id": "Client-Request-ID",
                },
                "location_map": {
                    "product_id": "path",
                    "variant_id": "path",
                    "authorization": "header",
                    "client_request_id": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.products_product_id_variants_variant_id_get_endpoint = _Endpoint(
            settings={
                "response_type": (ProductsProductIDVariantsGetRequest,),
                "auth": [],
                "endpoint_path": "/products/{productID}/variants/{variantID}",
                "operation_id": "products_product_id_variants_variant_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "product_id",
                    "variant_id",
                    "authorization",
                    "client_request_id",
                ],
                "required": [
                    "product_id",
                    "variant_id",
                    "authorization",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "product_id": (str,),
                    "variant_id": (str,),
                    "authorization": (str,),
                    "client_request_id": (str,),
                },
                "attribute_map": {
                    "product_id": "productID",
                    "variant_id": "variantID",
                    "authorization": "Authorization",
                    "client_request_id": "Client-Request-ID",
                },
                "location_map": {
                    "product_id": "path",
                    "variant_id": "path",
                    "authorization": "header",
                    "client_request_id": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.products_product_id_variants_variant_id_put_endpoint = _Endpoint(
            settings={
                "response_type": (ProductsProductIDVariantsGetRequest,),
                "auth": [],
                "endpoint_path": "/products/{productID}/variants/{variantID}",
                "operation_id": "products_product_id_variants_variant_id_put",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "product_id",
                    "variant_id",
                    "authorization",
                    "client_request_id",
                    "products_product_id_variants_get_request",
                ],
                "required": [
                    "product_id",
                    "variant_id",
                    "authorization",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "product_id": (str,),
                    "variant_id": (str,),
                    "authorization": (str,),
                    "client_request_id": (str,),
                    "products_product_id_variants_get_request": (ProductsProductIDVariantsGetRequest,),
                },
                "attribute_map": {
                    "product_id": "productID",
                    "variant_id": "variantID",
                    "authorization": "Authorization",
                    "client_request_id": "Client-Request-ID",
                },
                "location_map": {
                    "product_id": "path",
                    "variant_id": "path",
                    "authorization": "header",
                    "client_request_id": "header",
                    "products_product_id_variants_get_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def products_product_id_variants_get(self, product_id, authorization, **kwargs):
        """Returns a set of variants for the product.  # noqa: E501

        Returns a set of variants for the product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_variants_get(product_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            authorization (str): User authorization

        Keyword Args:
            skip_token (str): Skip token for paged collection. [optional]
            client_request_id (str): ID of request provIDed by user. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsVariantsBaseVariant
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout")
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths")
        kwargs["product_id"] = product_id
        kwargs["authorization"] = authorization
        return self.products_product_id_variants_get_endpoint.call_with_http_info(**kwargs)

    def products_product_id_variants_post(self, product_id, authorization, **kwargs):
        """Create a variant resource.  # noqa: E501

        Sample request:                   POST products/{productID}/variants                   {                       \"resourceType\": \"AzureSkuVariant\",                       ...                   }  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_variants_post(product_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            authorization (str): User authorization

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            products_product_id_variants_get_request (ProductsProductIDVariantsGetRequest): Request body of a Base Variant. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ProductsProductIDVariantsGetRequest
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout")
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths")
        kwargs["product_id"] = product_id
        kwargs["authorization"] = authorization
        return self.products_product_id_variants_post_endpoint.call_with_http_info(**kwargs)

    def products_product_id_variants_variant_id_delete(self, product_id, variant_id, authorization, **kwargs):
        """Delete the variant.  # noqa: E501

        Delete the variant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_variants_variant_id_delete(product_id, variant_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            variant_id (str): ID of variant
            authorization (str): User authorization

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout")
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths")
        kwargs["product_id"] = product_id
        kwargs["variant_id"] = variant_id
        kwargs["authorization"] = authorization
        return self.products_product_id_variants_variant_id_delete_endpoint.call_with_http_info(**kwargs)

    def products_product_id_variants_variant_id_get(self, product_id, variant_id, authorization, **kwargs):
        """Returns a variant for the product.  # noqa: E501

        Returns a variant for the product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_variants_variant_id_get(product_id, variant_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            variant_id (str): ID of variant
            authorization (str): User authorization

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ProductsProductIDVariantsGetRequest
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout")
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths")
        kwargs["product_id"] = product_id
        kwargs["variant_id"] = variant_id
        kwargs["authorization"] = authorization
        return self.products_product_id_variants_variant_id_get_endpoint.call_with_http_info(**kwargs)

    def products_product_id_variants_variant_id_put(self, product_id, variant_id, authorization, **kwargs):
        """Update the variant.  # noqa: E501

        Update the variant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_variants_variant_id_put(product_id, variant_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            variant_id (str): ID of variant
            authorization (str): User authorization

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            products_product_id_variants_get_request (ProductsProductIDVariantsGetRequest): Request body of a type of base variant. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ProductsProductIDVariantsGetRequest
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout")
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths")
        kwargs["product_id"] = product_id
        kwargs["variant_id"] = variant_id
        kwargs["authorization"] = authorization
        return self.products_product_id_variants_variant_id_put_endpoint.call_with_http_info(**kwargs)
