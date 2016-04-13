Summary:	Duplicate file finder
Name:		duff
Version:	0.5.2
Release:	2
License:	BSD
Group:		Applications
Source0:	https://github.com/elmindreda/duff/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e4688d2724e1990d7d36ecb89f114f9e
Patch0:		gettext.patch
Patch1:		shared-sha.patch
URL:		http://duff.dreda.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sha-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duff is a Unix command-line utility for quickly finding duplicates in
a given set of files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

install -d build-aux

%build
%{__gettextize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/duff.1*
