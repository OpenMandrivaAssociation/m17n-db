%define version	1.4.0
%define release	%mkrel 1

Name:      m17n-db
Summary:   The m17n database
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   LGPL
URL:       http://www.m17n.org/m17n-lib/index.html
Source0:   http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.bz2
BuildRequires:   glibc-i18ndata gettext-devel

%description
The m17n database; a sub-part of the m17n library.


%package    devel
Summary:    Headers of m17n for development
Group:      Development/C
Requires:   %{name} = %{version}

%description devel
Headers of %{name} for development.


%prep
%setup -q

%build
[[ -f configure ]] || ./bootstrap.sh || :
aclocal
autoconf
automake -a
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/m17n/*

%files devel
%defattr(-,root,root)
%doc COPYING
%{_libdir}/pkgconfig/*
