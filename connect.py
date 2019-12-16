import paramiko, cryptography
def connect_host():
    clinet = paramiko.SSHClient()
    clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    clinet.connect(hostname='116.62.65.165',
                   port=22,
                   username='root',
                   password='1234.com')
    stdin, stdout, stderr = clinet.exec_command('cd /root;ls')
    result = stdout
    print(result)
    clinet.close()
connect_host()