DISK PARTIONING
Formatting and Mounting storage volumes:-
When it comes to storage,the destop linux and server linux behave differently.

Formatting a Storage Volume
This is basically like preparing a blank notebook—you decide how it's organized before writing anything.
Formatting creates a filesystem (like ext4, xfs, ntfs, etc.) on a storage device so Linux can understand how to read and write data to it.
It uses mkfs (Make FileSystem), e.g.
EXAMPLE:-
sudo mkfs.ext4 /dev/sdb1
After formatting, your drive is ready—but Linux still doesn't "see" it yet. That’s where mounting comes in.

Mounting a Storage Volume
Imagine plugging in a USB drive we want to access it, mounting is what connects it to our file tree.
Mounting attaches the formatted device to a specific directory (called a mount point), like /mnt/usb or /media/drive.
EXAMPLE:-
sudo mount /dev/sdb1 /mnt/usb
Once mounted, we can browse or copy files just like any other folder.

Before attaching the USB
![WhatsApp Image 2025-06-14 at 13 21 03_6a58f771](https://github.com/user-attachments/assets/81bf8a2f-7b2b-43f3-9f1f-8526337a7e64)


After inserting the USB using the lsblk command which helps the user visualizing their storage devices and their structure.
It lists information about all block devices, like hard drives, SSDs, USBs, and their partitions.
Partitions are basically divisions each acting like an independent storage unit which allows the user organize data, 
allow multiple operating systems, or separate system files from personal files.
![WhatsApp Image 2025-06-14 at 13 06 04_6bde798e](https://github.com/user-attachments/assets/c827a669-cbae-4c4f-a00c-93d81d462b3d)


This command (ls -l /dev/sda) helps the user:-
i.ls (list) command with the -l option for long format to show detailed information about the block device /dev/sda.
ii.dev/sda is typically first hard disk. Since it lives in /dev, it’s not a regular file—it’s a block special file 
used by the kernel to interface with hardware.(kernel is the core component of an operating system.
It acts as a bridge between software and hardware, managing everything from memory and CPU scheduling to device communication and system calls.)
![WhatsApp Image 2025-06-14 at 13 11 25_75cb5e16](https://github.com/user-attachments/assets/34635efe-ae34-4d76-b8df-91c102a008ad)

The output means:-
b: This means it's a block device
rw-rw----: File permissions (owner can read/write, group can read/write)
1: Number of hard links (usually 1 for devices)
root: Owner
disk: Group
8, 0: Major and minor device numbers (identifiers for the kernel)
Jun 14 12:34: Last status change (not data modification)
/dev/sda: The name of the device


Another command that came into use here was sudo fdisk -l
It basically lists all available disks and their partition tables and it requires sudo because it reads from low-level disk devices.
It would show this kind of output:-
Disk /dev/sda: 100 GiB, 107374182400 bytes, ...
Device       Boot   Start      End  Sectors Size Type
/dev/sda1    *       2048   999423   997376 487M EFI System
/dev/sda2          999424 2097151  1097728  536M Linux filesystem

Disk size and device name (/dev/sda)
Partition numbers (like sda1)
Start and end sector 
Partition size and type 
Whether a partition is bootable(I dont understand this part?)


Mount command:-The mount command connects a storage device to the Linux file system so we can access its contents.
SYNTAX:-
sudo mount [OPTIONS] <device> <mount-point>
![WhatsApp Image 2025-06-14 at 13 22 37_47c9e09e](https://github.com/user-attachments/assets/40aa564b-4fcc-466a-8537-278aed97da89)
![WhatsApp Image 2025-06-14 at 13 22 57_1212c3f7](https://github.com/user-attachments/assets/a28d8d73-c00e-41c0-b27f-70ded2ee9322)
There are quite a few storage devices as seen.

The following command 
mount: Lists all currently mounted filesystems—including their devices, mount points, and mount options.
grep sda: Filters the output to only show entries related to devices whose names contain sda (like /dev/sda1)
![WhatsApp Image 2025-06-14 at 13 25 51_74f38021](https://github.com/user-attachments/assets/2e0a464b-b07f-41f1-93c7-d4f45f5b3540)

The output shows:-
/dev/sda1 (a partition from the first hard disk) is mounted.
It’s mounted at: /media/ananta/A251-1927
Filesystem type is vfat (common for USBs or SD cards).
Mount options include:
rw (read-write access)
nosuid, nodev, relatime (security/performance flags)
uid=1000, gid=1000 (gives user ID 1000 ownership—likely owner)
utf8, flush, and others related to file encoding and error handling


Umount command:-The umount command is all about cleanly detaching mounted file systems.
SYNTAX:-
sudo umount <mount-point> or
sudo umount <device>
![WhatsApp Image 2025-06-14 at 13 43 49_e2bfb4d1](https://github.com/user-attachments/assets/c9b0ba0b-9bd9-44cd-8e21-6f23c638ff50)

![WhatsApp Image 2025-06-14 at 13 44 37_bfef6ed2](https://github.com/user-attachments/assets/6affb7dd-5358-4922-a382-9cade7fdb48f)
mount command do not work anymore.


The following command (sudo fdisk /dev/sda) launches the interactive partition editor for the disk /dev/sda, using the fdisk utility. 
fdisk stands for "format disk". It's a text-based, menu-driven utility used to:
i. partition tables on a disk
ii.Create, delete, or resize partitions
iii.Change partition types
iv.Also setup bootable flag
sudo: Runs it with superuser privileges.
fdisk: Starts the partitioning tool for MBR-style partition tables .
/dev/sda: Targets the entire disk (not just a partition like /dev/sda1).

![WhatsApp Image 2025-06-14 at 13 49 01_fa6aac00](https://github.com/user-attachments/assets/f4184b13-be68-4598-aa71-90b001b16bb8)

![WhatsApp Image 2025-06-14 at 13 49 21_03491ace](https://github.com/user-attachments/assets/8d9f77a7-44ad-47ce-84cb-a604f3e50a1c)

![WhatsApp Image 2025-06-14 at 13 49 38_5aec7d38](https://github.com/user-attachments/assets/1f56e5bc-4d43-4b16-9532-926cd366ba7f)

The important commands used in these are:-
p	Print current partition table
n	Create a new partition
d	Delete an existing partition
t	Change partition type
a	Toggle bootable flag
w	Write changes to disk 
q	Quit without saving changes


GPT (Guid Partition Table)
It's a modern way of organizing how your hard disk is divided into chunks (called partitions). It replaced the older system called MBR.
Some features:-
i.Works with newer computers (UEFI-based)(Unified Extensible Firmware Interface.)
ii.Supports big disks (larger than 2 TB)
iii.Allows many partitions without hacks
iv.Has backup copies of the partition table for safety

MBR(Master Boot Record)
It’s the old-school way of organizing a hard drive.
Some features:-
i.It lives in the first 512 bytes of the disk
ii.Stores info for up to 4 primary partitions
iii.Includes a tiny bit of code to start the boot process


MFKS command:-mkfs formats a partition by creating a new filesystem on it—like setting up the structure so files can be stored in an organized way.
![WhatsApp Image 2025-06-14 at 15 04 07_beb7c597](https://github.com/user-attachments/assets/ec0fda8e-e39d-4909-8a9f-520284021d1f)
This command is basically doing:-
sudo: Run with superuser privileges .
mkfs.exfat: The tool that creates an exFAT file system.(exFAT stands for Extended File Allocation Table. 
It’s a filesystem created by Microsoft, designed to be a lightweight, cross-platform solution.)
/dev/sda1: The target partition you’re trying to format.


Some other important parts:-
i.Mounting storage volume:-Connecting a formatted partition (like /dev/sdb1) to a directory (like /mnt/usb) so you can read/write files on it.
ii.Temp file system:-A temporary in-memory filesystem (tmpfs) often used for /tmp, /run, etc.—fast and auto-clears on reboot.
iii.Mounting a file sys:-The act of making any supported filesystem (ext4, vfat, ntfs, etc.) usable by attaching it to a directory.
iv.Installing ncdu:-ncdu stands for NCurses Disk Usage—a super helpful CLI tool to explore disk space usage interactively.
(CLI-CLI stands for Command Line Interface. It’s a way of interacting with your computer using plain text commands,
instead of clicking buttons in a graphical interface.Its like directly talikng to the computer without mouse or keyboard.
Commands like ls, cd, mkdir, rsync, and git are all CLI-based.)
v.sudo ncdu:-Launches ncdu with root access—important if you want to scan system directories you normally can’t access.
vi.Scan:-ncdu scans the disk or directory you point it at and visually shows where your space is going.
vii.fstab file:-/etc/fstab is the config file that tells Linux which filesystems to auto-mount at boot—and how to mount them.
