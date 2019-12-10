# rcle
## RunCloud Let's Encrypt Automation
Install Let's Encrypt SSL on RunCloud.io servers

Credit:
https://github.com/rehmatworks/runcloud-letsencrypt

### Changelog:

v1.0.0
- Initial release
- Drop support TLS 1.0 TLS 1.1

read more https://blog.qualys.com/ssllabs/2018/11/19/grade-change-for-tls-1-0-and-tls-1-1-protocols
- Add support TLS 1.3 (TLS 1.2 TLS 1.3)

### Requirement
```bash
pip install wheel
```

### Installation
```bash
pip install rcle
```

### Usage
```bash
usage: PROG [-h] [-i {all}] [-u {all}] [-r] [-a {disable,enable}]

optional arguments:
  -h, --help            show this help message and exit
  -i, --install
                        Install SSL certificate on an app or on all available
                        apps. Provide the target app name or type all to
                        install SSL on all apps.
  -u, --uninstall
                        Uninstall SSL certificate from an app or from all
                        available apps.
  -r, --renew           Renew all installed SSl certificates.
  -a {disable,enable}, --autopilot {disable,enable}
                        Enable or disable auto-pilot mode.
```

### Examples
To install SSL on all available apps:
```bash
rcle -i all
```
And to install SSL on a specific app:
```bash
rcle -i appname
```

Autopilot mode automatically retrieves and installs SSL certificates on your new apps without needing you to sign in and run the install command.

To enable autopilot mode:
```bash
rcle -a enable

```
and to disable autopilot mode
```bash
rcle -a disable
```
To uninstall SSL certificate from all apps:
```bash
rcle -u all
```

And to uninstall SSL certificate from a specific app:
```bash
rcle -u appname
```
