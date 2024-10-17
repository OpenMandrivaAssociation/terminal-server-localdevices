Summary:	This enables the local devices on an X terminal
Name:		terminal-server-localdevices
Version:	1.0
Release:	10
License:	GPL
Group:		Networking/Other
URL:		https://www.advx.org

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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-9mdv2010.0
+ Revision: 434335
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-8mdv2009.0
+ Revision: 261486
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-7mdv2009.0
+ Revision: 254389
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-5mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0-5mdv2008.0
+ Revision: 70415
- use %%mkrel


* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdk
- rebuild

* Thu Dec 18 2003 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.0-3mdk
- put back nobody.nogroup as files owner: rpmlint might not like it, 
  but it's the only way to have read/write by root when using root_squash
  nfs, and have it unreadable by other non-root users.
- before making changes in this package, please e-mail me so I can make sure
  the changes are working in an installation with at least 12 X-terminals.
- OK, so I found out why Olivier changed it, ftpcontrib does not like user
  nobody, so I do a Bad Thing (TM), and do a chown in the post script.

* Tue Aug 12 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-2mdk
- fix files owner

* Tue Jul 29 2003 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.0-1mdk
- Take all the work I did for a local non-profit organization and make a
  package so we can implement it at other sites.

