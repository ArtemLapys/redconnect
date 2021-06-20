import paramiko 
import re

class Shell:

    def __init__(self, host, user, psw):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, username=user, password=psw, port=22)

        self.channel = self.ssh.invoke_shell()
        self.stdin = self.channel.makefile('wb')
        self.stdout = self.channel.makefile('r')

        self.last_login = str()
        self.last_failed_login = str()
        self.failed_login_attemps = str()

    def __del__(self):
        self.ssh.close()

    def close(self):
        """
        Закрывает соединение
        """
        self.ssh.close()

    def isclosed(self):
        """
        Проверяет, активен ли канал
        """
        return self.channel.closed

    def execute(self, cmd: str):
        """
        Обрабатывает команду в удалённом терминале.

        Возвращает кортеж состаящий из входной команды, результата выполнения, а также ошибки, в случае её возникновения.

        `cmd:` строка, обозначающая команду, которая должна быть выполнена
        """
        cmd = cmd.strip('\n')
        self.stdin.write(cmd + '\n')
        finish = 'end of stdOUT buffer. finished with exit status'
        echo_cmd = 'echo {} $?'.format(finish)
        self.stdin.write(echo_cmd + '\n')
        shin = self.stdin
        self.stdin.flush()

        shout = []
        sherr = []
        exit_status = 0
        for line in self.stdout:
            if str(line).startswith(cmd) or str(line).startswith(echo_cmd):
                # отсеивание мусора из stdin
                shout = []
            elif str(line).startswith(finish):
                # считывание статуса заверщения
                exit_status = int(str(line).rsplit(maxsplit=1)[1])
                if exit_status:
                    #если статус > 0, значит произошла ошибка. возвращаем её вместо выхода
                    sherr = shout
                    shout = []
                break

            elif str(line).startswith("Last login:"):
                self.last_login = str(line)
            elif str(line).startswith("Last failed login:"):
                self.last_failed_login = str(line)
            elif str(line).startswith("There was") and str(line).split(" ")[3:] == ("failed login attempt since the last successful login.\r\n").split(" "):
                self.last_failed_login = str(line)
            elif str(line).startswith("There were") and str(line).split(" ")[3:] == ("failed login attempts since the last successful login.\r\n").split(" "):
                self.last_failed_login = str(line)

            else:
                # удаление формата и добавление выходной строки в выходной список
                shout.append(re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]').sub('', line).
                             replace('\b', '').replace('\r', '').replace('\r', ''))

        # удаляем первую и последнюю строку из кортежа выхода и кортежа ошибки за ненадобностью
        if shout and echo_cmd in shout[-1]:
            shout.pop()
        if shout and cmd in shout[0]:
            shout.pop(0)
        if sherr and echo_cmd in sherr[-1]:
            sherr.pop()
        if sherr and cmd in sherr[0]:
            sherr.pop(0)

        return shin, shout, sherr