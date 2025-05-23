%global _gitcommit cc250ca4ce9a90d8dddb0fc359c5a80609cdafcb
%global _gitdate 20250429

%undefine _debugsource_packages

Name:           lenmus
Version:        6.0.1git%{_gitdate}
Release:        1%{?dist}
Summary:        A free program for learning music
License:        GPL-3.0
Group:          Productivity/Multimedia/Sound/Midi
URL:            http://www.lenmus.org/en/noticias
Source0:        https://github.com/lenmus/lenmus/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  fluidsynth-devel lenmus-bravura-fonts
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  lomse-devel
BuildRequires:  make
BuildRequires:  portmidi-devel
BuildRequires:  sqlite-devel
BuildRequires:  unittest-cpp-devel
%if 0%{fedora} <= 38
BuildRequires:  wxGTK3-devel
%else
BuildRequires:  wxGTK-devel
%endif
BuildRequires:  zlib-devel
BuildRequires:  fluid-soundfont-gm
Requires:       lomse
Requires:       timidity++
Requires:       lenmus-bravura-fonts

%description
LenMus is a free program for learning music. It allows you to focus on
specific skills and exercises, on both theory and aural training.
The different activities can be customized to meet your needs.
It includes an score editor.

%prep
%autosetup -n %{name}-%{_gitcommit}
sed -i -e 's|-Wall|-Wall -fPIC -fpermissive|' -e '272s|^#set|set|' -e 's|wx-config|wx-config-3.0|' CMakeLists.txt
sed -i CMakeLists.txt -e 's|fonts/truetype|fonts/lenmus-bravura-fonts|'

%build
%cmake -DPortTime_LIBRARY=%{_libdir}/libportmidi.so
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS *.md NEWS README THANKS
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/%{name}*

%changelog
* Tue May  5 2025 Martin RS - 6.0.1git20250429
- update
* Fri Sep 30 2022 Martin RS - 6.0.1
- update
* Sat Nov 13 2021 Martin RS - 5.6.3git
- update
* Sun Aug 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 5.6.2
- Rebuilt for Fedora
* Sun Dec 23 2012 joop.boonen@opensuse.org
- Don't start rctimidity automaticaly as audio playback won't work anymore
* Wed Dec 19 2012 joop.boonen@opensuse.org
- Used the lenmus provided desktop and png files
* Sun Dec 16 2012 joop.boonen@opensuse.org
- Build LenMus 5.3
- Created wrapper script and desktop file
- Added wx and make scripts
* Wed Nov 28 2012 joop.boonen@opensuse.org
- Build LenMus 5.2
