%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname Songwrite3

Name:           songwrite3
Version:        0.2
Release:        2%{?dist}
Summary:        Tablature editor with Python 3, Qt 5, EditObj 3, and Timidity
License:        GPLv3+
URL:            http://www.lesfleursdunormal.fr/static/informatique/songwrite/index_en.html
Source0:        https://files.pythonhosted.org/packages/05/29/5268b960e135d79a7400d3007e3c16c33a604ae936f3d298e9e9e2968478/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-editobj3
BuildRequires:  python%{python3_pkgversion}-qt5-base
Requires:  timidity++ evince tetex-latex

%{?python_enable_dependency_generator}


%description
Songwrite 3 is a music score and songbook editor. This software is
especially designed for musicians who do not master solfege like
the author Jean-Baptiste LAMY!) and to Linuxian musicians.
Songwrite 3 can edit staffs, but also tablatures (for guitar, bass,
banjo, lyre, diatonic accordion,...) and flute fingerings (for tin
whistle, recorder,...); it also manages lyrics. Songwrite 3 can play
and print the partitions.


%{?python_provide:%python_provide python3-%{name}}


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i setup.py -e "/name\s\+=.*%{srcname}/s/%{srcname}/%{name}/"
sed -i PKG-INFO -e "/Name:\s\+%{srcname}/s/%{srcname}/%{name}/"
sed -i %{name} -e '1s/\s\+-O//'


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%files
%license AUTHORS LICENSE.txt
%doc CHANGES README.rst
%{_bindir}/%{name}
# For noarch packages: sitelib
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon Jan 06 2025 Martin RS - 0.2
- Initial Fedora
