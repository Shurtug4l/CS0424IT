from impacket.smbconnection import SMBConnection

def os_fingerprint_no_auth(ip):
    try:
        # Crea una connessione SMB anonima
        smb = SMBConnection(ip, ip)
        smb.login('', '')  # Login anonimo
        smb_info = smb.getServerOS()
        print(f'OS Information for {ip}: {smb_info}')
        smb.logoff()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_ip = '192.168.50.101'  # Sostituisci con l'IP del sistema Windows 7

    os_fingerprint_no_auth(target_ip)
