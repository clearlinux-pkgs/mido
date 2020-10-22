#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mido
Version  : 1.2.9
Release  : 39
URL      : https://files.pythonhosted.org/packages/47/a8/f05e3e6491568de9e03506a869a6039e2892d8350809203bd9abcf4b17a8/mido-1.2.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/47/a8/f05e3e6491568de9e03506a869a6039e2892d8350809203bd9abcf4b17a8/mido-1.2.9.tar.gz
Summary  : MIDI Objects for Python
Group    : Development/Tools
License  : MIT
Requires: mido-bin = %{version}-%{release}
Requires: mido-license = %{version}-%{release}
Requires: mido-python = %{version}-%{release}
Requires: mido-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
==============================

%package bin
Summary: bin components for the mido package.
Group: Binaries
Requires: mido-license = %{version}-%{release}

%description bin
bin components for the mido package.


%package license
Summary: license components for the mido package.
Group: Default

%description license
license components for the mido package.


%package python
Summary: python components for the mido package.
Group: Default
Requires: mido-python3 = %{version}-%{release}

%description python
python components for the mido package.


%package python3
Summary: python3 components for the mido package.
Group: Default
Requires: python3-core
Provides: pypi(mido)

%description python3
python3 components for the mido package.


%prep
%setup -q -n mido-1.2.9
cd %{_builddir}/mido-1.2.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603395552
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mido
cp %{_builddir}/mido-1.2.9/LICENSE %{buildroot}/usr/share/package-licenses/mido/f249aa8ed0a0afb411524a251fdc63adeb390612
cp %{_builddir}/mido-1.2.9/docs/license.rst %{buildroot}/usr/share/package-licenses/mido/f243d53f50ec9a04ef1bdf42262d8e9c6481e5ee
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mido-connect
/usr/bin/mido-play
/usr/bin/mido-ports
/usr/bin/mido-serve

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mido/f243d53f50ec9a04ef1bdf42262d8e9c6481e5ee
/usr/share/package-licenses/mido/f249aa8ed0a0afb411524a251fdc63adeb390612

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
