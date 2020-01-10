%global fontname lohit-kannada
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.5.3
Release:        2%{?dist}
Summary:        Free Kannada font

Group:          User Interface/X
License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Kannada truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-kannada.conf


%build
make %{?_smp_mflags}

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README ChangeLog.old


%changelog
* Fri Apr 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-2
- Resolved #950521

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-4
- Spec file cleanup

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolves bug #825104

* Wed Mar 28 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Thu Feb 09 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.0-3
- Resolved bug 748710

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Mon Jun 06 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.6-2
- Resolved bug 705348

* Thu May 12 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.6-1
- upstream new release 2.4.6

* Fri Apr 28 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-8
- fixes bug 694705

* Wed Apr 13 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-7
- fixes bug 692362

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- resolved bug 673414, rupee sign

* Mon Oct 18 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- fixed zwj problem of bug 576105
- will work when, zwj processing will be fixed in pango

* Mon Oct 18 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- fixed bug 576105

* Fri Apr 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- fixed bug 578032

* Tue Mar 23 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release
- fix bugs 576105, 559462 

* Thu Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- fixed bug 548686, license field

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
