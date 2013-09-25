#define debug_package   %{nil}
#define distsuffix mrb

Name:           guvcview
Version:        1.7.1
Release:        1
Summary:        GTK+ UVC Viewer and Capturer
Group:          Video
License:        GPLv3+
URL:            http://guvcview.sourceforge.net/
Source0:        http://sourceforge.net/projects/guvcview/files/source/%{name}-src-%{version}.tar.gz

BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  gettext
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  intltool

%description
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.


%prep
%setup -q -n %{name}-src-%{version}
find src -type f -exec chmod u=rw,go=r {} \;


%build
CPPFLAGS=-I/usr/include/ffmpeg
export CPPFLAGS
%configure --enable-pulse --disable-debian-menu
%make


%install
%makeinstall_std

desktop-file-install \
        --add-category='X-AudioVideoCapture' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

mv %{buildroot}%{_datadir}/doc/%{name} _doc
rm _doc/INSTALL

%files -f %{name}.lang
%doc _doc/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/%{name}.desktop

