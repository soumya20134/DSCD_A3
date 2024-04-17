# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mapper_pb2 as mapper__pb2


class MapperServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendPartitions = channel.unary_unary(
                '/MapperService/SendPartitions',
                request_serializer=mapper__pb2.IdRequest.SerializeToString,
                response_deserializer=mapper__pb2.pointsResponse.FromString,
                )
        self.ReceiveUpdatedCentroid = channel.unary_unary(
                '/MapperService/ReceiveUpdatedCentroid',
                request_serializer=mapper__pb2.centroidUpdateRequest.SerializeToString,
                response_deserializer=mapper__pb2.ack.FromString,
                )


class MapperServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendPartitions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveUpdatedCentroid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MapperServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendPartitions': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPartitions,
                    request_deserializer=mapper__pb2.IdRequest.FromString,
                    response_serializer=mapper__pb2.pointsResponse.SerializeToString,
            ),
            'ReceiveUpdatedCentroid': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveUpdatedCentroid,
                    request_deserializer=mapper__pb2.centroidUpdateRequest.FromString,
                    response_serializer=mapper__pb2.ack.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MapperService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MapperService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendPartitions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MapperService/SendPartitions',
            mapper__pb2.IdRequest.SerializeToString,
            mapper__pb2.pointsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveUpdatedCentroid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MapperService/ReceiveUpdatedCentroid',
            mapper__pb2.centroidUpdateRequest.SerializeToString,
            mapper__pb2.ack.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
