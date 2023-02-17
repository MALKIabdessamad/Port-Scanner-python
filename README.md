This is a Python script that checks if a given port is open on a range of IP addresses. The script prompts the user to enter the port number and IP address range to check, and creates a file to store the results of the port check.

The check_port function takes an IP address, a port number, and a list results as parameters. It creates a socket and tries to connect to the specified IP address and port. If the connection is successful, the function adds a tuple (ip, port, True) to the results list. If the connection is unsuccessful, it adds a tuple (ip, port, False).

The main program prompts the user to enter the port number and IP address range to check. It splits the IP address range into a prefix and a size, and converts the size to an integer. It creates an output file to store the results of the port check.

The program creates a list of threads, and for each IP address in the range, it creates a new thread that calls the check_port function. The thread is started and added to the list of threads.

After all the threads have been created and started, the program waits for all the threads to finish by calling the join method on each thread.

Finally, the program opens the output file in write mode and iterates over the results list. For each result, if the port is open, it writes the IP address and port number to the file and prints a message to the console saying that the port is open. If the port is closed, it prints a message to the console saying that the port is closed
