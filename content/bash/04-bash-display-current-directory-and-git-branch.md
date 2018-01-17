Title: Bash Display Current Directory & Git Branch 
Date: 2018-01-17 15:44
tags: bash

The following is a screenshot.

![screenshot of terminal](images/current-directory-and-branch.png)

Make a backup of .bashrc

Find this section in the .bashrc file 

```sh
if [ "$color_prompt" = yes ]; then
    if [[ ${EUID} == 0 ]] ; then
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\h\[\033[01;34m\] \W \$\[\033[00m\] '
    else
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\] \[\033[01;34m\]\w \$\[\033[00m\] '
    fi
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h \w \$ '
fi
unset color_prompt force_color_prompt
```

Replace it with

```sh
parse_git_branch() {
git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

if [ "$color_prompt" = yes ]; then
    if [[ ${EUID} == 0 ]] ; then
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\h\[\033[01;34m\] \W \$\[\033[00m\] '
    else
        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\] \[\033[01;34m\]\W \[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '
    fi
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h \W \$ '
fi
unset color_prompt force_color_prompt
```

Save the .bashrc file

To see the changes either open a fresh terminal window or run the following in a currently open terminal window

```sh
source ~/.bashrc
```

This article was created using <a href="http://dillinger.io/" target="_blank">dillinger</a>, an open source markdown editor. 