#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyaml
Version  : 17.12.1
Release  : 28
URL      : https://pypi.debian.net/pyaml/pyaml-17.12.1.tar.gz
Source0  : https://pypi.debian.net/pyaml/pyaml-17.12.1.tar.gz
Summary  : PyYAML-based module to produce pretty and readable YAML-serialized data
Group    : Development/Tools
License  : WTFPL
Requires: pyaml-python3
Requires: pyaml-license
Requires: pyaml-python
Requires: PyYAML
BuildRequires : PyYAML
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: pyaml-python3

%description python
python components for the pyaml package.


%package python3
Summary: python3 components for the pyaml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyaml package.


%prep
%setup -q -n pyaml-17.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530383095
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pyaml
cp COPYING %{buildroot}/usr/share/doc/pyaml/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pyaml/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
