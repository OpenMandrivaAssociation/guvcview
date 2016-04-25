%define         major                 2
%define         minor                 0

%define         gvaname               gviewaudio
%define         libgvaname            %mklibname %{gvaname} %{major}.%{minor}
%define         develgvaname          %mklibname %{gvaname} -d

%define         gvename               gviewencoder
%define         libgvename            %mklibname %{gvename} %{major}.%{minor}
%define         develgvename          %mklibname %{gvename} -d

%define         gvv4l2name            gviewv4l2core
%define         libgvv4l2name         %mklibname %{gvv4l2name} %{major}.%{minor}
%define         develgvv4l2name       %mklibname %{gvv4l2name} -d

%define         gvrendername          gviewrender
%define         libgvrendername       %mklibname %{gvrendername} %{major}.%{minor}
%define         develgvrendername     %mklibname %{gvrendername} -d
%define		date	20160425

Name:           guvcview
Version:        2.0.3
Release:        1

Summary:        GTK+ UVC Viewer and Capturer
Group:          Video
License:        GPLv3+

URL:            http://guvcview.sourceforge.net/
Source0:        http://sourceforge.net/projects/%{name}/files/source/%{name}-src-%{version}-%{date}.tar.xz
Patch0:		ffmpeg3.patch

BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libdvbv5)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  intltool
BuildRequires:  pkgconfig(libpulse)

%description
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.


%package -n %{libgvaname}
Summary:        Shared library for %{name} audio support
Group:          System/Libraries
Provides:       lib%{gvaname} = %{version}-%{release}


%description -n %{libgvaname}
%{summary}.  

%package -n %{develgvaname}
Summary:        Development files for %{name} audio support
Group:          Development/Other
Requires:       %{libgvaname} = %{version}-%{release}

%description -n %{develgvaname}
%{summary}.
 
%package -n %{libgvename}
Summary:        Shared library for %{name} encoder support
Group:          System/Libraries
Provides:       lib%{gvename} = %{version}-%{release}

%description -n %{libgvename}
%{summary}.  

%package -n %{develgvename}
Summary:        Development files for %{name} encoder support
Group:          Development/Other
Requires:       %{libgvename} = %{version}-%{release}

%description -n %{develgvename}
%{summary}.

%package -n %{libgvv4l2name}
Summary:        Shared library for %{name} video support
Group:          System/Libraries
Provides:       lib%{gvv4l2name} = %{version}-%{release}

%description -n %{libgvv4l2name}
%{summary}.  

%package -n %{develgvv4l2name}
Summary:        Development files for %{name} video support
Group:          Development/Other
Requires:       %{libgvv4l2name} = %{version}-%{release}

%description -n %{develgvv4l2name}
%{summary}.

%package -n %{libgvrendername}
Summary:        Shared library for %{name} rendering support
Group:          System/Libraries
Provides:       lib%{gvrendername} = %{version}-%{release}

%description -n %{libgvrendername}
%{summary}.  

%package -n %{develgvrendername}
Summary:        Development files for %{name} rendering support
Group:          Development/Other
Requires:       %{libgvrendername} = %{version}-%{release}

%description -n %{develgvrendername}
%{summary}.

%prep
%setup -q -n %{name}-src-%{version}-%{date}
%apply_patches

%build
autoreconf -fi
%configure --enable-pulse --disable-debian-menu \
               --disable-silent-rules \
               --disable-static
%make

%install
%makeinstall_std

desktop-file-install \
        --add-category='X-AudioVideoCapture' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}
%find_lang gview_v4l2core


find %{buildroot}%{_libdir} -name *.la -delete

%__mv %{buildroot}%{_datadir}/doc/%{name} _doc
%__rm _doc/INSTALL

%files -f %{name}.lang
%doc _doc/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*.xml

%files -n %{libgvaname}
%{_libdir}/libgviewaudio-*.so.%{major}*

%files -n %{develgvaname}
%{_includedir}/guvcview-2/libgviewaudio/*.h
%{_libdir}/libgviewaudio.so
%{_libdir}/pkgconfig/libgviewaudio.pc

%files -n %{libgvename}
%{_libdir}/libgviewencoder-*.so.%{major}*

%files -n %{develgvename}
%{_includedir}/guvcview-2/libgviewencoder/*.h
%{_libdir}/libgviewencoder.so
%{_libdir}/pkgconfig/libgviewencoder.pc

%files -n %{libgvv4l2name} -f gview_v4l2core.lang
%{_libdir}/libgviewv4l2core-*.so.%{major}*

%files -n %{develgvv4l2name}
%{_includedir}/guvcview-2/libgviewv4l2core/*.h
%{_libdir}/libgviewv4l2core.so
%{_libdir}/pkgconfig/libgviewv4l2core.pc

%files -n %{libgvrendername}
%{_libdir}/libgviewrender-*.so.%{major}*

%files -n %{develgvrendername}
%{_includedir}/guvcview-2/libgviewrender/*.h
%{_libdir}/libgviewrender.so
%{_libdir}/pkgconfig/libgviewrender.pc
