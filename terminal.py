import subprocess

def launch_butterfly(ip_address):
    subprocess.call("butterfly.server.py --host=" + ip_address + " --port=57575 --unsecure", shell=True)
