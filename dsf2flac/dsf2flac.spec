%global _gitcommit 39d43901ce27d0cc53b5a4eb277a65082e9906f0
%global _gitdate 20250131

Name:           dsf2flac
Version:        0.1git%{_gitdate}
Release:        1%{?dist}
Summary:        Code for converting DSF to FLAC files

License:        GPLv2
URL:            https://github.com/hank/dsf2flac/
Source0:        https://github.com/hank/dsf2flac/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf automake libtool
BuildRequires:  gcc-c++ glibc-devel
BuildRequires:  boost-devel
BuildRequires:  id3lib-devel taglib-devel flac-devel

%description
dsf2flac is a file conversion tool for translating dsf or dff dsd audio files
into flac pcm audio files.


%prep
%autosetup -n %{name}-%{_gitcommit}
sed -i m4/ax_boost_timer.m4 \
  -e 's|boost/timer\.h|boost/timer/timer.h|' \
  -e 's/boost::timer /boost::timer::cpu_timer /'


%build
./autogen.sh --no-configure
%configure
%make_build


%install
%make_install


%files
%doc README.md doc/*
%{_bindir}/%{name}


%changelog
* Wed May  7 2025 Martin RS - 0.1git20250131
- update
* Tue Nov 16 2021 Martin RS - 0.1git20210731
- update
* Thu Apr 25 2019 Martin RS - 0.1git20180101
- new for Fedora
