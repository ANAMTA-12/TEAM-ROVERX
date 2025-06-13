Why Internet Protocols Matter?

i.Devices across different networks have varying speeds and capabilities.
ii.Protocols handle flow control (e.g., slow receiver tells fast sender to throttle)
iii.They also manage access control (preventing data collisions on shared links)

Some Internet Protocols:-
1. TCP/IP
TCP (Transmission Control Protocol):
i.Connection-oriented; ensures reliable, ordered delivery.
ii.Handles retransmissions, error-checking, flow control; forms the backbone of apps like web, email, FTP

IP (Internet Protocol):
i.Assigns unique IP addresses; routes packets across networks.

2. UDP (User Datagram Protocol)
i.Connectionless, “fire-and-forget” protocol.
ii.No guarantees: no ordering, retransmission, or handshakes.
iii.Fast—great for streaming, VoIP, gaming

3. FTP / SFTP(File Transfer Protocol / Secure File Transfer Protocol)
FTP: Classic client-server file transfer over TCP (ports 21/control, 20/data).
Plain text authentication; can be secured with SSL/TLS (FTPS) or replaced with SSH-based SFTP

4. HTTP / HTTPS(Hypertext Transfer Protocol / Hypertext Transfer Protocol Secure)
HTTP: Base protocol for web pages—client-server model over TCP.
HTTPS: Secure version (HTTP + TLS/SSL), encrypts web traffic.

5. SMTP / POP3 / IMAP (Simple Mail Transfer Protocol / Post Office Protocol Version 3 / Internet Message Access Protocol)
SMTP: Sending of emails between servers/clients.
POP3: Download emails from server.
IMAP: Access/manage emails directly on server

6. PPP (Point-to-Point Protocol)
i.Layer 2 protocol used for direct links (dial-up, DSL).
ii.Handles framing, authentication (PAP/CHAP), compression, and error detection

7.TELNET (Telecommunication Network)
Introduced: 1969, one of the oldest protocols.
Port Used: TCP port 23
Function: Allows users to log into a remote computer and run commands.
Main Issue:
No encryption – All data sent in plain text.
Vulnerable to eavesdropping and attacks.

8.SSH (Secure Shell)
A cryptographic network protocol used to securely access and manage remote systems over an unsecured network.
Replaces older, insecure protocols like Telnet and FTP.
Runs on TCP port 22.
i.All communication between client and server is encrypted, ensuring confidentiality.
ii.Uses public-private key pairs or passwords to verify identity.
iii.Ensures that data isn’t tampered with during transmission.
iv.Can securely forward other network connections through encrypted channels.
SSH Keys
Public Key: Shared openly; used to encrypt data.
Private Key: Kept secret; used to decrypt data.
Key Types:
User Key: Both keys are with the user.
Host Key: Keys are stored on the remote system.
Session Key: Used for encrypting large data transfers.

9.IPv4(Internet Protocol Version 4)
IPv4 is the fourth version of the Internet Protocol,and it’s the one that still powers most of the internet today. 
It’s like the addressing system of the internet—just as a house has a postal address, every device on a network needs an IP address to communicate.
i.IPv4 uses 32-bit addresses, typically shown as four numbers separated by dots (like 192.168.0.1).
ii.It supports about 4.3 billion unique addresses—not nearly enough for today’s internet-connected world.
iii.That shortage is what led to the development of IPv6, which has a much larger address pool.

10.IPv6(Internet Protocol Version 6)
IPv6 is like the next-gen upgrade to IPv4 a major leap to support the future of the internet.
i.It uses 128-bit addresses, which means it can support about 340 undecillion unique IP addresses (that’s 340 followed by 36 zeros!). 
So basically, every grain of sand could have its own IP.
ii.Pv6 addresses look like this: 2001:0db8:85a3:0000:0000:8a2e:0370:7334. Not exactly something you’d memorize, but very powerful.
iii.With so many addresses, devices don’t need to share IPs using Network Address Translation (NAT)—a common workaround in IPv4.
iv.IPsec (for encrypted traffic) is baked into IPv6, making secure communications more standard.
v.Devices can assign themselves an IP address automatically.

11.ICMP(Internet Control Message Protocol)
A network layer protocol used for error reporting and diagnostics.
It’s not used to exchange data between systems but to send control messages.
Commonly used by routers and network devices to report issues like unreachable hosts or network congestion.
i.IP lacks built-in error handling, so ICMP steps in to notify senders about delivery problems.
ii.Helps in troubleshooting and network diagnostics.
iii.Doesn’t require a handshake like TCP.
iv.For example, if a packet is too large or a route fails.
v.Sends echo requests and waits for replies to check connectivity.
vi.Maps the path packets take across the network.
How ICMP Works
When a problem occurs (e.g., packet can’t reach destination), an ICMP message is sent back to the source.
These messages help the sender adjust or reroute communication.

12.UDP(User Datagram Protocol)
A Transport Layer protocol in the Internet Protocol suite (UDP/IP).
Connectionless and unreliable—doesn’t guarantee delivery, order, or error checking.
Prioritizes speed and efficiency over reliability.
i.Data is sent without establishing a connection.
ii.Lightweight protocol with minimal header size (8 bytes).
iii.Leaves error handling to the application or other protocols like ICMP.
iv.Uses source and destination port numbers to identify processes.
UDP Header Fields
Source Port (2 bytes): Identifies sender’s port.
Destination Port (2 bytes): Identifies receiver’s port.
Length (2 bytes): Total length of header + data.
Checksum (2 bytes): Optional error-checking field.
Applications of UDP
i.VoIP (e.g., Skype, WhatsApp), video conferencing.
ii.Online games, live broadcasts.
iii.Quick request-response cycles.
iv.Like RIP (Routing Information Protocol).
v.Efficient for sending data to multiple recipients.

13.IMAP(Internet Message Access Protocol)
An application layer protocol used to retrieve and manage emails from a mail server.
Designed by Mark Crispin in 1986, currently at version IMAP4.
Unlike POP3, IMAP keeps emails on the server and syncs across all devices.
i.Read, delete, or move an email on one device, and it reflects everywhere.
ii.Organize emails into folders directly on the server.
iii.Mark emails as read, important, etc.
iv.Retrieve just headers or full content as needed.
v.Manages media files without downloading the entire message.
How IMAP Works
Follows a client-server architecture over TCP/IP.
Default ports:
143: Non-encrypted communication.
993: Encrypted communication (SSL/TLS).
The client connects to the server and syncs email data in real time.

14.Gopher
Gopher is a text-based protocol developed before the World Wide Web.
It allowed users to browse and retrieve documents from remote servers using a menu-driven interface.
Think of it like navigating folders and files on your computer—but across the internet.
How Gopher Works
i.You use a Gopher client to connect to a Gopher server.
ii.The server displays a list of files and folders.
iii.Clicking an item downloads and displays the file on your device.
Features
i.No images or fancy formatting—just fast, simple content.
ii.Organized like a tree structure for easy navigation.
iii.Ideal for slow or limited internet connections.

