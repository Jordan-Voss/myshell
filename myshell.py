#Jordan Voss 17327513
from cmd import Cmd
import os,sys,fileinput
def run_command(command):
    prompt.onecmd(command)
class myPrompt(Cmd):
    #code to run and get help for the quit command
    def do_quit(self, key):
        print("Bye!")
        return True
    def help_quit(self):
        print("Exit the application.")
#code to run and get help for the echo command
    def do_echo(self, s):
        print(s)
    def help_echo(self):
        print("Return a given string")
#code to run and get help for the cd command
    def do_cd(self, d=""):
        if d != "":
            os.chdir(d)
        else:
            print(os.getcwd())
    def help_cd(self):
        print("Change the current directory or report the current directory")
#code to run and get help for the dir command
    def do_dir(self, arg):
        path = '.'
        files = os.listdir(path)
        for name in files:
            print (name)
    def help_dir(self):
        print("List the contents of a directory")
#code to run and get help for the clr command
    def do_clr(self,args):
        os.system('clear')
    def help_clr(self):
        print("clear the screen")
#code to run and get help for the environ command
    def do_environ(self ,args):
        for param in os.environ.keys():
            print (param,os.environ[param])
    def help_environ(self):
        print("List all the environment strings")
#code to run and get help for the pause command
    def do_pause(self,args):
        input('Press Enter to Continue')
    def help_pause(self):
        print("Pause operation of the shell until enter is pressed")
#end of myPrompt function.
def main():
    prompt = myPrompt()
    #if statement to  determine how many arguments in the command line to figure out what to do if it needs to input from or output to a file
    if len(sys.argv) == 2: #if command line has an additional argument read the commands in that file
        for line in fileinput.input():
            line=line.rstrip()
            prompt.onecmd(line)
    elif len(sys.argv) > 2: #if the commant line contains at least 1 arg and a file, execute the arg and write it to the file
        file = open(sys.argv[-1],'w+')
        for m in sys.argv[2:-1]: # this function is incomplete with redirecting output to files
            n = str(prompt.onecmd(m))
            file.write(n)
        file.close()
    elif len(sys.argv) < 2: #else continue the prompt as normal taking input from the command line.
        prompt.prompt = "${}:~ ".format(os.getcwd())
        prompt.cmdloop("Starting prompt. Type '?' or 'help' to list commands.")
if __name__ == '__main__':
    main()
