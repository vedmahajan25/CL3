import xmlrpc.client

def main():
    server = xmlrpc.client.ServerProxy("http://localhost:8000/")
    try:
        n = int(input("Enter a number to calculate factorial: "))
        result = server.factorial(n)
        print("Factorial of", n, "is", result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
