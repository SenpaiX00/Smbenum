from smbprotocol.connection import Connection


def find_samba_shares(domain, username, password):
    smb_shares = []

    try:
        # Establish a connection to the domain
        connection = Connection(username, password, domain)

        # Connect to the server
        connection.connect()

        # List shares on the server
        shares = connection.list_shares()

        for share in shares:
            # Add share name to the list
            smb_shares.append(share.name)

        # Disconnect from the server
        connection.disconnect()

    except Exception as e:
        print(f"Failed to connect to the domain: {e}")

    return smb_shares


# Replace 'foo.co.uk' with your actual domain
domain = 'foo.co.uk'
username = 'your_username'
password = 'your_password'

# Find all the Samba shares in the domain
shares = find_samba_shares(domain, username, password)

# Print the found shares
if shares:
    print("Samba shares found:")
    for share in shares:
        print(share)
else:
    print("No Samba shares found in the domain.")
