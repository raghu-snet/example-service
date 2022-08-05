import sys
import grpc

# import the generated classes
import service.service_spec.example_service_pb2_grpc as grpc_ex_grpc
import service.service_spec.example_service_pb2 as grpc_ex_pb2

from service import registry

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "auto":
                test_flag = True

        # Example Service - Arithmetic
        endpoint = input("Endpoint (localhost:{}): ".format(registry["example_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["example_service"]["grpc"])


        grpc_method = input("Method (welcome|hello: ") if not test_flag else "hello"
        a = input("Greeting : ") if not test_flag else "Hello"
        b = input("Message : ") if not test_flag else "John"

        # Open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))
        #stub = grpc_ex_grpc.CalculatorStub(channel)
        #number = grpc_ex_pb2.Numbers(a=a, b=b)
        stub = grpc_ex_grpc.GreeterStub(channel)
        msg = grpc_ex_pb2.Message(greetingMsg=a,name=b)

        if grpc_method == "welcome":
            response = stub.welcome(msg)
            print(response.message)
        elif grpc_method == "hello":
            response = stub.hello(msg)
            print(response.message)
        else:
            print("Invalid method!")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)
