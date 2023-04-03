import subprocess

if __name__ == '__main__':
    # Prompt the user to enter a new host name
    new_name = input('Enter a new host name: ')

    # Run the command to change the host name
    command = 'powershell Rename-Computer -NewName ' + new_name + ' -Force'
    subprocess.call(command, shell=True)

    # Print a message to indicate that the host name has been changed
    print('Host name has been changed to:', new_name)
