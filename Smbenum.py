import smbclient

def find_samba_shares(domain):

    smb_shares = []

    

    try:

        # Connect to the domain

        with smbclient.SambaClient(domain) as client:

            # List all the shares

            shares = client.listShares()

            for share in shares:

                # Add share name to the list

                smb_shares.append(share.name)

    except smbclient.OperationFailure as e:

        print(f"Failed to connect to the domain: {e}")

    return smb_shares

# Replace 'foo.co.uk' with your actual domain

domain = 'foo.co.uk'

# Find all the Samba shares in the domain

shares = find_samba_shares(domain)

# Print the found shares

if shares:

    print("Samba shares found:")

    for share in shares:

        print(share)

else:

    print("No Samba shares found in the domain.")

