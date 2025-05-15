%{?!python3_pkgversion:%global python3_pkgversion 3}

%global _gitcommit fd8b5bb96fd1

%global _description %{expand:
Editobj3 is an automatic dialog box generator for Python objects.

It supports several backends; currenlty Qt, GTK and HTML are supported.
The HTML backend is based on `W2UI <http://w2ui.com>`_, and can be used
either in local single user mode, or in distributed multiple users mode.
}

%global srcname jibalamy-editobj3
%global pkgname Editobj3

Name:           editobj3
Version:        0.2
Release:        2%{?dist}
Summary:        An automatic dialog box generator for Python objects
License:        LGPLv3+
URL:            https://bitbucket.org/jibalamy/editobj3
Source0:        https://bitbucket.org/jibalamy/editobj3/get/%{_gitcommit}.tar.bz2#/%{srcname}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}


%description
%_description

%package -n python%{python3_pkgversion}-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-%{name}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{_gitcommit}
sed -i setup.py -e "/name\s\+=.*%{pkgname}/s/%{pkgname}/%{name}/"


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%files -n  python%{python3_pkgversion}-%{name}
%license LICENSE.txt
%doc README.rst
# For noarch packages: sitelib
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Jan 06 2025 Martin RS - 0.2
- Initial Fedora
