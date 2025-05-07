%global _gitcommit 2067a01cd652a723e22746683d271b43f8d2ff38
%global _gitdate 20241022

%undefine _debugsource_packages

Name:           lomse
Version:        0.30.0git%{_gitdate}
Release:        1%{?dist}
Summary:        A library to add capabilities to any program for rendering
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            http://www.lenmus.org/en/lomse/intro
Source0:        https://github.com/lenmus/lomse/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  boost-devel fontconfig-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libpng-devel
BuildRequires:  make

%description
Lomse is a project designed to provide software developers with a library to
add capabilities to any program for rendering, editing and playing back music
scores. It is written in C++ and it is free open source and platform
independent. It is based on the experience gained developing the Phonascus
program. Lomse stands for "LenMus Open Music Score Edition Library".

%package devel
Summary:        A library to add capabilities to any program for rendering
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for the package lomse.

%prep
%setup -q -n %{name}-%{_gitcommit}

%build
%cmake -G "Unix Makefiles" -DLOMSE_BUILD_STATIC_LIB=ON \
        -DCMAKE_BUILD_TYPE=Release -DFREETYPE_INCLUDE_DIRS=%{_includedir}/freetype2
%cmake_build

%install
%cmake_install
install -d %{buildroot}%{_datadir}/%{name}
cp -r test-scores %{buildroot}%{_datadir}/%{name}/
if [ ! -d "%{buildroot}%{_libdir}" ]; then
   mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
fi
rm %{buildroot}%{_libdir}/liblomse.so
ln -s liblomse.so.%{version} %{buildroot}%{_libdir}/liblomse.so
install -m755 */lib%{name}.a %{buildroot}%{_libdir}

%{?ldconfig_scriptlets}

%files
%doc *.md
%license LICENSE
%{_datadir}/%{name}
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.a
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Tue May  5 2025 Martin RS - 0.30.0git20241022
- update
* Mon Feb 20 2023 Martin RS - 0.30.0git20221227
- update
* Sat Nov 13 2021 Martin RS - 0.28.0git20211109
- update
* Sat Jun 27 2020 Martin RS - 0.27.0git20200617
- update
* Wed Nov 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20.0
- Rebuilt for Fedora
* Thu Jun 13 2013 joop.boonen@opensuse.org
- Update to version 0.14.0
* Sun Dec 16 2012 joop.boonen@opensuse.org
- Build lomse with fonts etc inside
* Sat Dec 15 2012 joop.boonen@opensuse.org
- Build version 0.12.5
