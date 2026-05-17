# CS0424IT: EPICODE Cybersecurity Specialist

12-week intensive at EPICODE (May-September 2024) covering red-team (recon,
OSINT, web exploitation, post-exploitation) and blue-team (SOC, SIEM, IR,
malware analysis, forensics) tracks, with three multi-week capstone projects.

Final cert: [Cybersecurity Specialist, EPICODE](certifications/epicode/EpicodeCertificate.pdf)
Author: [Simone La Porta](https://github.com/Shurtug4l) | [LinkedIn](https://linkedin.com/in/simonelaporta)

---

## Build Weeks (capstones)

### [`projects/bw1_red_team_foundations/`](projects/bw1_red_team_foundations/)

Offensive intro: HTTP brute-force scripts against DVWA and phpMyAdmin login
forms, custom TCP port scanner, HTTP status enumerator, before/after SQL
injection lab (`vulnerable.php` vs `corrected.php`), LSB steganography
encode/decode toolkit, and a multi-stage CTF chain (`BONUS_theta_steg/`)
extracting nested base64-encoded flags from an ASCII-art payload. Network
design built in Cisco Packet Tracer.

Stack: Python (`requests`, `PIL`, `socket`, `logging`), PHP, MySQL, Cisco
Packet Tracer.
Deliverables: presentation PDF + video, compendium, project quote.

### [`projects/bw2_pentesting_exploitation/`](projects/bw2_pentesting_exploitation/)

End-to-end red-team chain: SQL injection script + MD5 dictionary cracker,
stored-XSS payload, hand-rolled C buffer overflow (`bof_final.c`),
Metasploit exploitation of Metasploitable2 and Windows XP backed by Nessus
scans, three VulnHub box walkthroughs (Vancouver, Dina, DerpNStink) with
flag captures, OverTheWire Bandit progression.

Stack: C, Python (`hashlib`, `requests`), Metasploit, Nessus, Burp Suite,
Wireshark.
Deliverables: full presentation PDF, bonus presentation PDF.

### [`projects/bw3_malware_analysis/`](projects/bw3_malware_analysis/)

Blue-team capstone: static and dynamic analysis of a malware sample, with
behaviour mapping, IOC extraction, and full reporting.

Deliverable: malware analysis report PDF.

---

## Course structure

| Unit | Weeks | Focus | Capstone |
|------|-------|-------|----------|
| [Unit 1](coursework/unit_1_intro_and_recon/) | 1-3 | Linux and networking basics, OWASP Top 10, OSINT, reconnaissance | [BW1](projects/bw1_red_team_foundations/) |
| [Unit 2](coursework/unit_2_pentesting_redteam/) | 5-7 | Enumeration, exploitation, password attacks, web pentesting | [BW2](projects/bw2_pentesting_exploitation/) |
| [Unit 3](coursework/unit_3_blueteam_forensics/) | 9-11 | SOC and SIEM, incident response, forensics, malware analysis | [BW3](projects/bw3_malware_analysis/) |

Weekly lessons live under `coursework/`. Directory convention `SXLY` = Sessione X, Lezione Y.

---

## Certifications

Earned during the program or directly adjacent:

| Issuer | Certificate | File |
|--------|-------------|------|
| EPICODE | Cybersecurity Specialist (final) | [`epicode/EpicodeCertificate.pdf`](certifications/epicode/EpicodeCertificate.pdf) |
| Cisco | Ethical Hacker | [`cisco/Ethical_Hacker.pdf`](certifications/cisco/Ethical_Hacker.pdf) |
| Cisco | Junior Cybersecurity Analyst (pathway) | [`cisco/Junior_Cybersecurity_Analyst/`](certifications/cisco/Junior_Cybersecurity_Analyst/7_Junior_Cybersecurity_Analyst.pdf) |
| EC-Council | Digital Forensics Essentials | [`ec_council/DFE_Essentials.pdf`](certifications/ec_council/DFE_Essentials.pdf) |
| EC-Council | Ethical Hacking Essentials | [`ec_council/Ethical_Hacking_Essentials.pdf`](certifications/ec_council/Ethical_Hacking_Essentials.pdf) |
| EC-Council | SQL Injection Attacks | [`ec_council/SQL_Injection_Attacks.pdf`](certifications/ec_council/SQL_Injection_Attacks.pdf) |
| Security Blue Team | BTL1 Pathway Bundle | [`security_blue_team/`](certifications/security_blue_team/BTJAPathwayBundleCertificate.pdf) |
| Semgrep | Application Security Foundations L1-L3 + Secure Coding | [`semgrep/`](certifications/semgrep/) |

---

## Topics covered

```
network        TCP/IP, OSI, switching, routing, VLANs, Wireshark, Nmap, pfSense
recon          OSINT, Google dorking, Shodan, dark-web operations (Tor)
web            OWASP Top 10, SQLi, XSS, CSRF, brute-force, Burp Suite, SQLmap
exploitation   Metasploit, Nessus, manual exploit dev (C BoF), payload gen,
               post-exploitation, privilege escalation (Linux + Windows)
forensics      disk imaging, memory analysis, IOC extraction, timeline
malware        static + dynamic analysis, sandboxing, reverse engineering
defense        SOC, SIEM (Splunk), IR playbooks, threat hunting
secure code    Semgrep, code-review patterns, ASF L1-L3, secure-by-design
```

---

## Repository layout

```
CS0424IT/
├── projects/                Build Weeks (flagship deliverables)
│   ├── bw1_red_team_foundations/
│   ├── bw2_pentesting_exploitation/
│   └── bw3_malware_analysis/
├── coursework/              weekly lessons (SXLY = Sessione X Lezione Y)
│   ├── unit_1_intro_and_recon/    weeks 1-3
│   ├── unit_2_pentesting_redteam/ weeks 5-7
│   └── unit_3_blueteam_forensics/ weeks 9-11
└── certifications/          earned during the program
    ├── cisco/
    ├── ec_council/
    ├── epicode/
    ├── security_blue_team/
    └── semgrep/
```
