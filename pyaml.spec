#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyaml
Version  : 20.4.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/f1/cc/01712c4fa0e5b6f9f90d01d5adc46c9ad14bb6284406d13cde3ed7392082/pyaml-20.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f1/cc/01712c4fa0e5b6f9f90d01d5adc46c9ad14bb6284406d13cde3ed7392082/pyaml-20.4.0.tar.gz
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
======================
        
        PyYAML-based python module to produce pretty and readable YAML-serialized data.
        
        This module is for serialization only, see `ruamel.yaml`_ module for literate
        YAML parsing (keeping track of comments, spacing, line/column numbers of values, etc).

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
%setup -q -n pyaml-20.4.0
cd %{_builddir}/pyaml-20.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627686870
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
cp %{_builddir}/pyaml-20.4.0/COPYING %{buildroot}/usr/share/package-licenses/pyaml/4263532d38628c3adc51dbce2419bc2b3cab4795
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
