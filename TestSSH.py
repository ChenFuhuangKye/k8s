from sys import stderr, stdin, stdout
import paramiko

#service
ip = "10.0.1.1"
username = "karaf"
password = "karaf"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, port=32000, username=username, password=password, timeout=20)
stdout = client.exec_command('app activate org.onosproject.fwd')
stdout = client.exec_command('app activate org.onosproject.openflow')

client.close()
