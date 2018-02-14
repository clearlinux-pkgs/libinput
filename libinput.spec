#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : libinput
Version  : 1.10.0
Release  : 22
URL      : http://www.freedesktop.org/software/libinput/libinput-1.10.0.tar.xz
Source0  : http://www.freedesktop.org/software/libinput/libinput-1.10.0.tar.xz
Source99 : http://www.freedesktop.org/software/libinput/libinput-1.10.0.tar.xz.sig
Summary  : Input device library
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: libinput-bin
Requires: libinput-config
Requires: libinput-lib
Requires: libinput-doc
BuildRequires : cairo-dev32
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdk-pixbuf-dev32
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pango-dev32
BuildRequires : pkgconfig(32atk)
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gtk+-3.0)
BuildRequires : pkgconfig(32libevdev)
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32mtdev)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mtdev)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : valgrind

%description
libinput
========
libinput is a library that handles input devices for display servers and other
applications that need to directly deal with input devices.

%package bin
Summary: bin components for the libinput package.
Group: Binaries
Requires: libinput-config

%description bin
bin components for the libinput package.


%package config
Summary: config components for the libinput package.
Group: Default

%description config
config components for the libinput package.


%package dev
Summary: dev components for the libinput package.
Group: Development
Requires: libinput-lib
Requires: libinput-bin
Provides: libinput-devel

%description dev
dev components for the libinput package.


%package dev32
Summary: dev32 components for the libinput package.
Group: Default
Requires: libinput-lib32
Requires: libinput-bin
Requires: libinput-dev

%description dev32
dev32 components for the libinput package.


%package doc
Summary: doc components for the libinput package.
Group: Documentation

%description doc
doc components for the libinput package.


%package lib
Summary: lib components for the libinput package.
Group: Libraries

%description lib
lib components for the libinput package.


%package lib32
Summary: lib32 components for the libinput package.
Group: Default

%description lib32
lib32 components for the libinput package.


%prep
%setup -q -n libinput-1.10.0
pushd ..
cp -a libinput-1.10.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518615943
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dlibwacom=false builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
CFLAGS="$CFLAGS -m32" CXXFLAGS="$CXXFLAGS -m32" LDFLAGS="$LDFLAGS -m32 " PKG_CONFIG_PATH="/usr/lib32/pkgconfig" meson --libdir=/usr/lib32 --prefix /usr --buildtype=plain -Dlibwacom=false builddir
ninja -v -C builddir
popd

%install
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
popd
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib/udev/hwdb.d/90-libinput-model-quirks.hwdb
/usr/lib/udev/libinput-device-group
/usr/lib/udev/libinput-model-quirks

%files bin
%defattr(-,root,root,-)
/usr/bin/libinput
/usr/bin/libinput-debug-events
/usr/bin/libinput-list-devices
/usr/libexec/libinput/libinput-debug-events
/usr/libexec/libinput/libinput-debug-gui
/usr/libexec/libinput/libinput-list-devices
/usr/libexec/libinput/libinput-measure
/usr/libexec/libinput/libinput-measure-touch-size
/usr/libexec/libinput/libinput-measure-touchpad-pressure
/usr/libexec/libinput/libinput-measure-touchpad-tap
/usr/libexec/libinput/libinput-measure-trackpoint-range

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/80-libinput-device-groups.rules
/usr/lib/udev/rules.d/90-libinput-model-quirks.rules

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libinput.so
/usr/lib64/pkgconfig/libinput.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libinput.so
/usr/lib32/pkgconfig/libinput.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libinput.so.10
/usr/lib64/libinput.so.10.13.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libinput.so.10
/usr/lib32/libinput.so.10.13.0
