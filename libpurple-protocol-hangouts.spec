%define		snap	20190127
%define		commit	cccf2f62d439
Summary:	Hangouts plugin for libpurple
Name:		libpurple-protocol-hangouts
Version:	0.0.1
Release:	0.%{snap}.1
License:	GPL v3
Group:		Applications/Communications
Source0:	https://bitbucket.org/EionRobb/purple-hangouts/get/%{commit}.tar.bz2?/purple-hangouts-%{commit}.tar.bz2
# Source0-md5:	1628dcefdb100bd37111b54573dd1f8e
URL:		https://bitbucket.org/EionRobb/purple-hangouts/
BuildRequires:	glib2-devel
BuildRequires:	json-glib-devel
BuildRequires:	libpurple-devel
BuildRequires:	pkgconfig
BuildRequires:	protobuf-c
BuildRequires:	protobuf-c-devel
BuildRequires:	zlib-devel
Provides:	libpurple-protocol
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hangouts plugin for libpurple.

%prep
%setup -qn EionRobb-purple-hangouts-%{commit}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/purple-2/libhangouts.so
%{_pixmapsdir}/pidgin/protocols/*/hangouts.png
