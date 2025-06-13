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


![WhatsApp Image 2025-06-11 at 23 56 19_df87440e](https://github.com/user-attachments/assets/efb0a96a-3e29-4a30-a1f8-4ae576978e7d)



viii.chmod stands for “change mode”.It is used to change file or directory permissions in Linux and Unix systems.
Permissions control who can read, write, or execute a file.

ix.+x means to make it executable.

x.The echo command is used to display text or variables in the terminal.

xi.The $ symbol is used to access the value of the variable.


![WhatsApp Image 2025-06-11 at 21 39 22_0e2b3953](https://github.com/user-attachments/assets/e509d193-2ee3-4234-82ba-4c2b4d030083)
In the above code i have created a file named himom.sh which basically tells hi mom.

The output:-
![WhatsApp Image 2025-06-11 at 21 40 05_41b42c8a](https://github.com/user-attachments/assets/8fe77c22-fd50-4569-91ac-4a9b9558e51a)
As you can see I was facing the error first because in the code above I have skipped giving space after the echo command.
I fixed then:-
![WhatsApp Image 2025-06-11 at 22 06 40_f9c7c4dd](https://github.com/user-attachments/assets/08ad50b3-6e67-4ead-be4f-c2347e643d4e)
It shows the desired output.

Also made it executable:-
![WhatsApp Image 2025-06-11 at 22 07 26_0d3f9e63](https://github.com/user-attachments/assets/4abd7b3a-0277-4d6f-87b0-8c0f05a16c33)

Further I have use some of the commands.
The first two lines helps for user input.I have also further used some of the commands as well.
PWD-pwd stands for "Print Working Directory".It shows the full path of the current directory you are in, in the terminal.
USER-$USER is not a command—it's a shell variable.It holds the username of the currently logged-in user.
SHELL-$SHELL is an environment variable (not a command).It stores the path of the default shell assigned to the current user.
HOSTNAME-$HOSTNAME is an environment variable.It stores the name of the computer or system you're working on.
RANDOM-$RANDOM is a built-in Bash variable (not a command).Every time you use it, it gives a random number between 0 and 32767.
Great for scripts, games, random delays, or testing.


![WhatsApp Image 2025-06-12 at 00 11 24_eebafed1](https://github.com/user-attachments/assets/bbec5bee-c763-4445-98fb-0c7fb44260d2)

In this I have created a system which basically calculates when you will become a millionaire using the $RANDOM variable.This variable usually 
gives a random number between 0 to 32767 but here i have given $RANDOM % 15 which would give a random number between 0 to 14 and then we add it 
to our age.

![WhatsApp Image 2025-06-12 at 00 36 26_39606389](https://github.com/user-attachments/assets/0ecfd180-7522-4a1f-b30f-a61ced11aea8)

The output:-

![WhatsApp Image 2025-06-12 at 00 36 44_07772be8](https://github.com/user-attachments/assets/8d413aa6-28a6-4784-8a82-078a95f5becf)


In this code I have tried to build the elden ring game a little synopsis
![WhatsApp Image 2025-06-12 at 13 01 02_08040e30](https://github.com/user-attachments/assets/24f8aa04-716e-4402-8143-e38f5c237751)
![WhatsApp Image 2025-06-12 at 13 22 14_1782cfd1](https://github.com/user-attachments/assets/dc98b746-120d-49a0-b05e-26e62b2db579)

The output:-
![WhatsApp Image 2025-06-12 at 13 21 49_239fd850](https://github.com/user-attachments/assets/f08d07a1-4c0e-4b03-9b62-e1567bc56cfb)









