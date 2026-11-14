# 🚀 BOOT CAMP – Networking & Web Development Fundamentals

A structured collection of learning notes covering networking, client-server architecture, web technologies, internet communication, and cybersecurity fundamentals.

---

# 📚 Lecture 1 – Client-Server Architecture

## 1. What is Client-Server Architecture?

Client-Server Architecture is a communication model in which two main components interact with each other:

- Client: A device or application that requests information or services.
- Server: A computer or system that receives requests, processes them, and sends responses.

**In simple words: The client asks, and the server responds.**

### Examples of Clients
- Web browsers (Google Chrome, Firefox).
- Mobile applications (WhatsApp, Facebook).
- Smart TVs.
- Desktop applications.
- Gaming consoles.

### What is a Server?

A server is a powerful computer designed to provide services, resources, and information to other devices over a network.

Important points:
- Linux is one of the most commonly used server operating systems.
- Windows Server is also used in enterprise environments.
- Not all websites are hosted on Linux.
- Servers can handle multiple client requests simultaneously.
- Servers can be hosted in data centers or cloud platforms.

## 2. Types of Servers and Their Responsibilities

Different servers perform different tasks. Each type has its own speciality.

| Server Type | Responsibility | Examples |
|---|---|---|
| Web Server | Delivers website files and web pages. | Apache, Nginx |
| Application Server | Executes application code and business logic. | Django applications, Gunicorn |
| Database Server | Stores, manages, and retrieves data. | MySQL, PostgreSQL |
| File Server | Stores and shares files. | Google Drive, Amazon S3 |
| Mail Server | Sends, receives, and stores emails. | Gmail, Outlook |
| DNS Server | Converts domain names into IP addresses. | Google DNS (8.8.8.8), Cloudflare DNS (1.1.1.1) |

### Real-World Example

When you log in to an online shopping website:

1. The web server delivers the website.
2. The application server processes your login request.
3. The database server checks your username and password information.
4. The file storage service provides product images.
5. The mail service may send a confirmation email.

All these services work together to provide a complete experience.

## 3. Client-Server vs Peer-to-Peer (P2P)

### Client-Server Architecture

In this architecture, multiple clients communicate with a central server.

Advantages:
- Centralized management.
- Easier security and access control.
- Centralized data backup.
- Easy monitoring and maintenance.
- Multiple users can access shared resources.

Disadvantages:
- Server failure can interrupt services.
- Requires maintenance and infrastructure.
- Heavy traffic can overload the server.

Examples: Facebook, YouTube, Gmail, online banking.

### Peer-to-Peer Architecture (P2P)

In P2P architecture, devices communicate directly with each other without depending on one central server for every communication.

Each device is called a peer and can act as both a client and a server.

Advantages:
- No central server is required for every operation.
- Direct resource sharing.
- Workload can be distributed.
- Can continue working when some peers disconnect.

Disadvantages:
- Security management can be difficult.
- Backup and data management are more complicated.
- Performance depends on available peers.
- Peers can disconnect unexpectedly.

Examples:
- BitTorrent.
- Direct file sharing between computers.
- Decentralized blockchain networks such as Bitcoin.

### Simple Example

Imagine five friends sharing files.

- Client-Server: All five friends upload files to one central computer, and everyone downloads files from that computer.
- P2P: Friends share files directly with one another without depending on one central computer.

## 4. How Request and Response Work

Request and Response is the basic communication process between a client and a server.

### Communication Process

1. User Action: The user types a URL or clicks a link.
2. DNS Resolution: The browser finds the IP address of the domain.
3. Connection: The browser connects to the server through the network and ISP.
4. HTTP/HTTPS Request: The browser sends a request to the web server.
5. Backend Processing: The server processes the request and communicates with the database if needed.
6. HTTP/HTTPS Response: The server sends the requested information back.
7. Rendering: The browser processes HTML, CSS, and JavaScript and displays the webpage.

### Request-Response Diagram

```text
       USER
        |
        v
   WEB BROWSER
        |
        | DNS Lookup
        v
    DNS SERVER
        |
        | Returns IP Address
        v
   INTERNET / ISP
        |
        | HTTP / HTTPS Request
        v
   WEB SERVER
        |
        v
   BACKEND LOGIC
        |
        v
     DATABASE
        |
        | Requested Data
        v
   BACKEND SERVER
        |
        | HTTP Response
        v
    WEB BROWSER
        |
        v
   RENDER WEBSITE
```

## 5. What Does a Browser Actually Send?

When you enter a website or submit a form, the browser sends an HTTP request.

Example:

```http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "username": "ammar",
  "password": "example123"
}
```

Let's understand the request:

- `POST`: HTTP method used to send information.
- `/login`: Requested resource or endpoint.
- `HTTP/1.1`: HTTP protocol version.
- `Host`: Website domain.
- `Content-Type`: Type of data being sent.
- Request Body: Contains the submitted information.

### What Does the Server Send Back?

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Login successful"
}
```

The server sends:
- HTTP version.
- Status code.
- Status message.
- Response headers.
- Response body.

### Common HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | OK – Request successful. |
| 201 | Created – Resource created successfully. |
| 301 | Moved Permanently. |
| 400 | Bad Request. |
| 401 | Unauthorized. |
| 403 | Forbidden. |
| 404 | Page or resource not found. |
| 500 | Internal Server Error. |
| 503 | Service Unavailable. |

**Remember:**

- `404` means the requested resource could not be found.
- `500` means something went wrong on the server.

## 6. CRUD Operations

CRUD stands for:

- Create
- Read
- Update
- Delete

These are the four basic operations performed on data.

| CRUD Operation | HTTP Method | Purpose |
|---|---|---|
| Create | POST | Creates new data. |
| Read | GET | Retrieves data. |
| Update | PUT / PATCH | Updates existing data. |
| Delete | DELETE | Removes data. |

### Example: Student Management System

- POST: Add a new student.
- GET: Display student information.
- PUT: Replace all or most of a student's information.
- PATCH: Update only the student's email address.
- DELETE: Remove a student record.

## 7. HTTP vs HTTPS

HTTP: Hypertext Transfer Protocol.

HTTPS: Hypertext Transfer Protocol Secure.

HTTPS uses TLS encryption to protect communication between the browser and server.

| HTTP | HTTPS |
|---|---|
| Communication is not encrypted by HTTP itself. | Communication is encrypted using TLS. |
| Data can be exposed if intercepted. | Protects data during transmission. |
| No TLS protection. | Uses TLS certificates. |
| Usually uses port 80. | Usually uses port 443. |

### GET vs POST

| GET | POST |
|---|---|
| Mainly retrieves information. | Mainly submits information. |
| Parameters may appear in the URL. | Data is commonly sent in the request body. |
| Can appear in browser history. | Request body does not normally appear in the URL. |
| Can be cached under certain conditions. | Not normally cached by default. |

Important Security Concept:

POST is not automatically secure, and GET is not automatically insecure.

HTTPS encrypts HTTP communication, including the request body, URL path, and query string while in transit.

Never send passwords or sensitive information over unencrypted HTTP.

## 8. HTML vs JSON

### HTML

HTML stands for HyperText Markup Language.

It is used to structure content that browsers display to users.

Example:

```html
<h1>Welcome Ammar</h1>
<p>Welcome to my website.</p>
```

### JSON

JSON stands for JavaScript Object Notation.

It is a lightweight data format used to exchange information between applications and systems.

Example:

```json
{
  "name": "Ammar",
  "age": 25,
  "profession": "Developer"
}
```

Difference:
- HTML structures webpage content.
- JSON represents and exchanges structured data.

## 9. Sessions and Cookies

HTTP is a stateless protocol. This means each HTTP request is independent, and HTTP does not automatically remember previous requests.

To maintain user login information, websites commonly use sessions and cookies.

### Cookie

A cookie is a small piece of information stored in the user's browser.

### Session

A session is a mechanism used by the server to maintain information about a user's interaction with an application.

### How Login Sessions Work

1. User enters username and password.
2. Server verifies the login information.
3. Server creates a session.
4. Server sends a session cookie to the browser using `Set-Cookie`.
5. Browser stores the cookie.
6. Browser sends the cookie with subsequent requests.
7. Server identifies the user through the session.

**Important:** Session cookies should be protected using HTTPS and appropriate security settings such as HttpOnly and Secure.

## 10. What Are APIs?

API stands for Application Programming Interface.

An API allows two software applications to communicate and exchange information.

Simple example:

Imagine you have a frontend website and a backend developed using Django.

- Frontend: Displays the login form.
- API: Sends login information to the backend.
- Backend: Processes the request.
- Database: Checks the user's information.
- API: Returns the result to the frontend.

### API Communication

```text
FRONTEND (HTML/CSS/JS)
          |
          v
       API REQUEST
          |
          v
    DJANGO BACKEND
          |
          v
       DATABASE
          |
          v
      API RESPONSE
          |
          v
       FRONTEND
```

APIs commonly exchange data in JSON format.

## 11. What Happens When You Type a URL?

Example:

`https://www.daraz.pk`

1. You enter the URL in your browser.
2. The browser checks available DNS information.
3. A DNS resolver finds the IP address associated with the domain.
4. Your device connects to the destination server through your internet connection.
5. A secure connection is established using TLS.
6. The browser sends an HTTPS request.
7. The server processes the request.
8. The server sends an HTTP response.
9. The browser renders the website.

### What is an ISP?

ISP stands for Internet Service Provider.

An ISP provides internet connectivity to homes, businesses, and organizations.

Examples:
- PTCL.
- StormFiber.
- Nayatel.
- Jazz.
- Zong.

Public IP Address:

An ISP typically assigns a public IP address to your internet connection or router. This address allows your network to communicate with other networks over the internet.

Your devices usually have private IP addresses inside your local network, and NAT allows them to share the public IP address.

## 12. Static Websites vs Dynamic Websites

### Static Website

A static website delivers pre-created files such as HTML, CSS, JavaScript, and images.

The content generally remains the same for visitors unless the files are updated.

Examples:
- Personal portfolio.
- Company information website.
- Simple landing page.

### Dynamic Website

A dynamic website can generate or customize content based on user actions, database information, and application logic.

Examples:
- Facebook.
- YouTube.
- Daraz.
- Online banking.
- E-commerce websites.

| Static Website | Dynamic Website |
|---|---|
| Mostly pre-created content. | Content can change dynamically. |
| May not require a database. | Often uses a database. |
| Generally simpler to develop. | Requires application logic. |
| Good for simple websites. | Good for interactive applications. |

## 13. What is Web Hosting?

Web hosting is a service that makes your website accessible through the internet.

A hosting provider stores your website files and provides the infrastructure needed to serve them to visitors.

### Domain vs Hosting

- Domain: The human-readable website address, such as `example.com`.
- Hosting: The server infrastructure where your website files and applications run.
- DNS: Connects your domain name to the relevant server IP address.

### Types of Web Hosting

| Hosting Type | Explanation |
|---|---|
| Shared Hosting | Multiple websites share the same server resources. |
| VPS Hosting | A virtual private server provides allocated resources within a physical server. |
| Dedicated Hosting | One customer gets an entire physical server. |
| Cloud Hosting | Uses multiple connected computing resources to provide hosting services. |

---

# 🌐 Lecture 2 – How the Internet Works

## 1. What is the Internet?

The internet is a global network of interconnected computer networks.

Billions of devices communicate through networking technologies and standardized protocols.

Examples:
- Computers.
- Smartphones.
- Servers.
- Smart TVs.
- IoT devices.
- Network routers.

The internet allows these devices to exchange information from almost anywhere in the world.

## 2. Internet vs World Wide Web (WWW)

These two terms are related but not identical.

### Internet

The internet is the global infrastructure connecting devices and networks.

### World Wide Web

The World Wide Web is a collection of interconnected websites and web resources accessed through the internet.

Simple difference:

- Internet = The network infrastructure.
- WWW = Websites and web pages available through that network.

The web commonly uses HTTP and HTTPS for communication.

## 3. Evolution of the Web

### Web 1.0 – Read Only

Web 1.0 mainly consisted of static websites.

Users could read information but had limited interaction.

Examples: Early informational websites and online directories.

### Web 2.0 – Read and Write

Web 2.0 introduced interactive websites and user-generated content.

Users can create, share, comment, and communicate.

Examples:
- Facebook.
- YouTube.
- Instagram.
- Wikipedia.

### Web 3.0 – Decentralized Web Vision

Web 3.0 is commonly associated with decentralized technologies, blockchain, and user-controlled digital assets.

Examples:
- Decentralized applications (dApps).
- Blockchain-based services.
- Cryptocurrency networks.

## 4. What Happens When You Search on Google?

When you search something on Google, your computer does not search Google's entire internet database using its own CPU.

Instead:

1. Your browser sends a search request.
2. Google's servers receive the request.
3. Google's search systems use an enormous search index.
4. The search engine retrieves and ranks relevant information.
5. Results are sent back to your browser.
6. Your browser displays the results.

**Important distinction:**

Your CPU performs local operations, while Google's infrastructure performs the server-side search and ranking operations.

## 5. MAC Address – Hardware Network Identifier

MAC stands for Media Access Control.

A MAC address is a link-layer address associated with a network interface.

It is generally used to identify network interfaces within a local network.

Example:

```text
00:1A:2B:3C:4D:5E
```

**Important points:**
- Used in local network communication.
- Works at the Data Link Layer.
- Usually assigned to a network interface.
- Can be changed or spoofed in software.
- Routers replace the Ethernet/Wi-Fi link-layer frame as packets move between networks.

**MAC Address vs IP Address**

| MAC Address | IP Address |
|---|---|
| Link-layer address. | Network-layer address. |
| Used for local network delivery. | Used for communication across networks. |
| Associated with a network interface. | Assigned through manual configuration or DHCP. |
| Usually represented in hexadecimal. | IPv4 is represented in decimal notation. |

## 6. TCP/IP Model

TCP/IP stands for Transmission Control Protocol / Internet Protocol.

It is the networking model used for communication across the internet.

The commonly taught TCP/IP model has four layers.

| Layer | Responsibility | Examples |
|---|---|---|
| Application | Provides network services to applications. | HTTP, HTTPS, DNS, FTP |
| Transport | Provides communication between applications. | TCP, UDP |
| Internet | Handles logical addressing and routing. | IPv4, IPv6, ICMP |
| Network Access | Handles local network communication and physical transmission. | Ethernet, Wi-Fi |

### Simple Explanation

- Application: What application is communicating?
- Transport: How should data be delivered?
- Internet: Where should the data travel?
- Network Access: How does data travel across the local network?

## 7. What Are Data Packets?

When information travels over a network, it is divided into smaller units of data.

At different networking layers, these units have different names.

| Layer | Data Unit |
|---|---|
| Application | Data |
| Transport | Segment (TCP) / Datagram (UDP) |
| Internet | Packet |
| Network Access | Frame |
| Physical transmission | Bits |

The receiving device processes these units and reconstructs the original information.

Example:

When you download a large file, the information travels across the network in smaller pieces. The receiving device reassembles those pieces into the original file.

## 8. TCP vs UDP

TCP stands for Transmission Control Protocol.

UDP stands for User Datagram Protocol.

Both are transport-layer protocols, but they handle data differently.

| TCP | UDP |
|---|---|
| Connection-oriented. | Connectionless. |
| Reliable delivery mechanisms. | No built-in guarantee of delivery. |
| Maintains data order. | Does not guarantee data order. |
| Retransmits lost data. | No built-in retransmission. |
| More protocol overhead. | Lower protocol overhead. |
| Used for web browsing, email, file transfer. | Used for DNS queries, streaming, gaming, and real-time communication. |

Simple example:

- TCP: Sending an important document where correct and ordered delivery matters.
- UDP: A live voice or video call where receiving the latest information quickly is important.

**Remember:** UDP is not automatically faster in every situation. Performance depends on the application and network conditions.

## 9. Structure of a URL

A URL stands for Uniform Resource Locator.

It is the address used to locate a resource on the internet.

Example:

```text
https://www.daraz.pk/laptops/sort=price
```

### URL Components

| Component | Example | Purpose |
|---|---|---|
| Protocol/Scheme | https | Defines the communication protocol. |
| Subdomain | www | Identifies a subdomain. |
| Domain Name | daraz | Main registered domain label. |
| TLD | .pk | Top-Level Domain. |
| Path | /laptops | Identifies a resource or route. |
| Query String | ?sort=price | Provides additional parameters. |

Important: A query string begins with `?`. In the example above, `sort=price` is part of the path because there is no question mark.

Correct query-string example:

```text
https://www.daraz.pk/laptops?sort=price
Protocol SubDomain Domain Name Path Query
```

---

# 🔐 Lecture 3 – TCP, HTTP, Proxy, and VPN

## 1. Why is TCP Used?

TCP is widely used because it provides reliable, ordered communication between applications.

Its major features include:

- Reliable data delivery.
- Data sequencing.
- Error detection.
- Retransmission of lost data.
- Flow control.
- Congestion control.

### Why Does Reliability Matter?

Imagine downloading an important PDF file.

If some data is missing or arrives incorrectly, the file could become corrupted.

TCP helps solve this problem by tracking data and retransmitting missing information when necessary.

## 2. TCP Three-Way Handshake

Before TCP data communication begins, the two devices establish a connection using a three-way handshake.

The three steps are:

1. SYN
2. SYN-ACK
3. ACK

### Step 1 – SYN

The client sends a SYN packet to the server.

It means:

"I want to establish a TCP connection."

### Step 2 – SYN-ACK

The server responds with SYN-ACK.

It means:

"I received your request, and I am ready to establish the connection."

### Step 3 – ACK

The client sends an ACK packet.

It means:

"I received your response. The connection is established."

### Three-Way Handshake Diagram

```text
       CLIENT                 SERVER
          |                      |
          |       SYN            |
          |--------------------->|
          |                      |
          |      SYN + ACK       |
          |<---------------------|
          |                      |
          |        ACK           |
          |--------------------->|
          |                      |
          |  CONNECTION READY    |
```

**Remember:** SYN, SYN-ACK, ACK.

## 3. What is HTTP?

HTTP stands for Hypertext Transfer Protocol.

It is an application-layer protocol used for communication between clients and web servers.

HTTP is stateless, meaning it does not automatically remember previous requests.

### HTTP as a Rulebook

Think of HTTP as a set of rules that explains how a browser and server exchange information.

It defines:
- Request methods.
- Request headers.
- Response headers.
- Status codes.
- Message structure.

### Common HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve information. |
| POST | Submit information. |
| PUT | Replace or update a resource. |
| PATCH | Partially update a resource. |
| DELETE | Remove a resource. |

## 4. HTTP Versions

HTTP has evolved to improve communication performance and efficiency.

| Version | Main Feature |
|---|---|
| HTTP/1.0 | Basic request-response communication. |
| HTTP/1.1 | Persistent connections and improved performance. |
| HTTP/2 | Multiplexing, header compression, and better efficiency. |
| HTTP/3 | Uses QUIC over UDP to improve connection performance and reliability. |

### Simple Explanation

- HTTP/1.0: Basic communication.
- HTTP/1.1: Reuses connections.
- HTTP/2: Handles multiple streams over one connection.
- HTTP/3: Uses QUIC, which is built on UDP.

## 5. HTTP is Stateless

HTTP does not automatically remember previous requests.

For example:

1. You log in to a website.
2. You open another page.
3. HTTP itself does not remember that you logged in.
4. The website uses cookies, sessions, or tokens to recognize you.

This allows websites to maintain login sessions across multiple requests.

## 6. What is a Proxy Server?

A proxy server acts as an intermediary between a client and another server.

Instead of communicating directly with the destination, the client sends its request through the proxy.

### Forward Proxy

A forward proxy works on behalf of clients.

**Example:**

A company uses a forward proxy to control employees' internet access.

The proxy can:
- Filter websites.
- Apply access policies.
- Monitor network traffic.
- Cache certain content.

### Forward Proxy Diagram

```text
CLIENT
   |
   v
FORWARD PROXY
   |
   v
INTERNET
   |
   v
DESTINATION SERVER
```

## 7. What is a Reverse Proxy?

A reverse proxy works on behalf of backend servers.

It receives requests from clients and forwards them to the appropriate backend server.

### Why Do We Use Reverse Proxies?

- Load balancing.
- Improved security.
- SSL/TLS termination.
- Request filtering.
- Caching.
- Hiding backend server details.

Examples:
- Nginx.
- HAProxy.
- Cloudflare.

### Reverse Proxy Diagram

```text
       CLIENTS
          |
          v
    REVERSE PROXY
          |
     _____|_____
    |     |     |
    v     v     v
 SERVER  SERVER SERVER
   1       2      3
```

The reverse proxy distributes incoming requests across available backend servers.

## 8. What is a VPN?

VPN stands for Virtual Private Network.

A VPN creates an encrypted tunnel between your device and a VPN server.

It helps protect network traffic while it travels through untrusted networks.

### How Does a VPN Work?

1. You connect to a VPN application.
2. Your device establishes an encrypted tunnel with a VPN server.
3. Your internet traffic travels through that tunnel.
4. The VPN server forwards traffic to the destination.
5. The destination generally sees the VPN server's public IP address instead of your original public IP address.

### VPN Diagram

```text
       YOUR DEVICE
            |
            v
     ENCRYPTED TUNNEL
            |
            v
        VPN SERVER
            |
            v
         INTERNET
            |
            v
     DESTINATION WEBSITE
```

### Why Do We Use VPNs?

- Protect traffic on untrusted networks.
- Secure remote access to company networks.
- Change the apparent public IP address.
- Connect remote employees to internal resources.

**Important:** A VPN does not make you completely anonymous or guarantee protection against malware, phishing, or tracking.

---

# 🎯 Final Learning Summary

By completing these three lectures, you should understand:

- Client-server architecture.
- Frontend and backend communication.
- Different types of servers.
- Client-server vs P2P architecture.
- HTTP and HTTPS.
- HTTP methods and status codes.
- CRUD operations.
- Cookies and sessions.
- APIs and JSON.
- DNS and ISP.
- Domain names and web hosting.
- Static and dynamic websites.
- Internet and World Wide Web.
- Web 1.0, Web 2.0, and Web 3.0.
- MAC and IP addresses.
- TCP/IP model.
- Packets, segments, frames, and bits.
- TCP vs UDP.
- TCP three-way handshake.
- HTTP versions and stateless communication.
- Forward proxy and reverse proxy.
- VPN fundamentals.

---

## 📖 Learning Philosophy

**Understand the concept before memorizing the command.**

Networking is the foundation of web development, system administration, and cybersecurity.

Every website, application, and online service depends on communication between devices, networks, and servers.

Keep learning. Keep practicing. Keep building.

Boot Camp – Networking & Web Development Fundamentals