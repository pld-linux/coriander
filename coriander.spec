%define		_rc	rc4
Summary:	Coriander - GUI for IEEE1394, IIDC/DCAM compliant digital cameras
Summary(pl.UTF-8):	Coriander - GUI dla kamer cyfrowych zgodnych z IEEE1394 i IIDC/DCAM
Name:		coriander
Version:	2.0.0
Release:	0.%{_rc}.1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/coriander/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	b62c7e9b240a9c7f8bb9b66cce8310b6
URL:		http://sourceforge.net/projects/coriander/
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	ffmpeg-devel >= 0.4.9
BuildRequires:	ftplib-devel
BuildRequires:	libdc1394-devel >= 2.0.0-0.rc5.1
BuildRequires:	libgnomeui-devel
BuildRequires:	libraw1394-devel >= 1.2.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coriander is a full-featured GUI for IEEE1394, IIDC-compliant (aka
DCAM) digital cameras. It includes camera control, video display,
saving, FTP and V4L export.

%description -l pl.UTF-8
Coriander to w pełni funkcjonalny interfejs graficzny do kamer
cyfrowych zgodnych z IEEE1394 i IIDC (DCAM). Obsługuje sterowanie
kamerą, wyświetlanie obrazu, zapis i eksport FTP oraz V4L.

%prep
%setup -q -n %{name}-%{version}-%{_rc}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no translations yet
#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/coriander
%{_pixmapsdir}/%{name}
