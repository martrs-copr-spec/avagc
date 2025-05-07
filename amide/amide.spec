%global _gitcommit c02babd6b660a8d83c7f90eab69bbff34253923d
%global _gitdate 20231008

Name: 		amide
Version: 	1.0.6git%{_gitdate}
Release: 	3%{?dist}
Summary: 	Program for viewing and analyzing medical image data sets
License: 	GPLv2+
Group: 		Applications/Engineering
URL: 		https://amide.sourceforge.net
Source0: 	https://github.com/ferdymercury/amide/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Packager: 	Andy Loening <loening at alum dot mit dot edu>

Requires:	xmedcon >= 0.10.0
Requires:	gsl
Requires:	volpack
Requires:	ffmpeg-libs >= 0.4.9
Requires:	dcmtk >= 3.6.0
Requires:       gtk2 >= 2.16
Requires:	gnome-vfs2
Requires:	libgnomecanvas

BuildRequires:  autoconf automake libtool gcc-c++ glibc-devel intltool desktop-file-utils
BuildRequires:  xmedcon-devel
BuildRequires:  volpack-devel 
BuildRequires:  libxml2-devel 
BuildRequires:  gnome-doc-utils
BuildRequires:  libgnomecanvas-devel 
BuildRequires:  ffmpeg-devel >= 0.4.9
BuildRequires:  gsl-devel
BuildRequires:  dcmtk-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel >= 2.10
BuildRequires:  gtk-doc
BuildRequires:	gnome-vfs2-devel
BuildRequires:	openh264-devel

%description 

AMIDE is a tool for viewing and analyzing medical image data sets.
It's capabilities include the simultaneous handling of multiple data
sets imported from a variety of file formats, image fusion, 3D region
of interest drawing and analysis, volume rendering, and rigid body
alignments.


%prep
%setup -q -n %{name}-%{_gitcommit}

%build
intltoolize; libtoolize; gtkdocize; gnome-doc-prepare
autoreconf -i
%configure \
	   --enable-libecat=no \
	   --enable-vistaio=no \
	   --enable-amide-debug=no \
	   --disable-scrollkeeper
%__make

%install
#rm -rf $RPM_BUILD_ROOT
%make_install # DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor gnome --delete-original                   \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications                         \
  --add-category X-Red-Hat-Extra                                        \
  $RPM_BUILD_ROOT%{_datadir}/applications/*


%clean
rm -rf $RPM_BUILD_ROOT

%post
update-desktop-database %{_datadir}/applications

%postun
update-desktop-database %{_datadir}/applications

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README todo
%{_bindir}/*
%{_datadir}/pixmaps
%{_datadir}/gnome
%{_datadir}/omf
%{_datadir}/applications
%{_datadir}/locale
%{_mandir}/*



%changelog
* Wed May  7 2025 Martin RS - 1.0.6git20231008                                  
- update                                                                        
* Sat Sep  3 2022 Martin RS - 1.0.6git20220709                                  
- update
* Sun Mar 23 2021 Martin RS - 1.0.6
- update for Fedora
* Thu Feb 24 2011 Andy Loening <loening at alum dot mit dot edu>
- cutout gtk-doc building and scrollkeeper
* Sun Dec 16 2007 Andy Loening <loening at alum dot mit dot edu>
- small tweak for new gnome-doc help files
* Tue Nov 05 2002 Andy Loening <loening at alum dot mit dot edu>
- get it to work with scrollkeeper
* Sun Dec 19 2000 Andy Loening <loening at alum dot mit dot edu>
- wrote this fool thing
