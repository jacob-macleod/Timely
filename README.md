- [Timely](#timely)
  - [Status](#status)
  - [Usage](#usage)
  - [Compatibility](#compatibility)
  - [Installation](#installation)
    - [Docker](#docker)
    - [Git](#git)
  - [Contact and Bug Reports](#contact-and-bug-reports)

# Timely
Timely is a Productivity Timer (with analytics for users with an account)

Timely is self-hosted, and you are free to host it as a public server.

## Status
**Finished**

I've developed the first version, and I have no plans to develop any more versions

## Usage
Timely is self-hosted.

**Also**, if you self-host Timely, you'll need to replace all references to `http://localhost:5000`(/something) with the base url of your server.

If you want to use Timely as a PWA, please replace all references to `http://localhost:5000`(/) with `(the base url of your server)/index.html`

**IMPORTANT** - The encryption key for the login data is publically shown in `database.py`, so you should change it. However, even then the encryption isn't that good - it's only a Ceaser Cipher

## Compatibility 
Timely is compatible with all operating systems, including mobile as a PWA, except IOS. This is because IOS Safari introduces limitations with audio that make this app impossible to use - the timer makes no sound.

To find out how to install progressive web apps on Android, please refer to this [link](https://support.google.com/chrome/answer/9658361?co=GENIE.Platform%3DAndroid&hl=en).


## Installation
### Docker
This is the reccomended method to install - once you've installed docker (please refer to [here](https://www.docker.com/products/docker-desktop)) you can simply run, `docker run -p 5000:5000 jacobmacleod/timely`

### Git
Alternatively, you can clone the master branch with `git clone --single-branch --branch master https://github.com/jacob-macleod/Timely`, then run main.py with python3 main.py. You will need to install python 3 and flask for the code and git for the clone command - if you have installed pip3, you can install flask with pip3 install flask.

You can then navigate to http://localhost:5000/.

*This is not the reccomended option, but it is necessary for active development*

## Contact and Bug Reports
If you have any questions or are experiencing a bug, please open an issue [here](https://github.com/jacob-macleod/Timely/issues).