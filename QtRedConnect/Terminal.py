from shell import Shell
import argparse

def connectToShell(ip: str, username: str, password:str):
    try:
        shell = Shell(ip, username, password)
    except:
        print("Ошибка подключения")
        return

    while True:

        command = input("[input]:")
        res = shell.execute(command)

        out = []
        if res[1] != []:
            out = res[1]
        else:
            out = res[2]

        for elem in out:
            print("[output]:"+ elem, end = "")

        if shell.isclosed():
            shell.close()
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=None, type=str)
    parser.add_argument("--user", default=None, type=str)
    parser.add_argument("--password", default=None, type=str)
    args = parser.parse_args()

    connectToShell(args.ip, args.user, args.password)
