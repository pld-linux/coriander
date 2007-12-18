#
%define		_rc	rc4
Summary:	coriander
Summary(pl.UTF-8):	coriander
Name:		coriander
Version:	2.0.0
Release:	0.%{_rc}.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/coriander/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	b62c7e9b240a9c7f8bb9b66cce8310b6
URL:		http://sourceforge.net/projects/coriander/
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	libdc1394-devel >= 2.0.0-0.rc5.1
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package devel
Summary:	coriander header files
Summary(pl.UTF-8):	Pliki nagłówkowe coriandera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdc1394-devel

%description devel
coriander header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe coriandera.

%prep
%setup -q -n %{name}-%{version}-%{_rc}

%build
%{__libtoolize}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
#%attr(755,root,root) %{_bindir}/dc1394_reset_bus
#%attr(755,root,root) %{_bindir}/dc1394_vloopback
#%attr(755,root,root) %{_libdir}/libdc1394.so.20.0.0

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libdc1394.so
#%{_libdir}/libdc1394.la
#%{_includedir}/dc1394
#%{_pkgconfigdir}/libdc1394.pc
