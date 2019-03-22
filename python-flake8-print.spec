# Created by pyp2rpm-3.3.2
%global pypi_name flake8-print

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        print statement checker plugin for flake8

License:        MIT
URL:            https://github.com/jbkahn/flake8-print
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8) >= 1.5
BuildRequires:  python3dist(flake8) >= 1.5
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
Flake8 print plugin Check for Print statements in python files.This module
provides a plugin for flake8, the Python code checker. Installation You can
install or upgrade flake8-print with these commands:: $ pip install
flake8-print $ pip install --upgrade flake8-print Plugin for Flake8 --When both
flake8 2.4.1 and flake8-print are installed, the plugin is available in
flake8:: $ flake8...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(flake8) >= 1.5
Requires:       python3dist(pycodestyle)
Requires:       python3dist(setuptools)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
Flake8 print plugin Check for Print statements in python files.This module
provides a plugin for flake8, the Python code checker. Installation You can
install or upgrade flake8-print with these commands:: $ pip install
flake8-print $ pip install --upgrade flake8-print Plugin for Flake8 --When both
flake8 2.4.1 and flake8-print are installed, the plugin is available in
flake8:: $ flake8...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/flake8_print.py
%{python3_sitelib}/flake8_print-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 3.1.0-1
- Initial package.