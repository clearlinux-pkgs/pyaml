#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyaml
Version  : 21.10.1
Release  : 47
URL      : https://files.pythonhosted.org/packages/b6/f0/dbb524509ce28f5cfd4e1d9e3ef955f51186cfd1b8297f6e158778c4a8ef/pyaml-21.10.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b6/f0/dbb524509ce28f5cfd4e1d9e3ef955f51186cfd1b8297f6e158778c4a8ef/pyaml-21.10.1.tar.gz
Summary  : PyYAML-based module to produce pretty and readable YAML-serialized data
Group    : Development/Tools
License  : WTFPL
Requires: pyaml-license = %{version}-%{release}
Requires: pyaml-python = %{version}-%{release}
Requires: pyaml-python3 = %{version}-%{release}
Requires: PyYAML
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3

%description
pretty-yaml (or pyaml)
======================
PyYAML-based python module to produce pretty and readable YAML-serialized data.

%package license
Summary: license components for the pyaml package.
Group: Default

%description license
license components for the pyaml package.


%package python
Summary: python components for the pyaml package.
Group: Default
Requires: pyaml-python3 = %{version}-%{release}

%description python
python components for the pyaml package.


%package python3
Summary: python3 components for the pyaml package.
Group: Default
Requires: python3-core
Provides: pypi(pyaml)
Requires: pypi(pyyaml)

%description python3
python3 components for the pyaml package.


%prep
%setup -q -n pyaml-21.10.1
cd %{_builddir}/pyaml-21.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636413317
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
mkdir -p %{buildroot}/usr/share/package-licenses/pyaml
cp %{_builddir}/pyaml-21.10.1/COPYING %{buildroot}/usr/share/package-licenses/pyaml/4263532d38628c3adc51dbce2419bc2b3cab4795
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyaml/4263532d38628c3adc51dbce2419bc2b3cab4795

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
