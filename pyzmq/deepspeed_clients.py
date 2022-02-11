import subprocess

for i in range(2):
    subprocess.Popen(["python3", "client.py", str(i)])
