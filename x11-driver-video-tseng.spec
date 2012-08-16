%define git 0

Name: x11-driver-video-tseng
Version: 1.2.5
%if 0%git
Release: 0.%git.1
Source0: xf86-video-tseng-%git.tar.xz
%else
Release: 1
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tseng-%{version}.tar.bz2
%endif
Summary: X.org driver for Tseng Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-tseng is the X.org driver for Tseng Cards.

%prep
%if 0%git
%setup -qn xf86-video-tseng
%else
%setup -qn xf86-video-tseng-%{version}
%endif
[ -e autogen.sh ] && ./autogen.sh --help

%build
%configure2_5x \
	--x-includes=%{_includedir} \
   	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/tseng_drv.so
%{_mandir}/man4/tseng.*



%changelog
* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.5-0.20120327.1
+ Revision: 787454
- Update to current git to fix compatibility with x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.2.4-7
+ Revision: 748476
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.4-6
+ Revision: 703647
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.2.4-5
+ Revision: 683591
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-4
+ Revision: 671183
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.4-3mdv2011.0
+ Revision: 595732
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.2.4-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Thu Jul 22 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.2.4-1mdv2011.0
+ Revision: 557062
- New version: 1.2.4

* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 1.2.3-1mdv2010.0
+ Revision: 432152
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.2-1mdv2010.0
+ Revision: 391936
- update to new version 1.2.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.1-1mdv2009.1
+ Revision: 317854
- New version 1.2.1

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.0-3mdv2009.1
+ Revision: 308270
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.0-2mdv2009.0
+ Revision: 265953
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194132
- Update to version 1.2.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-3mdv2008.1
+ Revision: 166152
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.1-2mdv2008.1
+ Revision: 156625
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-1mdv2008.1
+ Revision: 154789
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to version 1.1.1 and add local mandriva patches.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2008.0
+ Revision: 75819
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Mon Jun 05 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-06-05 21:11:32 (36659)
- new upstream release

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

