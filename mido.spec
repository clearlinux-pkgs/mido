#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mido
Version  : 1.2.7
Release  : 6
URL      : https://pypi.debian.net/mido/mido-1.2.7.tar.gz
Source0  : https://pypi.debian.net/mido/mido-1.2.7.tar.gz
Summary  : MIDI Objects for Python
Group    : Development/Tools
License  : MIT
Requires: mido-bin
Requires: mido-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Mido - MIDI Objects for Python
==============================
Mido is a library for working with MIDI messages and ports. It's
designed to be as straight forward and Pythonic as possible:

%package bin
Summary: bin components for the mido package.
Group: Binaries

%description bin
bin components for the mido package.


%package python
Summary: python components for the mido package.
Group: Default

%description python
python components for the mido package.


%prep
%setup -q -n mido-1.2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496331078
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1496331078
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
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

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
