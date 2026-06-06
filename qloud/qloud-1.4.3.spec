Name:           qloud
Version:        1.4.3
Release:        1%{?dist}
Summary:        tool to measure a loudspeaker frequency response and distortions

License:        GPLv2
URL:            https://github.com/molke-productions/qloud
Source0:        https://github.com/molke-productions/qloud/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(jack) = 1.9.22
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(fftw3)

%description
QLoud is a tool to measure a loudspeaker frequency response and distortions.


%prep
%autosetup -n %{name}-%{version}


%build
%qmake_qt6 PREFIX=%{_prefix}
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
* Fri Jun  5 2026 Martin RS - 1.4.3
- upate
* Wed Feb 22 2023 Martin RS - 1.4.2git20220807
- initial for Fedora
