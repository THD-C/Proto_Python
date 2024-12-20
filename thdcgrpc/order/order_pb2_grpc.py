# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from order import order_pb2 as order_dot_order__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in order/order_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class OrderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrder = channel.unary_unary(
                '/order.Order/CreateOrder',
                request_serializer=order_dot_order__pb2.OrderDetails.SerializeToString,
                response_deserializer=order_dot_order__pb2.OrderDetails.FromString,
                _registered_method=True)
        self.DeleteOrder = channel.unary_unary(
                '/order.Order/DeleteOrder',
                request_serializer=order_dot_order__pb2.OrderID.SerializeToString,
                response_deserializer=order_dot_order__pb2.OrderDetails.FromString,
                _registered_method=True)
        self.GetOrder = channel.unary_unary(
                '/order.Order/GetOrder',
                request_serializer=order_dot_order__pb2.OrderID.SerializeToString,
                response_deserializer=order_dot_order__pb2.OrderDetails.FromString,
                _registered_method=True)
        self.GetOrderList = channel.unary_unary(
                '/order.Order/GetOrderList',
                request_serializer=order_dot_order__pb2.UserID.SerializeToString,
                response_deserializer=order_dot_order__pb2.OrderList.FromString,
                _registered_method=True)


class OrderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrderList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrder,
                    request_deserializer=order_dot_order__pb2.OrderDetails.FromString,
                    response_serializer=order_dot_order__pb2.OrderDetails.SerializeToString,
            ),
            'DeleteOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOrder,
                    request_deserializer=order_dot_order__pb2.OrderID.FromString,
                    response_serializer=order_dot_order__pb2.OrderDetails.SerializeToString,
            ),
            'GetOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrder,
                    request_deserializer=order_dot_order__pb2.OrderID.FromString,
                    response_serializer=order_dot_order__pb2.OrderDetails.SerializeToString,
            ),
            'GetOrderList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderList,
                    request_deserializer=order_dot_order__pb2.UserID.FromString,
                    response_serializer=order_dot_order__pb2.OrderList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'order.Order', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('order.Order', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Order(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/order.Order/CreateOrder',
            order_dot_order__pb2.OrderDetails.SerializeToString,
            order_dot_order__pb2.OrderDetails.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/order.Order/DeleteOrder',
            order_dot_order__pb2.OrderID.SerializeToString,
            order_dot_order__pb2.OrderDetails.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/order.Order/GetOrder',
            order_dot_order__pb2.OrderID.SerializeToString,
            order_dot_order__pb2.OrderDetails.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetOrderList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/order.Order/GetOrderList',
            order_dot_order__pb2.UserID.SerializeToString,
            order_dot_order__pb2.OrderList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
