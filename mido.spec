#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mido
Version  : 1.2.9
Release  : 31
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
Mido - MIDI Objects for Python
==============================
.. image:: https://travis-ci.org/olemb/mido.svg?branch=master
:target: https://travis-ci.org/olemb/mido

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

%description python3
python3 components for the mido package.


%prep
%setup -q -n mido-1.2.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554322486
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mido
cp LICENSE %{buildroot}/usr/share/package-licenses/mido/LICENSE
cp docs/license.rst %{buildroot}/usr/share/package-licenses/mido/docs_license.rst
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
/usr/share/package-licenses/mido/LICENSE
/usr/share/package-licenses/mido/docs_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
