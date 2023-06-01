#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : libinput
Version  : 1.23.0
Release  : 93
URL      : https://gitlab.freedesktop.org/libinput/libinput/-/archive/1.23.0/libinput-1.23.0.tar.gz
Source0  : https://gitlab.freedesktop.org/libinput/libinput/-/archive/1.23.0/libinput-1.23.0.tar.gz
Summary  : Input device library
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: libinput-bin = %{version}-%{release}
Requires: libinput-config = %{version}-%{release}
Requires: libinput-data = %{version}-%{release}
Requires: libinput-lib = %{version}-%{release}
Requires: libinput-libexec = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}
Requires: libinput-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : graphviz-extras
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(fribidi)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mtdev)
BuildRequires : pypi-pytest
BuildRequires : python3-dev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libinput
========
libinput is a library that provides a full input stack for display servers
and other applications that need to handle input devices provided by the
kernel.

%package bin
Summary: bin components for the libinput package.
Group: Binaries
Requires: libinput-data = %{version}-%{release}
Requires: libinput-libexec = %{version}-%{release}
Requires: libinput-config = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}

%description bin
bin components for the libinput package.


%package config
Summary: config components for the libinput package.
Group: Default

%description config
config components for the libinput package.


%package data
Summary: data components for the libinput package.
Group: Data

%description data
data components for the libinput package.


%package dev
Summary: dev components for the libinput package.
Group: Development
Requires: libinput-lib = %{version}-%{release}
Requires: libinput-bin = %{version}-%{release}
Requires: libinput-data = %{version}-%{release}
Provides: libinput-devel = %{version}-%{release}
Requires: libinput = %{version}-%{release}

%description dev
dev components for the libinput package.


%package lib
Summary: lib components for the libinput package.
Group: Libraries
Requires: libinput-data = %{version}-%{release}
Requires: libinput-libexec = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}

%description lib
lib components for the libinput package.


%package libexec
Summary: libexec components for the libinput package.
Group: Default
Requires: libinput-config = %{version}-%{release}
Requires: libinput-license = %{version}-%{release}

%description libexec
libexec components for the libinput package.


%package license
Summary: license components for the libinput package.
Group: Default

%description license
license components for the libinput package.


%package man
Summary: man components for the libinput package.
Group: Default

%description man
man components for the libinput package.


%prep
%setup -q -n libinput-1.23.0
cd %{_builddir}/libinput-1.23.0
pushd ..
cp -a libinput-1.23.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685639051
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dlibwacom=false \
-Ddocumentation=false \
-Ddebug-gui=false  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dlibwacom=false \
-Ddocumentation=false \
-Ddebug-gui=false  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libinput
cp %{_builddir}/libinput-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libinput/f5a6ed09e0687479426f93fd084dc38c812b966d || :
cp %{_builddir}/libinput-%{version}/doc/api/style/LICENSE %{buildroot}/usr/share/package-licenses/libinput/5a48bb048772f9029b604fbdd869d92fddae1cef || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib/udev/libinput-device-group
/V3/usr/lib/udev/libinput-fuzz-extract
/V3/usr/lib/udev/libinput-fuzz-to-zero
/usr/lib/udev/libinput-device-group
/usr/lib/udev/libinput-fuzz-extract
/usr/lib/udev/libinput-fuzz-to-zero

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/libinput
/usr/bin/libinput

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/80-libinput-device-groups.rules
/usr/lib/udev/rules.d/90-libinput-fuzz-override.rules

%files data
%defattr(-,root,root,-)
/usr/share/libinput/10-generic-keyboard.quirks
/usr/share/libinput/10-generic-mouse.quirks
/usr/share/libinput/10-generic-trackball.quirks
/usr/share/libinput/30-vendor-a4tech.quirks
/usr/share/libinput/30-vendor-aiptek.quirks
/usr/share/libinput/30-vendor-alps.quirks
/usr/share/libinput/30-vendor-contour.quirks
/usr/share/libinput/30-vendor-cypress.quirks
/usr/share/libinput/30-vendor-elantech.quirks
/usr/share/libinput/30-vendor-glorious.quirks
/usr/share/libinput/30-vendor-ibm.quirks
/usr/share/libinput/30-vendor-kensington.quirks
/usr/share/libinput/30-vendor-logitech.quirks
/usr/share/libinput/30-vendor-madcatz.quirks
/usr/share/libinput/30-vendor-microsoft.quirks
/usr/share/libinput/30-vendor-razer.quirks
/usr/share/libinput/30-vendor-synaptics.quirks
/usr/share/libinput/30-vendor-trust.quirks
/usr/share/libinput/30-vendor-vmware.quirks
/usr/share/libinput/30-vendor-wacom.quirks
/usr/share/libinput/50-framework.quirks
/usr/share/libinput/50-system-acer.quirks
/usr/share/libinput/50-system-apple.quirks
/usr/share/libinput/50-system-asus.quirks
/usr/share/libinput/50-system-chicony.quirks
/usr/share/libinput/50-system-chuwi.quirks
/usr/share/libinput/50-system-cyborg.quirks
/usr/share/libinput/50-system-dell.quirks
/usr/share/libinput/50-system-gigabyte.quirks
/usr/share/libinput/50-system-google.quirks
/usr/share/libinput/50-system-gpd.quirks
/usr/share/libinput/50-system-hp.quirks
/usr/share/libinput/50-system-huawei.quirks
/usr/share/libinput/50-system-lenovo.quirks
/usr/share/libinput/50-system-pine64.quirks
/usr/share/libinput/50-system-sony.quirks
/usr/share/libinput/50-system-starlabs.quirks
/usr/share/libinput/50-system-system76.quirks
/usr/share/libinput/50-system-toshiba.quirks
/usr/share/libinput/50-system-vaio.quirks
/usr/share/zsh/site-functions/_libinput

%files dev
%defattr(-,root,root,-)
/usr/include/libinput.h
/usr/lib64/libinput.so
/usr/lib64/pkgconfig/libinput.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libinput.so.10.13.0
/usr/lib64/libinput.so.10
/usr/lib64/libinput.so.10.13.0

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/libinput/libinput-analyze
/V3/usr/libexec/libinput/libinput-debug-events
/V3/usr/libexec/libinput/libinput-debug-tablet
/V3/usr/libexec/libinput/libinput-list-devices
/V3/usr/libexec/libinput/libinput-measure
/V3/usr/libexec/libinput/libinput-quirks
/V3/usr/libexec/libinput/libinput-record
/V3/usr/libexec/libinput/libinput-test
/usr/libexec/libinput/libinput-analyze
/usr/libexec/libinput/libinput-analyze-per-slot-delta
/usr/libexec/libinput/libinput-analyze-recording
/usr/libexec/libinput/libinput-analyze-touch-down-state
/usr/libexec/libinput/libinput-debug-events
/usr/libexec/libinput/libinput-debug-tablet
/usr/libexec/libinput/libinput-list-devices
/usr/libexec/libinput/libinput-list-kernel-devices
/usr/libexec/libinput/libinput-measure
/usr/libexec/libinput/libinput-measure-fuzz
/usr/libexec/libinput/libinput-measure-touch-size
/usr/libexec/libinput/libinput-measure-touchpad-pressure
/usr/libexec/libinput/libinput-measure-touchpad-size
/usr/libexec/libinput/libinput-measure-touchpad-tap
/usr/libexec/libinput/libinput-quirks
/usr/libexec/libinput/libinput-record
/usr/libexec/libinput/libinput-replay
/usr/libexec/libinput/libinput-test

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libinput/5a48bb048772f9029b604fbdd869d92fddae1cef
/usr/share/package-licenses/libinput/f5a6ed09e0687479426f93fd084dc38c812b966d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libinput-analyze-per-slot-delta.1
/usr/share/man/man1/libinput-analyze-recording.1
/usr/share/man/man1/libinput-analyze-touch-down-state.1
/usr/share/man/man1/libinput-analyze.1
/usr/share/man/man1/libinput-debug-events.1
/usr/share/man/man1/libinput-debug-tablet.1
/usr/share/man/man1/libinput-list-devices.1
/usr/share/man/man1/libinput-list-kernel-devices.1
/usr/share/man/man1/libinput-measure-fuzz.1
/usr/share/man/man1/libinput-measure-touch-size.1
/usr/share/man/man1/libinput-measure-touchpad-pressure.1
/usr/share/man/man1/libinput-measure-touchpad-size.1
/usr/share/man/man1/libinput-measure-touchpad-tap.1
/usr/share/man/man1/libinput-measure.1
/usr/share/man/man1/libinput-quirks-list.1
/usr/share/man/man1/libinput-quirks-validate.1
/usr/share/man/man1/libinput-quirks.1
/usr/share/man/man1/libinput-record.1
/usr/share/man/man1/libinput-replay.1
/usr/share/man/man1/libinput-test-suite.1
/usr/share/man/man1/libinput-test.1
/usr/share/man/man1/libinput.1
