%define		snap	20210629
%define		commit	55b9f01d040b240b794700f44d9c21a6cb51251e
Summary:	Hangouts plugin for libpurple
Name:		libpurple-protocol-hangouts
Version:	0.0.1
Release:	0.%{snap}.1
License:	GPL v3
Group:		Applications/Communications
Source0:	https://github.com/EionRobb/purple-hangouts/archive/%{commit}/purple-hangouts-%{commit}.tar.gz
# Source0-md5:	0cf8cb337edfd81e1584e3b59083f3f4
URL:		https://github.com/EionRobb/purple-hangouts
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
%setup -qn purple-hangouts-%{commit}

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
