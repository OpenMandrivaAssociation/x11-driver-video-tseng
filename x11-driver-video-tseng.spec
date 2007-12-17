Name: x11-driver-video-tseng
Version: 1.1.1
Release: %mkrel 1
Summary: The X.org driver for Tseng Cards
Group: Development/X11
URL: http://xorg.freedesktop.org

########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-tseng  xorg/drivers/xf86-video-tseng
# cd xorg/drivers/xf86-video/tseng
# git-archive --format=tar --prefix=xf86-video-tseng-1.1.1/ master | bzip2 -9 > xf86-video-tseng-1.1.1.tar.bz2
########################################################################
Source0: xf86-video-tseng-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Tseng Cards

%prep
%setup -q -n xf86-video-tseng-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/tseng_drv.la
%{_libdir}/xorg/modules/drivers/tseng_drv.so
%{_mandir}/man4/tseng.*
