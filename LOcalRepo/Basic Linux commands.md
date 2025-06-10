LINUX COMMANDS

Linux is an open-source operating system that's known for its flexibility, security, and stability. Unlike Windows or macOS, which are proprietary, Linux is freely available and can be modified by anyone. It’s widely used for servers, software development, and even personal computing, with various distributions like Ubuntu, Fedora, and Arch Linux.

WHY IS IT IMPORTANT TO STILL USE TEXT COMMANDS IN THIS ADVANCED WORLD?

i. We have more control over the machines, we can run commands to change permissions, view hidden files, interact with databases, start servers, manage processes, etc. ii. It is faster for example we can make 10,000 files in a single line. iii. We can also automate things. iv. Easily available everywhere. v. Requirement in the market.

 The operating system is divided into two parts where one is Microsoft and the second is everything related to Unix.
 What is Unix?
 Unix is a powerful, multitasking, multiuser operating system originally developed in the late 1960s at  Bell Labs. It's known for its simplicity, portability, and robustness, forming the foundation for many modern operating systems, including Linux and macOS. It is referred as the "father" of many operating system.

Commands i. whoami:- It is basically a command which prints the username of the current user. 

ii. man command:-It basically gives you the information for all the  commands 
SYNTAX-man

 Press q/Q for exit.
 Press h/H for help.

 iii. clear command:-It is a command used for clearing all the previous commands. It clears the terminal screen. We can also use ctrl+l.

 iv.pwd command:-It stands for print working directory. If we are lost in the filesystem we can use pwd command to know which folder path we are currently using and thus it will print the current folder path,







 v.ls command:-This command is used to list all the files that the current folder contains. If we add a folder name or path, it will print that folder contents as well. SYNTAX:-ls 

vi.cd command:-This command is used to change directory within the file system. It basically allows users to browse between folders. 

vii. mkdir command:-This command is used to create a new directory. It comes in use when we are organizing files

 viii. rmdir command:-This command is basically used to remove directories. It only works on folders that have no files or subdirectories inside them

. ix. touch command:-This command in linux is basically used to create empty files or update the timestamp of existing files.

 x.rm command:-This command is used to remove files and directories. It is used to delete unwanted data and the deleted files cannot be recovered easily. 

xi. cp command:- This command is used to copy files and directories. It comes handy for backing up data or moving files without deleting the original. 

xii.mv command:-It is used to move or rename files and directories. It is handy for reorganizing files.

 xiii. cat command:-This command in Linux is used to view, concatenate and create files. It's one of the most frequently used commands for handling text files. 

xiv. less/more command:-These commands in Linux are used to view the contents of a file one page at a time, making it more useful than cat commands for reading large files.

 xv. head command:-The head command in Linux is used to display the first few lines of a file. By default, it shows the first 10 lines, but we can customize as well.
 xvi. tail command:-The tail command is used to display the last few lines of a file, By default, it shows the last 10 lines but again we can customize.

 xvii. echo command:-It is used to display text or variables in the terminal. It is basically used to print information.
 
xviii. df command:-The df command is used to display disk space usage for file systems. It helps check available and used storage.

 xix. chmod command:-It is used to change file permissions allowing users to control who can read, write, or execute a file or directory.

 xx. chown command:- It is used to change the ownership of files and directories. It allows users with the necessary permissions to assign a new owner to a file. 

xxi. du command:-The du command in Linux is used to check disk usage for files and directories.

 xxii. top command:- It is used to monitor system performance and view real-time process activity. It is used for checking CPU and memory usage. 

xxiii. ps command:-The ps command in Linux is used to display information about currently running processes. It's great for checking which programs are currently running. 

xxiv. kill command:-The kill command in Linux is used to terminate processes by sending them specific signals. It's useful when a program becomes unresponsive or needs to be stopped. 

xxv. grep command:-It is used for searching text within files based on specific patterns. 

xxvi. find command:- The find is used to search for files and directories based on various criteria like name, type, size, and modification time(directory hierarchy).

 xxvii. locate command:-It is used to find files as fast as possible by searching a prebuilt database instead of scanning directories in real time. It is faster than the find command. 

xxviii. history command:- It is used to display previously executed commands in the terminal. It helps track past commands and can be useful for repeating tasks. 

xxix. alias command:-It is used to create shortcuts for frequently used commands, making terminal usage more efficient.

 xxx. uname command:-The uname command in Linux is used to display system information, including operating system.
 xxxi. sudo command:-The sudo command in Linux allows users to run commands with superuser privileges, typically as the root user. It's essential for performing administrative tasks. 

xxxii. apt command:-The apt command in Linux is used for managing software packages on Debian-based systems (like Ubuntu). It simplifies package installation, updating, and removal. 

xxxiii. yum command:-It is used for package management on Red Hat based systems(like CentOS, RHEL, and Fedora). It helps install, update, remove, and manage software packages. 

xxxiv. nano command:-The nano command in Linux opens Nano, a simple and user-friendly text editor for creating and modifying files directly from the terminal. 

xxxv. vi/vim command:-The vi and vim commands in Linux open Vi or Vim, powerful text editors for working with files directly from the terminal. Vim (Vi Improved) adds extra features and enhancements to the original Vi editor.

 xxxvi. tar command:-It is basically used to create, extract and manage archive files. It is basically used for compressing and backing up files.

 xxxvii. zip/unzip command:-The zip and unzip commands in Linux are used to compress and extract files in ".zip" format, making file transfer and storage more efficient. 

xxxviii. wget command:-This command is used to download files from the internet. It comes in handy for retrieving files from websites and automating downloads as well.

 xxxix. curl command:-The curl command in Linux is used to transfer data from or to a server using various protocols. 

xl. ssh command:-The ssh command in Linux is used to securely connect to remote systems over a network using the Secure Shell (SSH) protocol. It enables remote login and command execution. 

xli. scp command:- It is used to securely copy files between a local and remote system using SSH. It encrypts data transfer, ensuring safe file movement. xlii. rsync command:-The rsync command in Linux is used for efficient file synchronization and transfer, allowing copying of files and directories while minimizing data transfer.

 xliii. mount/umount command:-The mount and umount commands in Linux are used to attach and detach file systems, such as external drives or network shares. 

xliv. df command:-The df command in Linux stands for disk file system and is used to report disk space usage of our file systems. This shows the amount of used and available disk space on all mounted filesystems.
 xlv. du command:-It stands for disk usage and is used to estimate the amount of space used by files and directories. By default, it shows the size of the current directory and its subdirectories. 

xlvi. ifconfig command:-The ifconfig command in Linux is used to configure and display network interfaces. It's commonly used to check IP addresses, enable or disable interfaces, and troubleshoot network connections. 

xlvii. ping command:-The ping command in Linux is used to test network connectivity by sending ICMP Echo Request packets to a target host and measuring the response time.

 xlviii. netstat command:-The netstat command in Linux is used to monitor network connections, routing tables, and interface statistics. It's helpful for troubleshooting network issues and checking active connections

. xlix. uptime command:-The uptime command basically displays how long the system has been running.

 l. reboot/shutdown command:-The reboot command is used to restart or power off the system and also helps with maintenance and updates.

