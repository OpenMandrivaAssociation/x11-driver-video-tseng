Name: x11-driver-video-tseng
Version: 1.2.4
Release: %mkrel 2
Summary: X.org driver for Tseng Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tseng-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-tseng is the X.org driver for Tseng Cards.

%prep
%setup -q -n xf86-video-tseng-%{version}

%build
%configure2_5x --x-includes=%{_includedir}\
               --x-libraries=%{_libdir}
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
