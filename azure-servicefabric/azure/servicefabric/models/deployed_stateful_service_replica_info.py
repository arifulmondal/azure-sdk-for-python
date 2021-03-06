# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .deployed_service_replica_info import DeployedServiceReplicaInfo


class DeployedStatefulServiceReplicaInfo(DeployedServiceReplicaInfo):
    """Information about a stateful service replica deployed on a node.

    :param service_name:
    :type service_name: str
    :param service_type_name:
    :type service_type_name: str
    :param service_manifest_name:
    :type service_manifest_name: str
    :param code_package_name:
    :type code_package_name: str
    :param partition_id:
    :type partition_id: str
    :param replica_status: Possible values include: 'Invalid', 'InBuild',
     'Standby', 'Ready', 'Down', 'Dropped'
    :type replica_status: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param address: The last address returned by the replica in Open or
     ChangeRole.
    :type address: str
    :param service_package_activation_id:
    :type service_package_activation_id: str
    :param host_process_id: Host process id of the process that is hosting the
     replica. This will be zero if the replica is down. In hyper-v containers
     this host process id will be from different kernel.
    :type host_process_id: str
    :param service_kind: Polymorphic Discriminator
    :type service_kind: str
    :param replica_id:
    :type replica_id: str
    :param replica_role: Possible values include: 'Unknown', 'None',
     'Primary', 'IdleSecondary', 'ActiveSecondary'
    :type replica_role: str or :class:`enum <azure.servicefabric.models.enum>`
    :param reconfiguration_information:
    :type reconfiguration_information: :class:`ReconfigurationInformation
     <azure.servicefabric.models.ReconfigurationInformation>`
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'service_type_name': {'key': 'ServiceTypeName', 'type': 'str'},
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'code_package_name': {'key': 'CodePackageName', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'replica_status': {'key': 'ReplicaStatus', 'type': 'str'},
        'address': {'key': 'Address', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
        'host_process_id': {'key': 'HostProcessId', 'type': 'str'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'replica_id': {'key': 'ReplicaId', 'type': 'str'},
        'replica_role': {'key': 'ReplicaRole', 'type': 'str'},
        'reconfiguration_information': {'key': 'ReconfigurationInformation', 'type': 'ReconfigurationInformation'},
    }

    def __init__(self, service_name=None, service_type_name=None, service_manifest_name=None, code_package_name=None, partition_id=None, replica_status=None, address=None, service_package_activation_id=None, host_process_id=None, replica_id=None, replica_role=None, reconfiguration_information=None):
        super(DeployedStatefulServiceReplicaInfo, self).__init__(service_name=service_name, service_type_name=service_type_name, service_manifest_name=service_manifest_name, code_package_name=code_package_name, partition_id=partition_id, replica_status=replica_status, address=address, service_package_activation_id=service_package_activation_id, host_process_id=host_process_id)
        self.replica_id = replica_id
        self.replica_role = replica_role
        self.reconfiguration_information = reconfiguration_information
        self.service_kind = 'Stateful'
