#Glacier Command Line Utility ![Version](https://img.shields.io/badge/version-2014.03.0-red.svg?style=flat) [![MIT license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
===

Command line wrapper around Boto's Amazon Glacier support.

Basic help menu:
```bash
usage: glacier [-h] [-d] [-a ACCESS_KEY] [-s SECRET_KEY] [-k]
               {us-east-1,ap-northeast-1,ap-southeast-2,cn-north-1,us-west-2,us-west-1,eu-central-1,eu-west-1}
               {freeze,ls,create,delete} ...

Glacier CLI Utility

positional arguments:
  {us-east-1,ap-northeast-1,ap-southeast-2,cn-north-1,us-west-2,us-west-1,eu-central-1,eu-west-1}
                        Region to use.
  {freeze,ls,create,delete}
                        subcommand help
    freeze              Send a file to Glacier.
    ls                  List vaults or keys in vaults.
    create              Create a vault.
    delete              Delete a key or an empty vault.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enabled debug-level logging.
  -a ACCESS_KEY, --access_key ACCESS_KEY
                        Access key to use.
  -s SECRET_KEY, --secret_key SECRET_KEY
                        Secret key to use.
  -k, --insecure        Do not verify server SSL certificate.
```

Creating (buckets):
```bash
usage: glacier
        {us-east-1,ap-northeast-1,ap-southeast-2,cn-north-1,us-west-2,us-west-1,eu-central-1,eu-west-1} create
       [-h] vault

positional arguments:
  vault       Vault name.

optional arguments:
  -h, --help  show this help message and exit

$ ./glacier us-east-1 create mark_test
```

Listing:
```bash
usage: glacier
        {us-east-1,ap-northeast-1,ap-southeast-2,cn-north-1,us-west-2,us-west-1,eu-central-1,eu-west-1} ls
       [-h] [vault [vault ...]]

positional arguments:
  vault       Bucket to list.

optional arguments:
  -h, --help  show this help message and exit

$ ./glacier us-east-1 ls
[Vault("arn:aws:glacier:us-east-1:054653668741:vaults/test")]

$ ./glacier us-east-1 ls test
[]
```

Freezing:
```bash
usage: glacier
        {us-east-1,ap-northeast-1,ap-southeast-2,cn-north-1,us-west-2,us-west-1,eu-central-1,eu-west-1} freeze
       [-h] [--description DESCRIPTION] vault filename

positional arguments:
  vault                 Vault to send frozen file to.
  filename              File to freeze.

optional arguments:
  -h, --help            show this help message and exit
  --description DESCRIPTION
                        Description to add to fozen file.

$ ./glacier us-east-1 freeze test test.txt
3iPTJ3KwJsRpggCDGcZHE9RtETTcjKIxUowoTcLDfdo...
```

Thawing:
```bash
TODO
```

Deleting:
```bash
usage: glacier
        {us-east-1,ap-northeast-1,ap-southeast-2,cn-north-1,us-west-2,us-west-1,eu-central-1,eu-west-1} delete
       [-h] vault [key]

positional arguments:
  vault       Vault name.
  key         Key name.

optional arguments:
  -h, --help  show this help message and exit

$ ./glacier us-east-1 delete test 3iPTJ3KwJsRpggCDGcZHE9RtETTcjKIxUowoTcLDfdo...
```
