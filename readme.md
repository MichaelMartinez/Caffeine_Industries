## Caffeine Industries - Pelican Site

This is the repo of the [Caffeine Industries](http://caffeineindustries.com) website.

### Instructions

With perseverance I will update this blog regularly and these instructions will be redundant. That said, I haven't used
pelican since version 2 and need some help remembering the commands. These instructions will serve that role.

1. `pelican content` -> generate the html while in development.
2. `cd output` -> change to output directory
3. `python -m pelican.server` -> runs a development server to check html
4. `cd ..` -> back to top level
5. `make ssh_upload` -> pass for ssh key in lastpass. Host is configured in ~/.ssh/config, generated keys inside ~/.ssh/cpanel
6. BACKUP ONLY - `make ftp_upload` -> publish the site: Password is in lastpass if you forget ;P

Todo:
1. Automation -> one step to publish
2. Write more!

## License

&copy; 2015-2017 Michael Martinez

This repository is licensed under the MIT license. See `LICENSE` for
details.
