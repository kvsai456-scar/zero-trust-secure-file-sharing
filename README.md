# Zero Trust Secure File Sharing (Proof of Concept)

## Overview

This project is a **Zero Trust–inspired secure file sharing system** designed as a **proof of concept (PoC)** to demonstrate core security principles such as client-side encryption, least-privilege access, and auditability.

Files are encrypted in the browser before being uploaded to the server. The server never has access to plaintext data and only stores encrypted files and limited metadata. Access is controlled through time-limited and usage-limited download links.

This project is intended for **learning, demonstration, and portfolio purposes only** and is not production-ready.

---

## Core Security Principles

* **Zero Trust Architecture**
  The system assumes the server is untrusted. All sensitive data is encrypted on the client before transmission.

* **Client-Side Encryption**
  Files are encrypted in the browser using AES-GCM before upload.

* **Least Privilege Access**
  Shared links are restricted by expiration time and maximum number of downloads.

* **Auditability**
  Upload and download events are logged for visibility into file access activity.

---

## Features

* Client-side file encryption using AES-GCM (256-bit)
* Secure upload and download workflow
* Time-limited and usage-limited sharing links
* Basic audit logging for file access events
* Simple web interface
* Python Flask backend

---

## Architecture Overview

1. User selects a file in the browser.
2. The file is encrypted locally using AES-GCM.
3. The encrypted file is uploaded to the server.
4. The server stores only encrypted data and metadata.
5. A secure link is generated with expiration and usage limits.
6. The recipient downloads the encrypted file and decrypts it locally using the shared key.

---

## Technology Stack

* Frontend: HTML, CSS, JavaScript (Web Crypto API)
* Backend: Python (Flask)
* Encryption: AES-GCM (Client-side)
* Storage: Local server storage / in-memory metadata

---

## Installation and Setup

### Prerequisites

* Python 3.8 or higher
* Git
* Modern web browser (Chrome, Firefox, or Edge recommended)

### Clone the Repository

```bash
git clone https://github.com/kvsai456-scar/zero-trust-secure-file-sharing.git
cd zero-trust-secure-file-sharing
```

### Install Dependencies

```bash
pip install flask
```

### Run the Server

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## Usage

1. Open the web interface in your browser.
2. Select a file to upload.
3. The file will be encrypted automatically in the browser.
4. A download link and encryption key will be generated.
5. Share the link and key securely with the recipient.
6. The recipient uses the key to decrypt the file after downloading.

---

## Project Status: Proof of Concept

This project is a **demonstration of Zero Trust concepts**, not a production-ready secure file sharing platform.

### What This Project Is

* A learning-focused security prototype
* A portfolio project demonstrating cryptography and secure system design
* A foundation for building a real Zero Trust file sharing system

### What This Project Is Not

* Not production hardened
* Not certified for real-world sensitive data
* Not compliant with enterprise security standards

---

## Known Security Limitations

This implementation intentionally simplifies or omits several critical security features:

* No automated key exchange (encryption keys must be shared manually)
* No user authentication or identity verification
* No enforced HTTPS/TLS configuration
* In-memory metadata storage (non-persistent audit logs and link states)
* Limited server-side hardening and threat mitigation
* No rate limiting or replay protection

Because of these limitations, this system **must not be deployed in real environments** without major security upgrades.

---

## Roadmap to Production-Ready

To convert this PoC into a secure platform, the following features must be implemented:

* Secure key exchange (ECDH or RSA-based)
* Strong TLS enforcement and certificate validation
* User authentication and role-based access control
* Persistent, tamper-evident audit logging
* Rate limiting and replay protection
* Secure storage backend and server hardening
* Full threat modeling and penetration testing
* Deployment using a production-grade WSGI server and hardened infrastructure

---

## Threat Model Summary

### Threats Considered

* Man-in-the-middle attacks
* Unauthorized access via leaked links
* Server compromise
* Replay attacks
* Brute force attempts on access endpoints

### Current Mitigations

* Client-side encryption prevents server-side data exposure
* Link expiration and usage limits reduce long-term exposure
* Basic audit logs provide visibility into access events

---

## Disclaimer

This software is provided for **educational and demonstration purposes only**.
Do not use this system to store or share sensitive, personal, or confidential data in real-world environments.
