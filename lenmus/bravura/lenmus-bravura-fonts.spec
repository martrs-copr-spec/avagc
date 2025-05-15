Version: 1.392
Release: 2%{?dist}
URL:     https://github.com/lenmus/bravura/
%global  _disable_source_fetch 0

%global foundry           lenmus
%global fontlicense       SIL-OFL-1.1

%global fontlicenses      LICENSE.txt
%global fontdocs          README.md
%global fontfamily        bravura
%global fontsummary       OpenType music font by Daniel Spreadbury at Steinberg

%global fonts             src/*.otf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
Bravura is an OpenType music font designed by Daniel Spreadbury at
Steinberg.

It is the reference font for Standard Music Font Layout (SMuFL)
project, which provides a standard way of mapping the thousands of musical
symbols required by conventional music notation into the Private Use Area
in Unicode’s Basic Multilingual Plane for a single (format-independent)
font.
}

Source0:  https://github.com/lenmus/bravura/archive/refs/tags/%{version}-0.tar.gz
Source10: 60-%{fontpkgname}.conf

%fontpkg

%prep
%setup -n %{fontfamily}-%{version}-0

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Sat May  3 2025 Martin RS - 1.392
- update to build in copr
* Mon Feb 20 2023 Martin RS - 1.392
- update version
* Sat Nov 13 2021 Martin RS - 1.18
- update packaging using fonts-rpm-templates
* Sat Jun 27 2020 Martin RS - 1.18
- initial for Fedora
