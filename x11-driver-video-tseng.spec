%define git 20120327

Name: x11-driver-video-tseng
Version: 1.2.5
%if 0%git
Release: 0.%git.1
Source: xf86-video-tseng-%git.tar.xz
%else
Release: 1
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tseng-%{version}.tar.bz2
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
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/tseng_drv.so
%{_mandir}/man4/tseng.*

