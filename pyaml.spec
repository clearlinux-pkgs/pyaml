#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyaml
Version  : 15.8.2
Release  : 8
URL      : https://pypi.python.org/packages/source/p/pyaml/pyaml-15.8.2.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyaml/pyaml-15.8.2.tar.gz
Summary  : PyYAML-based module to produce pretty and readable YAML-serialized data
Group    : Development/Tools
License  : WTFPL
Requires: pyaml-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
pretty-yaml (or pyaml)
======================
PyYAML-based python module to produce pretty and readable YAML-serialized data.

%package python
Summary: python components for the pyaml package.
Group: Default

%description python
python components for the pyaml package.


%prep
%setup -q -n pyaml-15.8.2

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
