Name:      m17n-db
Summary:   The m17n database
Version:   1.6.2
Release:   %mkrel 3
Group:     System/Internationalization
License:   LGPLv2+
URL:       http://www.m17n.org/m17n-lib/index.html
Source0:   http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
BuildRequires:   glibc-i18ndata gettext-devel
BuildArch: noarch
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
%setup -q -n %{name}-%{version}

%build
%configure2_5x --build=%{_host}
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

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
%{_datadir}/pkgconfig/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-2mdv2011.0
+ Revision: 666351
- mass rebuild

* Mon Oct 04 2010 Funda Wang <fwang@mandriva.org> 1.6.2-1mdv2011.0
+ Revision: 582857
- 1.6.2 final

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 1.6.2-0.RC.1mdv2011.0
+ Revision: 580637
- new verson 1.6.2 RC

* Tue Apr 27 2010 Funda Wang <fwang@mandriva.org> 1.6.1-1mdv2010.1
+ Revision: 539484
- New version 1.6.1

* Tue Mar 30 2010 Funda Wang <fwang@mandriva.org> 1.6.0-1mdv2010.1
+ Revision: 529676
- update to new version 1.6.0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.5-2mdv2010.1
+ Revision: 523235
- rebuilt for 2010.1

* Wed Jul 29 2009 Funda Wang <fwang@mandriva.org> 1.5.5-1mdv2010.0
+ Revision: 402888
- new version 1.5.5

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 1.5.4-1mdv2009.1
+ Revision: 351214
- New version 1.5.4

* Tue Oct 21 2008 Funda Wang <fwang@mandriva.org> 1.5.3-1mdv2009.1
+ Revision: 295988
- New version 1.5.3

* Tue Jul 08 2008 Funda Wang <fwang@mandriva.org> 1.5.2-1mdv2009.0
+ Revision: 232833
- New version 1.5.2

* Tue Jul 08 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-3mdv2009.0
+ Revision: 232802
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix no-buildroot-tag

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 1.5.1-1mdv2008.1
+ Revision: 163362
- update to new version 1.5.1

* Fri Dec 28 2007 Funda Wang <fwang@mandriva.org> 1.5.0-1mdv2008.1
+ Revision: 138761
- New version 1.5.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 21 2007 Funda Wang <fwang@mandriva.org> 1.4.0-1mdv2008.0
+ Revision: 54221
- New version


* Tue Jan 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.3.4-1mdv2007.0
+ Revision: 106763
- add buildrequires on gettext-devel for `AM_GNU_GETTEXT
- new release
- latest snapshot (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)
- Import m17n-db

* Fri Aug 04 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.3.3-3.20060803.1mdv2007.0
- fix build
- latest snapshot (UTUMI Hirosi <utuhiro78@yahoo.co.jp>): better Thai support
  (http://sourceforge.net/mailarchive/forum.php?thread_id=26116958&forum_id=43684)

* Mon Jun 26 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.3-2.20060625.1mdv2007.0
- latest snapshot

* Sat Feb 25 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.3-1mdk
- new release

* Thu Jan 19 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.1-1mdk
- new release

* Fri Dec 23 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.3.0-1mdk
- new release

* Wed Nov 16 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-4.20051116.1mdk
- latest snapshot
- remove patches for vi-vni.mim (merged upstream)

* Wed Sep 14 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.2.0-3.20050809.2mdk
- source 1, patch 0: add new vi-vni.mim input method for vietnamese (Yukiko
  Bando)

* Wed Aug 10 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-3.20050809.1mdk
- latest snapshot

* Tue Apr 26 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-2.20050425.1mdk
- latest snapshot
- spec cleanup
- remove find_lang (it doesn't have po files)

* Tue Dec 28 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.2.0-1mdk
- new release

* Fri Nov 26 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.1.0-4.cvs20041126.1mdk
- latest snapshot

* Wed Aug 18 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1.0-1mdk
- new release
- only run bootstrap if needed

* Thu Jul 15 2004 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 1.0.2-2.cvs20040714.1mdk
- cvs 20040714

* Fri May 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.2-1mdk
- initial package (based on UTUMI Hirosi <utuhiro78@yahoo.co.jp> 's work)

