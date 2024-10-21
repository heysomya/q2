import grpc
import login_pb2
import login_pb2_grpc

def run():
    # Ask the user for the username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Open a channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = login_pb2_grpc.LoginStub(channel)

        # Create a login request with the user inputs
        login_request = login_pb2.LoginRequest(userName=username, passWord=password)

        # Make the call to login method
        response = stub.login(login_request)
        print(f"Login Response: {response.responseMessage}, Code: {response.responseCode}")

        # If login was successful, call logout method
        if response.responseCode == 200:
            empty_request = login_pb2.Empty()
            response = stub.logout(empty_request)
            print(f"Logout Response: {response.responseMessage}, Code: {response.responseCode}")

if __name__ == '__main__':
    run()