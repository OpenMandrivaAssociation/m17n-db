Summary:	The m17n database
Name:		m17n-db
Version:	1.8.0
Release:	2
Group:		System/Internationalization
License:	LGPLv2+
Url:		http://www.m17n.org/m17n-lib/index.html
Source0:	http://savannah.c3sl.ufpr.br//m17n/m17n-db-%version.tar.gz
BuildArch:	noarch
BuildRequires:	glibc-i18ndata
BuildRequires:	gettext-devel

%description
The m17n database; a sub-part of the m17n library.

%package    devel
Summary:	Headers of m17n for development
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Headers of %{name} for development.

%prep
%setup -q

%build
%configure --build=%{_host}
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/m17n

%files devel
%doc AUTHORS README NEWS ChangeLog
%{_datadir}/pkgconfig/*
