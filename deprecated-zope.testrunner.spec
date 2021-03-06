#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-zope.testrunner
Version  : 4.8.1
Release  : 31
URL      : https://pypi.debian.net/zope.testrunner/zope.testrunner-4.8.1.tar.gz
Source0  : https://pypi.debian.net/zope.testrunner/zope.testrunner-4.8.1.tar.gz
Summary  : Zope testrunner script.
Group    : Development/Tools
License  : ZPL-2.1
Requires: deprecated-zope.testrunner-bin = %{version}-%{release}
Requires: deprecated-zope.testrunner-license = %{version}-%{release}
Requires: deprecated-zope.testrunner-python = %{version}-%{release}
Requires: setuptools
Requires: six
Requires: zope.exceptions
Requires: zope.interface
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
***************
zope.testrunner
***************
.. image:: https://img.shields.io/pypi/v/zope.testrunner.svg
:target: https://pypi.python.org/pypi/zope.testrunner/
:alt: Latest release

%package bin
Summary: bin components for the deprecated-zope.testrunner package.
Group: Binaries
Requires: deprecated-zope.testrunner-license = %{version}-%{release}

%description bin
bin components for the deprecated-zope.testrunner package.


%package legacypython
Summary: legacypython components for the deprecated-zope.testrunner package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-zope.testrunner package.


%package license
Summary: license components for the deprecated-zope.testrunner package.
Group: Default

%description license
license components for the deprecated-zope.testrunner package.


%package python
Summary: python components for the deprecated-zope.testrunner package.
Group: Default

%description python
python components for the deprecated-zope.testrunner package.


%prep
%setup -q -n zope.testrunner-4.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554339641
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-zope.testrunner
cp LICENSE.rst %{buildroot}/usr/share/package-licenses/deprecated-zope.testrunner/LICENSE.rst
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/zope-testrunner

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-zope.testrunner/LICENSE.rst

%files python
%defattr(-,root,root,-)
