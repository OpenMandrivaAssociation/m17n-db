Name:      m17n-db
Summary:   The m17n database
Version:   1.5.2
Release:   %mkrel 1
Group:     System/Internationalization
License:   LGPLv2+
URL:       http://www.m17n.org/m17n-lib/index.html
Source0:   http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
BuildRequires:   glibc-i18ndata gettext-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

mkdir -p %buildroot%_libdir
mv %buildroot%_datadir/pkgconfig %buildroot%_libdir/pkgconfig
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README NEWS ChangeLog
%{_bindir}/*
%{_datadir}/m17n

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
