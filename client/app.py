import grpc
import login_pb2
import login_pb2_grpc
import socket

def check_network():
    try:
        server_ip = socket.gethostbyname('grpc-server')
        print(f"Resolved grpc-server to {server_ip}")
        
        sock = socket.create_connection(('grpc-server', 50051), timeout=5)
        print("Successfully connected to grpc-server:50051")
        sock.close()
    except Exception as e:
        print(f"Network check failed: {e}")

def run():
    logged_in = False

    check_network()

    with grpc.insecure_channel('grpc-server:50051') as channel:
        stub = login_pb2_grpc.LoginStub(channel)

        while True:
            print("Select an option:")
            print("1. Login")
            print("2. Logout")
            print("3. Exit")
            action = input("Enter 1, 2, or 3: ").strip()

            if action == '1':
                if not logged_in:
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")

                    try:
                        login_request = login_pb2.LoginRequest(userName=username, passWord=password)
                        response = stub.login(login_request)
                        print(f"Login Response: {response.responseMessage}, Code: {response.responseCode}")

                        if response.responseCode == 200:
                            logged_in = True
                            print("Login successful.")
                    except grpc.RpcError as e:
                        print(f"Login failed: {e.details()} (code: {e.code()})")
                else:
                    print("You are already logged in. Please logout first.")

            elif action == '2':
                if logged_in:
                    try:
                        empty_request = login_pb2.Empty()
                        response = stub.logout(empty_request)
                        print(f"Logout Response: {response.responseMessage}, Code: {response.responseCode}")

                        if response.responseCode == 200:
                            logged_in = False
                            print("Logout successful.")
                    except grpc.RpcError as e:
                        print(f"Logout failed: {e.details()} (code: {e.code()})")
                else:
                    print("You are not logged in. Please login first.")

            elif action == '3':
                print("Exiting...")
                break

            else:
                print("Invalid action. Please enter '1', '2', or '3'.")

if __name__ == '__main__':
    run()
