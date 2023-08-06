import http.client

def execute_command(command):
    conn = http.client.HTTPConnection(host_ip, host_port)
    request_path = '/execute?' + command  # Construct the correct path
    conn.request('GET', request_path)
    response = conn.getresponse()
    return response.read().decode()

def session_handler():
    while True:
        try:
            command = input('Enter command: ')
            if command == 'exit':
                execute_command('exit')
                print('[-] The server has terminated the session.')
                break
            elif command == 'answer':
                print(42)
            else:
                response = execute_command(command)
                print(response)
        except KeyboardInterrupt:
            print('[+] Keyboard interrupt issued.')
            break
        except Exception as e:
            print('Error:', str(e))
            break


def banner():
    rf = '''
    \033[1;32m    _____ \033[0m_________    _____________ \033[1;32m_____
    \033[1;32m    _____ \033[0m________/ /  ____________ \033[1;32m_____/
    \033[0m                 / /    
                    / /
                   / /
    \033[1;32m_______ \033[0m______/ /     ____________ \033[1;32m________
    \033[1;32m______ \033[0m________/     ____________ \033[1;32m_________/
    \033[0m        \  \        |  |  
             \  \       |  |
              \  \      |  | 
               \  \     |  | 
                \  \    |  | 
    '''
    print(rf)

host_ip = '192.168.56.3'
host_port = 2222
session_handler()
