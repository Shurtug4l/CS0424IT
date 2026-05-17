# Build Week 1: Red Team Foundations

Multi-vector offensive intro after weeks 1-3 of the program. Mixes web
exploitation, scanning, network design, and steganography. Capstone of
[Unit 1](../../coursework/unit_1_intro_and_recon/).

## Components

### [`brute_force_dvwa/`](brute_force_dvwa/) & [`brute_force_phpmyadmin/`](brute_force_phpmyadmin/)
Python HTTP brute-force against DVWA and phpMyAdmin login forms. Uses
`requests.Session()` to preserve cookies and supports finding either the
first valid credential or every valid pair. Wordlists and run results
captured in-tree.

### [`scan_ports/`](scan_ports/)
Python TCP port scanner with structured logging. Reads target IP from
stdin, scans a configurable port range via raw `socket.connect()`, and
emits a timestamped log file.

### [`http_status/`](http_status/)
HTTP status enumerator: probes a list of URLs and reports response codes,
useful as a reconnaissance primitive.

### [`BONUS_sql_injection/`](BONUS_sql_injection/)
Before/after SQL injection lab. `vulnerable.php` demonstrates unsanitized
string concatenation; `corrected.php` applies prepared statements as the
fix. Didactic pair for a hands-on walkthrough.

### [`BONUS_steganography/`](BONUS_steganography/)
LSB steganography encoder and decoder in Python (`PIL`). Embeds a text
message bit-by-bit into image pixel least-significant-bits and decodes
it back.

### [`BONUS_theta_steg/`](BONUS_theta_steg/)
Multi-stage CTF: an ASCII-art payload (`help.txt`) encodes nested base64
flags. Chain: ASCII pattern decode, base64 layers, brainfuck program
(`brainfuck.py`). Intermediate flags captured in `flag-aa.txt` through
`flag-ah.txt`.

### `design_rete.pdf` / `design_rete.pkt`
Multi-site network architecture designed in Cisco Packet Tracer.

## Stack

Python (`requests`, `PIL`, `socket`, `logging`), PHP, MySQL, Cisco Packet
Tracer, DVWA, phpMyAdmin.

## Deliverables

- [`presentazione/BW1_Theta_Project_presentation.pdf`](presentazione/BW1_Theta_Project_presentation.pdf) + `.mp4` video
- [`presentazione/BW1_Bonus_presentation.pdf`](presentazione/BW1_Bonus_presentation.pdf) + `.mp4` video
- [`presentazione/BW1_compendio.pdf`](presentazione/BW1_compendio.pdf) (project compendium)
- [`presentazione/BW1_preventivo.pdf`](presentazione/BW1_preventivo.pdf) (project quote)
