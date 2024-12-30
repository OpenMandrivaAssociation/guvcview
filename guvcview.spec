%define _disable_ld_no_undefined 1

%define	major	2
%define	minor	0

%define	gvanam	e		gviewaudio
%define	libgvaname		%mklibname %{gvaname}
%define	develgvaname		%mklibname %{gvaname} -d
%define	oldlibgvaname		%mklibname %{gvaname} %{major}.%{minor}

%define	gvename			gviewencoder
%define	libgvename		%mklibname %{gvename}
%define	develgvename		%mklibname %{gvename} -d
%define	oldlibgvename		%mklibname %{gvename} %{major}.%{minor}

%define	gvv4l2name		gviewv4l2core
%define	libgvv4l2name		%mklibname %{gvv4l2name}
%define	develgvv4l2name		%mklibname %{gvv4l2name} -d
%define	oldlibgvv4l2name	%mklibname %{gvv4l2name} %{major}.%{minor}

%define	gvrendername		gviewrender
%define	libgvrendername		%mklibname %{gvrendername}
%define	develgvrendername	%mklibname %{gvrendername} -d
%define	oldlibgvrendername	%mklibname %{gvrendername} %{major}.%{minor}

Name:		guvcview
Version:	2.2.1
Release:	1
Summary:	GTK+ UVC Viewer and Capturer
Group:		Video
License:	GPLv3+
URL:		https://guvcview.sourceforge.net/
Source0:	https://downloads.sourceforge.net/guvcview/%{name}-src-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires: 	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libdvbv5)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	intltool
BuildRequires:	autoconf-archive
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(libusb-1.0)

%description
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%files -f %{name}.lang
#doc _doc/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
#{_datadir}/pixmaps/%{name}
%{_datadir}/applications/%{name}.desktop
#{_datadir}/metainfo/%{name}.appdata.xml

#--------------------------------------------------------------------

%package -n %{libgvaname}
Summary:	Shared library for %{name} audio support
Group:	 	System/Libraries
Provides:	lib%{gvaname} = %{version}-%{release}
# Intentionally unversioned, because libname should not contain version number
Obsoletes:	%{oldlibgvaname}

%description -n %{libgvaname}
%{summary}.

%files -n %{libgvaname}
%{_libdir}/libgviewaudio-*.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develgvaname}
Summary:	Development files for %{name} audio support
Group:	 	Development/Other
Requires:	%{libgvaname} = %{version}-%{release}

%description -n %{develgvaname}
%{summary}.
 
%files -n %{develgvaname}
%{_includedir}/guvcview-2/libgviewaudio/*.h
%{_libdir}/libgviewaudio.so
%{_libdir}/pkgconfig/libgviewaudio.pc

#--------------------------------------------------------------------

%package -n %{libgvename}
Summary:	Shared library for %{name} encoder support
Group:	 	System/Libraries
Provides:	lib%{gvename} = %{version}-%{release}
# Intentionally unversioned, because libname should not contain version number
Obsoletes:	%{oldlibgvename}

%description -n %{libgvename}
%{summary}.

%files -n %{libgvename}
%{_libdir}/libgviewencoder-*.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develgvename}
Summary:	Development files for %{name} encoder support
Group:	 	Development/Other
Requires:	%{libgvename} = %{version}-%{release}

%description -n %{develgvename}
%{summary}.

%files -n %{develgvename}
%{_includedir}/guvcview-2/libgviewencoder/*.h
%{_libdir}/libgviewencoder.so
%{_libdir}/pkgconfig/libgviewencoder.pc

#--------------------------------------------------------------------

%package -n %{libgvv4l2name}
Summary:	Shared library for %{name} video support
Group:	 	System/Libraries
Provides:	lib%{gvv4l2name} = %{version}-%{release}
# Intentionally unversioned, because libname should not contain version number
Obsoletes:	%{oldlibgvv4l2name}

%description -n %{libgvv4l2name}
%{summary}.

%files -n %{libgvv4l2name} -f gview_v4l2core.lang
%{_libdir}/libgviewv4l2core-*.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develgvv4l2name}
Summary:	Development files for %{name} video support
Group:		Development/Other
Requires:	%{libgvv4l2name} = %{version}-%{release}

%description -n %{develgvv4l2name}
%{summary}.

%files -n %{develgvv4l2name}
%{_includedir}/guvcview-2/libgviewv4l2core/*.h
%{_libdir}/libgviewv4l2core.so
%{_libdir}/pkgconfig/libgviewv4l2core.pc

#--------------------------------------------------------------------

%package -n %{libgvrendername}
Summary:	Shared library for %{name} rendering support
Group:	 	System/Libraries
Provides:	lib%{gvrendername} = %{version}-%{release}
# Intentionally unversioned, because libname should not contain version number
Obsoletes:	%{oldlibgvrendername}

%description -n %{libgvrendername}
%{summary}.

%files -n %{libgvrendername}
%{_libdir}/libgviewrender-*.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develgvrendername}
Summary:	Development files for %{name} rendering support
Group:		Development/Other
Requires:	%{libgvrendername} = %{version}-%{release}

%description -n %{develgvrendername}
%{summary}.

%files -n %{develgvrendername}
%{_includedir}/guvcview-2/libgviewrender/*.h
%{_libdir}/libgviewrender.so
%{_libdir}/pkgconfig/libgviewrender.pc

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-src-%{version}

%build
%cmake \
	-DUSE_SDL2=ON
%make_build

%install
%make_install -C build

%find_lang %{name}
%find_lang gview_v4l2core

#find %{buildroot}%{_libdir} -name *.la -delete

#mv %{buildroot}%{_datadir}/doc/%{name} _doc
#rm _doc/INSTALL
#rm %{buildroot}%{_datadir}/doc/%{name}/INSTALL

