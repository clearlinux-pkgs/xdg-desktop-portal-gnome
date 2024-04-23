#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v10
# autospec commit: 5905be9
#
Name     : xdg-desktop-portal-gnome
Version  : 46.1
Release  : 6
URL      : https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/archive/46.1/xdg-desktop-portal-gnome-46.1.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/archive/46.1/xdg-desktop-portal-gnome-46.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: xdg-desktop-portal-gnome-data = %{version}-%{release}
Requires: xdg-desktop-portal-gnome-libexec = %{version}-%{release}
Requires: xdg-desktop-portal-gnome-license = %{version}-%{release}
Requires: xdg-desktop-portal-gnome-locales = %{version}-%{release}
Requires: xdg-desktop-portal-gnome-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(gnome-desktop-4)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(xdg-desktop-portal)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# xdg-desktop-portal-gnome
A backend implementation for [xdg-desktop-portal](http://github.com/flatpak/xdg-desktop-portal)
that is using GTK and various pieces of GNOME infrastructure, such as the
org.gnome.Shell.Screenshot or org.gnome.SessionManager D-Bus interfaces.

%package data
Summary: data components for the xdg-desktop-portal-gnome package.
Group: Data

%description data
data components for the xdg-desktop-portal-gnome package.


%package libexec
Summary: libexec components for the xdg-desktop-portal-gnome package.
Group: Default
Requires: xdg-desktop-portal-gnome-license = %{version}-%{release}

%description libexec
libexec components for the xdg-desktop-portal-gnome package.


%package license
Summary: license components for the xdg-desktop-portal-gnome package.
Group: Default

%description license
license components for the xdg-desktop-portal-gnome package.


%package locales
Summary: locales components for the xdg-desktop-portal-gnome package.
Group: Default

%description locales
locales components for the xdg-desktop-portal-gnome package.


%package services
Summary: services components for the xdg-desktop-portal-gnome package.
Group: Systemd services
Requires: systemd

%description services
services components for the xdg-desktop-portal-gnome package.


%prep
%setup -q -n xdg-desktop-portal-gnome-46.1
cd %{_builddir}/xdg-desktop-portal-gnome-46.1
pushd ..
cp -a xdg-desktop-portal-gnome-46.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713885065
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-gnome
cp %{_builddir}/xdg-desktop-portal-gnome-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-gnome/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang xdg-desktop-portal-gnome
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/xdg-desktop-portal-gnome.desktop
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.gnome.service
/usr/share/glib-2.0/schemas/xdg-desktop-portal-gnome.gschema.xml
/usr/share/xdg-desktop-portal/portals/gnome.portal

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/xdg-desktop-portal-gnome
/usr/libexec/xdg-desktop-portal-gnome

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdg-desktop-portal-gnome/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/xdg-desktop-portal-gnome.service

%files locales -f xdg-desktop-portal-gnome.lang
%defattr(-,root,root,-)

