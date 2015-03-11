import boto
import boto.glacier


def connect(region=None, access_key=None, secret_key=None, **kwargs):
    return boto.glacier.connect_to_region(
        region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )

def ls(**args):
    vaults = args.pop('vaults', list())
    if not vaults: # Empty list of vaults - print vaults.
        print(connect(**args).list_vaults())
    else:
        for vault in vaults:
            # NOTE this needs to be modified - glacier too slow for first pass
            print(connect(**args).layer1.describe_vault(vault))
    

def create(**args):
    vault = args.pop('vault')
    connect(**args).create_vault(vault)

def delete(**args):
    vault = args.pop('vault')
    key = args.pop('key', str())
    if not key:
        connect(**args).delete_vault(vault)
    else:
        connect(**args).get_vault(vault).delete_archive(key)

def freeze(**args):
    description = args.pop('description',str())
    filename = args.pop('filename')
    vault = args.pop('vault')
    print(connect(**args).get_vault(vault).upload_archive(filename, description))
