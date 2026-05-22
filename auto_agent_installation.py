import paramiko
import create_nr_infra_cmd as cnic
import generate_api_key as gak

def run_ssh_command():
    api_key = gak.get_user_key()
    install_command = cnic.create_infra_cmd(api_key)
    hostname = "HOST_NAME"
    username = "USERNAME"
    pkey_path = "PEM_FILE_PATH.pem"
    command = install_command
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        private_key = paramiko.RSAKey.from_private_key_file(pkey_path)
        
        print(f"Connecting to {hostname}...")
        client.connect(hostname=hostname, username=username, pkey=private_key)
        print("Connected successfully!")
        
        stdin, stdout, stderr = client.exec_command(command)
        
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        
        if output:
            print("\n--- Command Output ---")
            print(output.strip())
            
        if error:
            print("\n--- Command Error ---")
            print(error.strip())
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        client.close()
        print("\nConnection closed.")

if __name__ == "__main__":
    run_ssh_command()