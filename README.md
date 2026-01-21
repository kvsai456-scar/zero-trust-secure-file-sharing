# Zero-Trust Secure File Sharing System

A secure file sharing web application that enforces client-side encryption, controlled access, and auditability under a zero-trust security model.  
The server never stores or processes plaintext files — all encryption and decryption occur in the client’s browser.

---

## Key Security Principles

- Zero Trust Architecture  
  Every request is validated. Shared links are not treated as authorization.
- Client-Side Encryption (AES-GCM 256-bit)  
  Files are encrypted in the browser before upload. The server only stores encrypted blobs.
- Controlled Access Links  
  Time-limited and download-limited links reduce exposure.
- Audit Logging & Alerts  
  All uploads and downloads are logged for traceability and misuse detection.

---

## System Architecture

**Flow:**
1. Sender selects a file in the browser  
2. File is encrypted locally using AES-GCM  
3. Encrypted file is uploaded to the server  
4. Server stores encrypted file and issues a time-bound download token  
5. Receiver downloads encrypted file  
6. Receiver decrypts locally using the shared key and IV  

**Trust Boundaries:**
- Client → Server: Only encrypted data crosses this boundary  
- Server → Storage: Only encrypted blobs are persisted  
- User → Link: Every request is validated under access policies  

---

## Features

- Client-side file encryption (AES-GCM, 256-bit)
- Time-bound, limited-use download links
- Unauthorized first-download detection
- Full audit log (uploads, downloads, link abuse)
- Single-origin architecture (no CORS dependency)
- Secure file storage (encrypted-only persistence)

---

## Tech Stack

- Frontend: HTML, JavaScript (Web Crypto API)  
- Backend: Python, Flask  
- Storage: Local filesystem (demo), extensible to S3 or cloud storage  
- Security: AES-GCM encryption, zero-trust access model  

---

## Project Structure

```
zero-trust-secure-file-sharing/
├── backend/
│   ├── backend.py
│   ├── audit.log
│   └── storage/
├── client/
│   ├── index.html
│   └── decrypt.html
└── docs/
    └── threat-model.md
```

---

## Setup and Run

### Prerequisites
- Python 3.9+
- Browser with Web Crypto API support (Chrome, Edge, Firefox)

### Install Dependencies
```
pip install flask
```

### Run Server
```
cd backend
python backend.py
```

Open in browser:
```
http://127.0.0.1:5000
```

---

## Usage Flow

### Sender
1. Open the app in the browser  
2. Select a file  
3. Click Encrypt & Upload  
4. Copy:
   - Download link  
   - IV  
   - Encrypted AES key  

### Receiver
1. Open `/decrypt.html`  
2. Upload the `.enc` file  
3. Paste:
   - IV  
   - Encrypted AES key  
4. Click Decrypt File  
5. Download original file  

---

## Audit Logs

View system logs:
```
http://127.0.0.1:5000/logs
```

Logs include:
- Upload events
- Download attempts
- Expired link access
- Download limit violations

---

## Threat Model Summary

| Threat | Mitigation |
|--------|------------|
| Server breach | Files stored encrypted only |
| Link theft | Expiry and download limits |
| Unauthorized access | Token validation and audit logs |
| Insider misuse | Traceability via logs |
| File tampering | AES-GCM integrity checks |

---

## Limitations

- AES key sharing is manual in this demo (out-of-band)
- No sandbox-based malware analysis
- In-memory metadata storage (non-persistent on restart)
- Not production-hardened (no TLS, no authentication layer)

---

## Future Improvements

- Hybrid key exchange (RSA or ECDH)
- Database-backed metadata and logs
- TLS enforcement
- Cloud storage integration (S3, GCS)
- Behavioral malware analysis
- Role-based access control

---

## Resume Description

Built a zero-trust secure file sharing system using client-side AES-GCM encryption, time-bound access tokens, and full audit logging, ensuring the server never stores or processes plaintext data.

---

## License
MIT

---

## Author
Your Name  
Cybersecurity, Application Security, and Cloud Security Enthusiast
