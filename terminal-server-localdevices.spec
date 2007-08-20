Summary:	This enables the local devices on an X terminal.
Name:		terminal-server-localdevices
Version:	1.0
Release:	%mkrel 4
License:	GPL
Group:		Networking/Other
URL:		http://www.advx.org

Source0:	xterminals.tar.bz2
BuildRoot:	%_tmppath/%name-%version-root
Requires:	terminal-server, clusternfs, etherboot

%description
This package enables the local floppy, cdrom and soundcard on an X terminal.
It runs Samba, sshd and artsd on the terminal, and uses a clever Xstartup
script so that KDM automatically assigns ressources to the loggued user.
As an added feature, it can also auto-create temporary users: if someone
logs as a special user, it will create a new user, and delete it when they
log off, making it perfect for public-access computers. Finally, it also
enables users to run local applications (cd player, scanner) using
"runlocal <command>".

You will need the terminal-server and clusternfs packages to use these
functions.

For installation instructions read the README file in /home/xterminals.

%prep
%setup -q -n xterminals

%install
mkdir -p %{buildroot}/home/xterminals
mkdir -p %{buildroot}/etc/rc.d
cp -a *.d*  %{buildroot}/etc/rc.d
cp -a README bin contrib etc keys users %{buildroot}/home/xterminals

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%dir /home/xterminals
/home/xterminals/bin
/home/xterminals/contrib
/home/xterminals/keys
/home/xterminals/users
/home/xterminals/README
/home/xterminals/etc
%config(noreplace) /etc/rc.d/*

%post
chown nobody:nogroup /home/xterminals/etc/ -R

