
# HOW TO pull a docker image and login to that container as root 
# C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker pull --help

# Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

# Pull an image or a repository from a registry

# Options:
#  -a, --all-tags                Download all tagged images in the repository
#      --disable-content-trust   Skip image verification (default true)
#      --platform string         Set platform if server is multi-platform
#                                capable
#  -q, --quiet                   Suppress verbose output

#C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker pull oraclelinux:9
#9: Pulling from library/oraclelinux
#07773263ab23: Pull complete
#Digest: sha256:01c7e8c446a9a8a9565f4a98505aa14f09c1b6bce0935a5b606b18c4d1545a63
#Status: Downloaded newer image for oraclelinux:9
#docker.io/library/oraclelinux:9

#C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker ps
#CONTAINER ID   IMAGE           COMMAND       CREATED              STATUS              PORTS     NAMES
#f657e6f247f6   oraclelinux:9   "/bin/bash"   About a minute ago   Up About a minute             angry_goodall

#C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker exec -it angry_goodall /bin/bash
#[root@f657e6f247f6 /]# pwd
#/
#[root@f657e6f247f6 /]# whoami
#root
#[root@f657e6f247f6 /]# :)
#bash: syntax error near unexpected token `)'
#[root@f657e6f247f6 /]# ls -a
#.   .dockerenv  bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
#..  afs         boot  etc  lib   media  opt  root  sbin  sys  usr


-----------------------------------------------------------------------------------
# HOW TO login to linux docker image 
# SSH into a Container
# Use docker ps to get the name of the existing container.
# Use the command docker exec -it <container name> /bin/bash to get a bash shell in the container.
# Generically, use docker exec -it <container name> <command> to execute whatever command you specify in the container.


-----------------------------------------------------------------------------------

# HOW TO create users
# useradd -m <username> 
#
# Home directories
# In order to create a user with the default home directory use the following option:
#
# useradd -m test
#
# This user now has a /home/test directory.

# Add a password
# You then add a password for the test user by using the passwd command: passwd test. This will prompt you to enter a password for the user.

# There is an option for adding an encrypted password via the -p option on useradd, but this is not recommended for security purposes.

# Note that the -p option doesn't allow you to input a plaintext password, it expects you to encrypt it first. This is intentionally difficult, because you should not do it! Just use the passwd command.

-----------------------------------------------------------------------------------

# HOW TO check user rights and how to set them - https://www.redhat.com/sysadmin/manage-permissions 
# https://linuxopsys.com/topics/give-normal-user-root-privileges#:~:text=Edit%20%2Fetc%2Fpasswd%20for%20the,give%20root%20permissions%20to%20user.
# Method  1: Adding to Root Group using usermod
# Let's see how we can grant normal user root access by adding to root group.

# adduser user1
# adduser user2
# groupadd test
# These are the groups I have in my Linux box.

# groups
# root bin daemon sys adm disk wheel
# I am going to add user1 to root group as follows:

# usermod -G root user1
# The following usermod command given below provides the existing user with the root privilege

# usermod -g 0 -o root_user
# Method 2: Adding to Root Group using Useradd Command
# I have added a new user, 'user3' to the root group using one single command:


# useradd -m -G root user3
# groups user3
# user3 : user3 root
# Another option using useradd command

# useradd -c “Imitation Root” -d /home/root_user -m -k /etc/skel -s /bin/bash -u 0 -o -g root root_user
# Method 3: Editing /etc/passwd file
# Edit /etc/passwd for the particular user. Change the user's UID and GID to '0'. This will give root permissions to user.

# root:x:0:0:root:/root:/bin/bash
# temproot:x:128:128:temproot
# Now, temproot user should have root privilege:

# root:x:0:0:root:/root:/bin/bash
# temproot:x:0:0:temproot
# Note: This is not the recommended method for granting root access

# Method 4: Setting as Sudo User
# The sudo configuration file is /etc/sudoers and you can edit this file using visudo command: # visudo.

# Using visudo protects from conflicts and guarantees that the right syntax is used.


# To give full access (grant root privileges) to specific users

# Add the entry given below in the file:

# bob, tom ALL=(ALL) ALL
# Following this method is not a good idea because this allows both bob and tom to use the su command to grant themselves permanent root privileges. Thereby skipping the command logging features of sudo.

# Granting access to specific files to one particular user

# This entry allows bob and all the other members of the group operator to gain access to all the program files in the /sbin and /usr/sbin directories, as well as the privilege of running the command /usr/oracle/backup.pl.


# bob, %operator ALL= /sbin/, /usr/sbin, /usr/oracle/backup.pl
# Conclusion
# In this tutorial, we learned how to allow root access to a user in a Linux system.

# Login in as root and running commands is dangerous because all commands are with the highest privileges. Accident mistakes can even delete root directories and unsafe to run programs with a root shell.



-------------------------
# Oracle Linux is using YUM as package manager, therefore below are the yum command options:
# [root@f657e6f247f6 /]# yum -h
# usage: yum [options] COMMAND

# List of Main Commands:

# alias                     List or create command aliases
# autoremove                remove all unneeded packages that were originally installed as dependencies
# check                     check for problems in the packagedb
# check-update              check for available package upgrades
# clean                     remove cached data
# deplist                   [deprecated, use repoquery --deplist] List package's dependencies and what packages provide them
# distro-sync               synchronize installed packages to the latest available versions
# downgrade                 Downgrade a package
# group                     display, or use, the groups information
# help                      display a helpful usage message
# history                   display, or use, the transaction history
# info                      display details about a package or group of packages
# install                   install a package or packages on your system
# list                      list a package or groups of packages
# makecache                 generate the metadata cache
# mark                      mark or unmark installed packages as installed by user.
# module                    Interact with Modules.
# provides                  find what package provides the given value
# reinstall                 reinstall a package
# remove                    remove a package or packages from your system
# repolist                  display the configured software repositories
# repoquery                 search for packages matching keyword
# repository-packages       run commands on top of all packages in given repository
# search                    search package details for the given string
# shell                     run an interactive YUM shell
# swap                      run an interactive YUM mod for remove and install one spec
# updateinfo                display advisories about packages
# upgrade                   upgrade a package or packages on your system
# upgrade-minimal           upgrade, but only 'newest' package match which fixes a problem that affects your system

# List of Plugin Commands:

# builddep                  Install build dependencies for package or spec file
# changelog                 Show changelog data of packages
# config-manager            manage yum configuration options and repositories
# copr                      Interact with Copr repositories.
# debug-dump                dump information about installed rpm packages to file
# debug-restore             restore packages recorded in debug-dump file
# debuginfo-install         install debuginfo packages
# download                  Download package to current directory
# groups-manager            create and edit groups metadata file
# needs-restarting          determine updated binaries that need restarting
# playground                Interact with Playground repository.
# repoclosure               Display a list of unresolved dependencies for repositories
# repodiff                  List differences between two sets of repositories
# repograph                 Output a full package dependency graph in dot format
# repomanage                Manage a directory of rpm packages
# reposync                  download all packages from remote repo

# General YUM options:
  # -c [config file], --config [config file]
                        # config file location
  # -q, --quiet           quiet operation
  # -v, --verbose         verbose operation
  # --version             show YUM version and exit
  # --installroot [path]  set install root
  # --nodocs              do not install documentations
  # --noplugins           disable all plugins
  # --enableplugin [plugin]
                        # enable plugins by name
  # --disableplugin [plugin]
                        # disable plugins by name
  # --releasever RELEASEVER
                        # override the value of $releasever in config and repo files
  # --setopt SETOPTS      set arbitrary config and repo options
  # --skip-broken         resolve depsolve problems by skipping packages
  # -h, --help, --help-cmd
                        # show command help
  # --allowerasing        allow erasing of installed packages to resolve dependencies
  # -b, --best            try the best available package versions in transactions.
  # --nobest              do not limit the transaction to the best candidate
  # -C, --cacheonly       run entirely from system cache, don't update cache
  # -R [minutes], --randomwait [minutes]
                        # maximum command wait time
  # -d [debug level], --debuglevel [debug level]
                        # debugging output level
  # --debugsolver         dumps detailed solving results into files
  # --showduplicates      show duplicates, in repos, in list/search commands
  # -e ERRORLEVEL, --errorlevel ERRORLEVEL
                        # error output level
  # --obsoletes           enables yum's obsoletes processing logic for upgrade or display capabilities that the package obsoletes for info, list and repoquery
  # --rpmverbosity [debug level name]
                        # debugging output level for rpm
  # -y, --assumeyes       automatically answer yes for all questions
  # --assumeno            automatically answer no for all questions
  # --enablerepo [repo]   Enable additional repositories. List option. Supports globs, can be specified multiple times.
  # --disablerepo [repo]  Disable repositories. List option. Supports globs, can be specified multiple times.
  # --repo [repo], --repoid [repo]
                        # enable just specific repositories by an id or a glob, can be specified multiple times
  # --enable              enable repos with config-manager command (automatically saves)
  # --disable             disable repos with config-manager command (automatically saves)
  # -x [package], --exclude [package], --excludepkgs [package]
                        # exclude packages by name or glob
  # --disableexcludes [repo], --disableexcludepkgs [repo]
                        # disable excludepkgs
  # --repofrompath [repo,path]
                        # label and path to an additional repository to use (same path as in a baseurl), can be specified multiple times.
  # --noautoremove        disable removal of dependencies that are no longer used
  # --nogpgcheck          disable gpg signature checking (if RPM policy allows)
  # --color COLOR         control whether color is used
  # --refresh             set metadata as expired before running the command
  # -4                    resolve to IPv4 addresses only
  # -6                    resolve to IPv6 addresses only
  # --destdir DESTDIR, --downloaddir DESTDIR
                        # set directory to copy packages to
  # --downloadonly        only download packages
  # --comment COMMENT     add a comment to transaction
  # --bugfix              Include bugfix relevant packages, in updates
  # --enhancement         Include enhancement relevant packages, in updates
  # --newpackage          Include newpackage relevant packages, in updates
  # --security            Include security relevant packages, in updates
  # --advisory ADVISORY, --advisories ADVISORY
                        # Include packages needed to fix the given advisory, in updates
  # --bz BUGZILLA, --bzs BUGZILLA
                        # Include packages needed to fix the given BZ, in updates
  # --cve CVES, --cves CVES
                        # Include packages needed to fix the given CVE, in updates
  # --sec-severity {Critical,Important,Moderate,Low}, --secseverity {Critical,Important,Moderate,Low}
                        # Include security relevant packages matching the severity, in updates
  # --forcearch ARCH      Force the use of an architecture
  
# Example of jenkins controller address: https://jenkins.cerner.com/rom/view/SCP%20Tooling/   
# Temporary password for jenkins installation: 3e23beda39694f70a67e61fc2e878d5b 
# *************************************************************
# *************************************************************
# *************************************************************

# Jenkins initial setup is required. An admin user has been created and a password generated.
# Please use the following password to proceed to installation:

# 3e23beda39694f70a67e61fc2e878d5b

# This may also be found at: /root/.jenkins/secrets/initialAdminPassword

# *************************************************************
# *************************************************************
# *************************************************************

# I guess I need to fix this: https://forums.docker.com/t/systemctl-status-is-not-working-in-my-docker-container/9075/2 ---> !!!!!!!!!!!!!!

# Usefull commands:
# service --status-all
# pstree
# pstree | head -n 5
# EXAMPLE: pstree -c -G -h -l -n -p -s -t -u -U -Z

---------------------------------------------------------------
# HOW TO check current user: use 'id' command in terminal
# HOW TO check currently logged in users: use 'w' command in terminal


---------------------------------------------------------------
# HOW TO list users in groups and check current user : https://www.cyberciti.biz/faq/linux-list-all-members-of-a-group/
# Linux Show All Members of a Group Commands
# /etc/group file – User group file
# members command – List members of a group
# lid command (or libuser-lid on newer Linux distros) – List user’s groups or group’s users
# There are two types of groups in Linux:

# Primary group – is the main group that is associated with user account. Each user is a member of exactly one primary group.
# Secondary group – used to provide additional rights to user. For example, access to the dvd/cdrom drive can be granted with help of cdrom group.
# Linux: List all members of a group using /etc/group file
# Use the grep command or cat command/more command as follows:
# $ grep 'grpup-name-here' /etc/group
# $ grep 'ftponly' /etc/group
# $ cat /etc/group
# $ less /etc/group
# $ grep -i --color 'ftponly' /etc/group

# ftponly:x:1001:raj,vivek,archana,sai,sayali
# We can also type the compgen command or getend command to list all group names on Linux:
# $ compgen -g
# $ getent group

# To get just a list of all members of a group called ftponly, type the following awk command:

# awk -F':' '/ftponly/{print $4}' /etc/group
# # list all members of sudo group in linux #
# awk -F':' '/sudo/{print $4}' /etc/group
# Display group memberships for each Linux user
# Want to see group memberships for each given USERNAME under Linux? The syntax is as follows for the groups command:
# groups
# groups {USERNAME}
# groups vivek

# The following outputs indicates that the user named ‘vivek’ is part of four groups including ‘vivek’ primary group:

# vivek : vivek wheel lxd vboxusers

# HOW TO Create a docker compose file so that the systemctl is up and running as a process when starting the docker container, and, while at it, also try to put jenkins and prerequisities in the installation docker file section.

vycUQi/jpYltp3I1$yYQTJesSlYELVaznDYaQ8XeXyzXSdh8mkb5wwagv8BdHlxYpuqE7AZ8tjNtTl2RmOtE

$6$vycUQi/jpYltp3I1$yYQTJesSlYELVaznDYaQ8XeXyzXSdh8mkb5wwagv8BdHlxYpuqE7AZ8tjNtTl2RmOtE.rycoQp6krxlgYHOYK.:19276:0:99999:7:::
E:$6$vycUQi/jpYltp3I1$yYQTJesSlYELVaznDYaQ8XeXyzXSdh8mkb5wwagv8BdHlxYpuqE7AZ8tjNtTl2RmOtE.rycoQp6krxlgYHOYK.:19276:0:99999:7:::
ADE:$6$vycUQi/jpYltp3I1$yYQTJesSlYELVaznDYaQ8XeXyzXSdh8mkb5wwagv8BdHlxYpuqE7AZ8tjNtTl2RmOtE.rycoQp6krxlgYHOYK.:19276:0:99999:7:::


# HOW TO ls command - other command is tree
# Examples that work for me:
# A: ls -a -c -C -F --file-type -l -g
# B: ls -a -c -C -F --classify -l -g
# C: ls -a -c -C -F --file-type -l -g -i -p --indicator-style=slash -R -x
# D: ls -a -c -C -F --file-type -l -g -i -p --indicator-style=slash -R -x -Z --context
# E: ls -a -c -C -F --file-type -l -g -i -p --indicator-style=slash -R -x -Z --context -l
# F: ls -a -l -i - shortest option to get a pretty good result
# F: ls -a -l -i -p - shortest option to get a pretty good result, with the -p addition also marks directories with a '/' at their end 



# [root@f657e6f247f6 bin]# ls --help
# Usage: ls [OPTION]... [FILE]...
# List information about the FILEs (the current directory by default).
# Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

# Mandatory arguments to long options are mandatory for short options too.
  # -a, --all                  do not ignore entries starting with .
  # -A, --almost-all           do not list implied . and ..
      # --author               with -l, print the author of each file
  # -b, --escape               print C-style escapes for nongraphic characters
      # --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                               # e.g., '--block-size=M'; see SIZE format below
  # -B, --ignore-backups       do not list implied entries ending with ~
  # -c                         with -lt: sort by, and show, ctime (time of last
                               # modification of file status information);
                               # with -l: show ctime and sort by name;
                               # otherwise: sort by ctime, newest first
  # -C                         list entries by columns
      # --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                               # if omitted), 'auto', or 'never'; more info below
  # -d, --directory            list directories themselves, not their contents
  # -D, --dired                generate output designed for Emacs' dired mode
  # -f                         do not sort, enable -aU, disable -ls --color
  # -F, --classify             append indicator (one of */=>@|) to entries
      # --file-type            likewise, except do not append '*'
      # --format=WORD          across -x, commas -m, horizontal -x, long -l,
                               # single-column -1, verbose -l, vertical -C
      # --full-time            like -l --time-style=full-iso
  # -g                         like -l, but do not list owner
      # --group-directories-first
                             # group directories before files;
                               # can be augmented with a --sort option, but any
                               # use of --sort=none (-U) disables grouping
  # -G, --no-group             in a long listing, don't print group names
  # -h, --human-readable       with -l and -s, print sizes like 1K 234M 2G etc.
      # --si                   likewise, but use powers of 1000 not 1024
  # -H, --dereference-command-line
                             # follow symbolic links listed on the command line
      # --dereference-command-line-symlink-to-dir
                             # follow each command line symbolic link
                               # that points to a directory
      # --hide=PATTERN         do not list implied entries matching shell PATTERN
                               # (overridden by -a or -A)
      # --hyperlink[=WHEN]     hyperlink file names; WHEN can be 'always'
                               # (default if omitted), 'auto', or 'never'
      # --indicator-style=WORD  append indicator with style WORD to entry names:
                               # none (default), slash (-p),
                               # file-type (--file-type), classify (-F)
  # -i, --inode                print the index number of each file
  # -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  # -k, --kibibytes            default to 1024-byte blocks for disk usage;
                               # used only with -s and per directory totals
  # -l                         use a long listing format
  # -L, --dereference          when showing file information for a symbolic
                               # link, show information for the file the link
                               # references rather than for the link itself
  # -m                         fill width with a comma separated list of entries
  # -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  # -N, --literal              print entry names without quoting
  # -o                         like -l, but do not list group information
  # -p, --indicator-style=slash
                             # append / indicator to directories
  # -q, --hide-control-chars   print ? instead of nongraphic characters
      # --show-control-chars   show nongraphic characters as-is (the default,
                               # unless program is 'ls' and output is a terminal)
  # -Q, --quote-name           enclose entry names in double quotes
      # --quoting-style=WORD   use quoting style WORD for entry names:
                               # literal, locale, shell, shell-always,
                               # shell-escape, shell-escape-always, c, escape
                               # (overrides QUOTING_STYLE environment variable)
  # -r, --reverse              reverse order while sorting
  # -R, --recursive            list subdirectories recursively
  # -s, --size                 print the allocated size of each file, in blocks
  # -S                         sort by file size, largest first
      # --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                               # time (-t), version (-v), extension (-X)
      # --time=WORD            change the default of using modification times;
                               # access time (-u): atime, access, use;
                               # change time (-c): ctime, status;
                               # birth time: birth, creation;
                             # with -l, WORD determines which time to show;
                             # with --sort=time, sort by WORD (newest first)
      # --time-style=TIME_STYLE  time/date format with -l; see TIME_STYLE below
  # -t                         sort by time, newest first; see --time
  # -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  # -u                         with -lt: sort by, and show, access time;
                               # with -l: show access time and sort by name;
                               # otherwise: sort by access time, newest first
  # -U                         do not sort; list entries in directory order
  # -v                         natural sort of (version) numbers within text
  # -w, --width=COLS           set output width to COLS.  0 means no limit
  # -x                         list entries by lines instead of by columns
  # -X                         sort alphabetically by entry extension
  # -Z, --context              print any security context of each file
  # -1                         list one file per line.  Avoid '\n' with -q or -b
      # --help     display this help and exit
      # --version  output version information and exit

# The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
# Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).
# Binary prefixes can be used, too: KiB=K, MiB=M, and so on.

# The TIME_STYLE argument can be full-iso, long-iso, iso, locale, or +FORMAT.
# FORMAT is interpreted like in date(1).  If FORMAT is FORMAT1<newline>FORMAT2,
# then FORMAT1 applies to non-recent files and FORMAT2 to recent files.
# TIME_STYLE prefixed with 'posix-' takes effect only outside the POSIX locale.
# Also the TIME_STYLE environment variable sets the default style to use.

# Using color to distinguish file types is disabled both by default and
# with --color=never.  With --color=auto, ls emits color codes only when
# standard output is connected to a terminal.  The LS_COLORS environment
# variable can change the settings.  Use the dircolors command to set it.

# Exit status:
 # 0  if OK,
 # 1  if minor problems (e.g., cannot access subdirectory),
 # 2  if serious trouble (e.g., cannot access command-line argument).

# GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
# Report any translation bugs to <https://translationproject.org/team/>
# Full documentation <https://www.gnu.org/software/coreutils/ls>
# or available locally via: info '(coreutils) ls invocation'

# HOW TO Use command tree
# Examples that work for me:
# tree -a -l -f -R -N
# tree -a -l -f -R -N -Q -p -u -g -h
# tree -a -l -f -R -N -Q -p -u -g -s
# tree -a -l -f -R -N -Q -p -u -g -s -D --inodes
# tree -a -l -f -R -N -Q -p -u -g -s -D --inodes --device -C
# tree -a -l -f -R -N -Q -p -u -g -s -D --inodes --device -C -X

# [root@f657e6f247f6 bin]# tree --help
# usage: tree [-acdfghilnpqrstuvxACDFJQNSUX] [-H baseHREF] [-T title ]
        # [-L level [-R]] [-P pattern] [-I pattern] [-o filename] [--version]
        # [--help] [--inodes] [--device] [--noreport] [--nolinks] [--dirsfirst]
        # [--charset charset] [--filelimit[=]#] [--si] [--timefmt[=]<f>]
        # [--sort[=]<name>] [--matchdirs] [--ignore-case] [--fromfile] [--]
        # [<directory list>]
  # ------- Listing options -------
  # -a            All files are listed.
  # -d            List directories only.
  # -l            Follow symbolic links like directories.
  # -f            Print the full path prefix for each file.
  # -x            Stay on current filesystem only.
  # -L level      Descend only level directories deep.
  # -R            Rerun tree when max dir level reached.
  # -P pattern    List only those files that match the pattern given.
  # -I pattern    Do not list files that match the given pattern.
  # --ignore-case Ignore case when pattern matching.
  # --matchdirs   Include directory names in -P pattern matching.
  # --noreport    Turn off file/directory count at end of tree listing.
  # --charset X   Use charset X for terminal/HTML and indentation line output.
  # --filelimit # Do not descend dirs with more than # files in them.
  # --timefmt <f> Print and format time according to the format <f>.
  # -o filename   Output to file instead of stdout.
  # --du          Print directory sizes.
  # --prune       Prune empty directories from the output.
  # ------- File options -------
  # -q            Print non-printable characters as '?'.
  # -N            Print non-printable characters as is.
  # -Q            Quote filenames with double quotes.
  # -p            Print the protections for each file.
  # -u            Displays file owner or UID number.
  # -g            Displays file group owner or GID number.
  # -s            Print the size in bytes of each file.
  # -h            Print the size in a more human readable way.
  # --si          Like -h, but use in SI units (powers of 1000).
  # -D            Print the date of last modification or (-c) status change.
  # -F            Appends '/', '=', '*', '@', '|' or '>' as per ls -F.
  # --inodes      Print inode number of each file.
  # --device      Print device ID number to which each file belongs.
  # ------- Sorting options -------
  # -v            Sort files alphanumerically by version.
  # -t            Sort files by last modification time.
  # -c            Sort files by last status change time.
  # -U            Leave files unsorted.
  # -r            Reverse the order of the sort.
  # --dirsfirst   List directories before files (-U disables).
  # --sort X      Select sort: name,version,size,mtime,ctime.
  # ------- Graphics options -------
  # -i            Don't print indentation lines.
  # -A            Print ANSI lines graphic indentation lines.
  # -S            Print with CP437 (console) graphics indentation lines.
  # -n            Turn colorization off always (-C overrides).
  # -C            Turn colorization on always.
  # ------- XML/HTML/JSON options -------
  # -X            Prints out an XML representation of the tree.
  # -J            Prints out an JSON representation of the tree.
  # -H baseHREF   Prints out HTML format with baseHREF as top directory.
  # -T string     Replace the default HTML title and H1 header with string.
  # --nolinks     Turn off hyperlinks in HTML output.
  # ------- Input options -------
  # --fromfile    Reads paths from files (.=stdin)
  # ------- Miscellaneous options -------
  # --version     Print version and exit.
  # --help        Print usage and this help message and exit.
  # --            Options processing terminator.
  
  
# HOW TO start commandctl or something like that , systemd, etc. to finish the jenkins installation on the Linux Docker container.

  