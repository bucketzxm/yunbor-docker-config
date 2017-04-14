import paramiko
import datetime
import os
import ConfigParser
import codecs
hostname = ""
port = 22
username = ""
password = ""
REMOTE_PATH = ""
LOCAL_PATH = ""


def loadConfig():
    global hostname
    global port
    global username
    global password
    global REMOTE_PATH
    global LOCAL_PATH
    f = codecs.open("config.ini", "r", encoding='UTF-8')
    config = ConfigParser.ConfigParser()
    config.readfp(f)
    hostname = config.get("global", "hostname")
    port = int(config.get("global", "port"))
    username = config.get("global", "username")
    password = config.get("global", "password")
    REMOTE_PATH = config.get("global", "REMOTE_PATH")
    LOCAL_PATH = config.get("global", "LOCAL_PATH")


def upload(localFile, remoteDir):
    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        try:
            filename = os.path.basename(localFile)
            if not remoteDir.endswith('/'):
                remoteDir += '/'
            sftp.put(localFile, str(remoteDir) + str(filename))
        except Exception as e:
            t.close()
            raise e
        print("upload success!")
        t.close()
    except Exception as e:
        print(e)
        raise e


if __name__ == "__main__":
    loadConfig()
    upload(LOCAL_PATH, REMOTE_PATH)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, 22, username, password)
    stdin, stdout, stderr = ssh.exec_command("du -ah " + REMOTE_PATH)
    print("stdout: " + str(stdout.readlines()))
    print("stderr: " + str(stderr.readlines()))
    ssh.close()
