 BASH
 Bash stands for Bourne Again SHell—a modern replacement for the original Unix shell (sh).
 It’s a command-line interpreter used in Linux and Unix systems.
 It’s the default shell in most Linux distributions.
 It is basically like a robot assistant that helps you perform certain task by typing some commands.

 BASH SCRIPTING
Bash scripting is writing a series of Bash commands in a file (usually ending in .sh) to automate tasks.
Instead of typing commands one by one, you write them once and run the script whenever needed.
It’s like teaching your computer a routine—once, and it remembers forever.

CREATING MY FIRST BASH SCRIPT
Some of the important points to keep in mind before creating your first bash script:-
i.To create a file You have to use a syntax called nano <file name you want>.sh.Nano is basically a text editor and it’s one of the easiest tools for editing files directly from the terminal.

ii.sh stands for shell.It's a command-line shell and scripting language.
It basically allows you to run commands, write scripts, and automate tasks and still widely used today for shell scripts (.sh files).

iii.A shell file (or shell script) is a text file that contains a sequence of Linux/Unix commands.
File extension: usually .sh
It is written in a shell scripting language like bash, sh, or zsh and is used to automate tasks you’d normally type in the terminal.

iv.We create the file by first writing on top:- #!/bin/bash,which is basically a shell script.
It tells the system which interpreter to use to execute the script.
In this case:
#! = Shebang (special character combination)
/bin/bash = Full path to the Bash shell
Why is it Important?
Without this line:
The system might use another shell (like sh or dash) which may not support all Bash features.This can cause errors or unexpected behavior in your script.

v.Then to execute it we can use bash <file name you want>.sh or make it executable using chmod +x <file name you want>.sh.

vi.We first use ls -l command to check whether the file is executable or not.Then we gave permission by using chmod +x <file name you want>.sh.

vii.ls stands for “list”.It is used to list the contents of a directory (i.e., files and folders).
ls -l command is a long listing format of the ls command.It shows detailed information about files and directories in the current directory.

viii.chmod stands for “change mode”.It is used to change file or directory permissions in Linux and Unix systems.
Permissions control who can read, write, or execute a file.

ix.+x means to make it executable.

x.The echo command is used to display text or variables in the terminal.

![WhatsApp Image 2025-06-11 at 21 39 22_0e2b3953](https://github.com/user-attachments/assets/e509d193-2ee3-4234-82ba-4c2b4d030083)
In the above code i have created a file named himom.sh which basically tells hi mom.

The output:-
![WhatsApp Image 2025-06-11 at 21 40 05_41b42c8a](https://github.com/user-attachments/assets/8fe77c22-fd50-4569-91ac-4a9b9558e51a)
As you can see I was facing the error first because in the code above I have skipped giving space after the echo command.
I fixed then:-
![WhatsApp Image 2025-06-11 at 22 06 40_f9c7c4dd](https://github.com/user-attachments/assets/08ad50b3-6e67-4ead-be4f-c2347e643d4e)
It shows the desired output.



