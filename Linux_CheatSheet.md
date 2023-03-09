###################################################### LINUX ######################################################

# Linux Commands Tips&Tricks - CheatSheet

# HOW TO Use command tree
 Examples that work for me:
 tree -a -l -f -R -N
 tree -a -l -f -R -N -Q -p -u -g -h
 tree -a -l -f -R -N -Q -p -u -g -s
 tree -a -l -f -R -N -Q -p -u -g -s -D --inodes
 tree -a -l -f -R -N -Q -p -u -g -s -D --inodes --device -C
 tree -a -l -f -R -N -Q -p -u -g -s -D --inodes --device -C -X
 tree -afl -L 1  <--- shortest ok form
 tree -a -l -f -R -N -Q -p -u -g -s -D -C -L 1  <--- also a very good form
 
 
# HOW TO ls command - other command is tree
 Examples that work for me:
 A: ls -a -c -C -F --file-type -l -g
 B: ls -a -c -C -F --classify -l -g
 C: ls -a -c -C -F --file-type -l -g -i -p --indicator-style=slash -R -x
 D: ls -a -c -C -F --file-type -l -g -i -p --indicator-style=slash -R -x -Z --context
 E: ls -a -c -C -F --file-type -l -g -i -p --indicator-style=slash -R -x -Z --context -l
 F: ls -a -l -i - shortest option to get a pretty good result
 F: ls -a -l -i -p - shortest option to get a pretty good result, with the -p addition also marks directories with a '/' at their end 

# How To Set or Change Linux User Password
# COMMAND INFO: passwd -- it is an interactive command 
# EXAMPLE: passwd <username>
# OTHER OPTION: usermod --password PASSWORD USERNAME


passwd --help
Usage: passwd [OPTION...] <accountName>
  -k, --keep-tokens       keep non-expired authentication tokens
  -d, --delete            delete the password for the named account (root only); also removes password lock if any
  -l, --lock              lock the password for the named account (root only)
  -u, --unlock            unlock the password for the named account (root only)
  -e, --expire            expire the password for the named account (root only)
  -f, --force             force operation
  -x, --maximum=DAYS      maximum password lifetime (root only)
  -n, --minimum=DAYS      minimum password lifetime (root only)
  -w, --warning=DAYS      number of days warning users receives before password expiration (root only)
  -i, --inactive=DAYS     number of days after password expiration when an account becomes disabled (root only)
  -S, --status            report password status on the named account (root only)
      --stdin             read new tokens from stdin (root only)

Help options:
  -?, --help              Show this help message
      --usage             Display brief usage message


# COMMAND INFO: yum
# EXAMPLE: yum

yum --help
usage: yum [options] COMMAND

List of Main Commands:

alias                     List or create command aliases
autoremove                remove all unneeded packages that were originally installed as dependencies
check                     check for problems in the packagedb
check-update              check for available package upgrades
clean                     remove cached data
deplist                   [deprecated, use repoquery --deplist] List package's dependencies and what packages provide them
distro-sync               synchronize installed packages to the latest available versions
downgrade                 Downgrade a package
group                     display, or use, the groups information
help                      display a helpful usage message
history                   display, or use, the transaction history
info                      display details about a package or group of packages
install                   install a package or packages on your system
list                      list a package or groups of packages
makecache                 generate the metadata cache
mark                      mark or unmark installed packages as installed by user.
module                    Interact with Modules.
provides                  find what package provides the given value
reinstall                 reinstall a package
remove                    remove a package or packages from your system
repolist                  display the configured software repositories
repoquery                 search for packages matching keyword
repository-packages       run commands on top of all packages in given repository
search                    search package details for the given string
shell                     run an interactive YUM shell
swap                      run an interactive YUM mod for remove and install one spec
updateinfo                display advisories about packages
upgrade                   upgrade a package or packages on your system
upgrade-minimal           upgrade, but only 'newest' package match which fixes a problem that affects your system

List of Plugin Commands:

builddep                  Install build dependencies for package or spec file
changelog                 Show changelog data of packages
config-manager            manage yum configuration options and repositories
copr                      Interact with Copr repositories.
debug-dump                dump information about installed rpm packages to file
debug-restore             restore packages recorded in debug-dump file
debuginfo-install         install debuginfo packages
download                  Download package to current directory
groups-manager            create and edit groups metadata file
needs-restarting          determine updated binaries that need restarting
playground                Interact with Playground repository.
repoclosure               Display a list of unresolved dependencies for repositories
repodiff                  List differences between two sets of repositories
repograph                 Output a full package dependency graph in dot format
repomanage                Manage a directory of rpm packages
reposync                  download all packages from remote repo

General YUM options:
  -c [config file], --config [config file]
                        config file location
  -q, --quiet           quiet operation
  -v, --verbose         verbose operation
  --version             show YUM version and exit
  --installroot [path]  set install root
  --nodocs              do not install documentations
  --noplugins           disable all plugins
  --enableplugin [plugin]
                        enable plugins by name
  --disableplugin [plugin]
                        disable plugins by name
  --releasever RELEASEVER
                        override the value of $releasever in config and repo files
  --setopt SETOPTS      set arbitrary config and repo options
  --skip-broken         resolve depsolve problems by skipping packages
  -h, --help, --help-cmd
                        show command help
  --allowerasing        allow erasing of installed packages to resolve dependencies
  -b, --best            try the best available package versions in transactions.
  --nobest              do not limit the transaction to the best candidate
  -C, --cacheonly       run entirely from system cache, don't update cache
  -R [minutes], --randomwait [minutes]
                        maximum command wait time
  -d [debug level], --debuglevel [debug level]
                        debugging output level
  --debugsolver         dumps detailed solving results into files
  --showduplicates      show duplicates, in repos, in list/search commands
  -e ERRORLEVEL, --errorlevel ERRORLEVEL
                        error output level
  --obsoletes           enables yum's obsoletes processing logic for upgrade or display capabilities that the package obsoletes for info, list and
                        repoquery
  --rpmverbosity [debug level name]
                        debugging output level for rpm
  -y, --assumeyes       automatically answer yes for all questions
  --assumeno            automatically answer no for all questions
  --enablerepo [repo]   Enable additional repositories. List option. Supports globs, can be specified multiple times.
  --disablerepo [repo]  Disable repositories. List option. Supports globs, can be specified multiple times.
  --repo [repo], --repoid [repo]
                        enable just specific repositories by an id or a glob, can be specified multiple times
  --enable              enable repos with config-manager command (automatically saves)
  --disable             disable repos with config-manager command (automatically saves)
  -x [package], --exclude [package], --excludepkgs [package]
                        exclude packages by name or glob
  --disableexcludes [repo], --disableexcludepkgs [repo]
                        disable excludepkgs
  --repofrompath [repo,path]
                        label and path to an additional repository to use (same path as in a baseurl), can be specified multiple times.
  --noautoremove        disable removal of dependencies that are no longer used
  --nogpgcheck          disable gpg signature checking (if RPM policy allows)
  --color COLOR         control whether color is used
  --refresh             set metadata as expired before running the command
  -4                    resolve to IPv4 addresses only
  -6                    resolve to IPv6 addresses only
  --destdir DESTDIR, --downloaddir DESTDIR
                        set directory to copy packages to
  --downloadonly        only download packages
  --comment COMMENT     add a comment to transaction
  --bugfix              Include bugfix relevant packages, in updates
  --enhancement         Include enhancement relevant packages, in updates
  --newpackage          Include newpackage relevant packages, in updates
  --security            Include security relevant packages, in updates
  --advisory ADVISORY, --advisories ADVISORY
                        Include packages needed to fix the given advisory, in updates
  --bz BUGZILLA, --bzs BUGZILLA
                        Include packages needed to fix the given BZ, in updates
  --cve CVES, --cves CVES
                        Include packages needed to fix the given CVE, in updates
  --sec-severity {Critical,Important,Moderate,Low}, --secseverity {Critical,Important,Moderate,Low}
                        Include security relevant packages matching the severity, in updates
  --forcearch ARCH      Force the use of an architecture



# To run steam on linux(ubuntu) use this - might include them also directly in the image dockerfile

apt-get install software-properties-common

add-apt-repository multiverse

apt update

apt install steam

###################################################### LINUX ######################################################

###################################################################################################################

###################################################### DOCKER #####################################################

# HOW TO pull a docker image and login to that container as root 
 C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker pull --help

 Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

 Pull an image or a repository from a registry

 Options:
  -a, --all-tags                Download all tagged images in the repository
      --disable-content-trust   Skip image verification (default true)
      --platform string         Set platform if server is multi-platform
                                capable
  -q, --quiet                   Suppress verbose output

C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker pull oraclelinux:9
9: Pulling from library/oraclelinux
07773263ab23: Pull complete
Digest: sha256:01c7e8c446a9a8a9565f4a98505aa14f09c1b6bce0935a5b606b18c4d1545a63
Status: Downloaded newer image for oraclelinux:9
docker.io/library/oraclelinux:9

docker build -t oraclelinux:9 .



C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker ps
CONTAINER ID   IMAGE           COMMAND       CREATED              STATUS              PORTS     NAMES
f657e6f247f6   oraclelinux:9   "/bin/bash"   About a minute ago   Up About a minute             angry_goodall

C:\Projects - Tool Validation - Setup - Etc\Project - Jenkins>docker exec -it angry_goodall /bin/bash
[root@f657e6f247f6 /]# pwd
/
[root@f657e6f247f6 /]# whoami
root
[root@f657e6f247f6 /]# :)
bash: syntax error near unexpected token `)'
[root@f657e6f247f6 /]# ls -a
.   .dockerenv  bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
..  afs         boot  etc  lib   media  opt  root  sbin  sys  usr


-----------------------------------------------------------------------------------
# HOW TO login to linux docker image 
 SSH into a Container
 Use docker ps to get the name of the existing container.
 Use the command docker exec -it <container name> /bin/bash to get a bash shell in the container.
 Generically, use docker exec -it <container name> <command> to execute whatever command you specify in the container.
 
# Example of dockerfile
# Image Version 0.7
# Base image
FROM oraclelinux:9

# Information
LABEL maintainer="Nicolae Codleanu <nicolae.codleanu@cerner.com>"

# Trying to find a way to start the container with systemctl also up and running
# COPY start.sh start.sh
# CMD ["/bin/bash", "start.sh"]
CMD ["COPY", "start.sh start.sh"]
CMD ["/sbin/init", "start.sh"]

# Run available updates 
# CMD [“echo”,”Get available updates”] 
RUN yum update
RUN yum upgrade 
# CMD [“echo”,”Updates processed”] 

# To build, run and connect to the container with something like: 
# docker build –t orel9jk:0.5 .
#   --> must include the . at the end which specifies the directory(in this case current dir)
#       where the Dockerfile is located.
# docker exec -it <container id> sh
# Run the container from this image using a command like this: 
# docker run -it -d --privileged=true image_id /sbin/init -p 8080:80
# docker run -i -t -d orel9jk:0.2

# Install Jenkins Section

# First install pre-requisites - Java
# CMD [“echo”,”Jenkins Section - Installing pre-requisites”]
RUN yum install -q -y java-11-openjdk

# Retrieving jenkins repo
# CMD [“echo”,”Jenkins Section - Installing wget”]
RUN yum install  -q -y wget
#CMD [“echo”,”Jenkins Section - Retrieving jenkins repo”] 
RUN wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat/jenkins.repo
# CMD [“echo”,”Jenkins Section - Importing jenkins repo key”]     
RUN rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
# CMD [“echo”,”Jenkins Section - Completed instalation of pre-requisites”] 

# Install Jenkins
# CMD [“echo”,”Jenkins Section - Installing Jenkins”] 
RUN yum install  -q -y jenkins 
# CMD [“echo”,”Jenkins Section - Completed instalation of Jenkins”] 

# Starting Jenkins - this part doesn't work yet
#CMD [“echo”,”Jenkins Section - Starting Jenkins”]
#RUN systemctl daemon-reload 
#RUN systemctl enable jenkins
#RUN systemctl start jenkins
#CMD [“echo”,”Jenkins Section - Jenkins Running”] 

# COMMAND INFO: useradd 
# EXAMPLE: useradd -m <username>




 
###################################################### DOCKER ######################################################
