%global _gitcommit fba65f1f145064a6c5181451232b8adb3c4b5ecb
%global _gitdate 20220807

Name:           qloud
Version:        1.4.2git%{_gitdate}
Release:        1%{?dist}
Summary:        tool to measure a loudspeaker frequency response and distortions

License:        GPLv2
URL:            https://github.com/molke-productions/qloud
Source0:        https://github.com/molke-productions/qloud/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(jack) == 1.9.22
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(fftw3)

%description
QLoud is a tool to measure a loudspeaker frequency response and distortions.


%prep
%autosetup -n %{name}-%{_gitcommit}


%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Feb 22 2023 Martin RS - 1.4.2git20220807
- initial for Fedora
