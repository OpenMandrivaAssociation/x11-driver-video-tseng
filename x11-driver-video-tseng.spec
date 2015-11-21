%define _disable_ld_no_undefined 1

Summary:	X.org driver for Tseng Cards
Name:		x11-driver-video-tseng
Version:	1.2.5
Release:	15
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tseng-%{version}.tar.bz2
Patch0:		remove_mibstore_h.store

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-server)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-tseng is the X.org driver for Tseng Cards.

%prep
%setup -qn xf86-video-tseng-%{version}
%apply_patches

%build
%configure \
	--x-includes=%{_includedir} \
   	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/tseng_drv.so
%{_mandir}/man4/tseng.*

