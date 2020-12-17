#
# TODO:
#/usr/bin/nepomukpimindexerutility
#/usr/share/apps/akonadi_nepomuk_feeder/akonadi_nepomuk_feeder.notifyrc
#/usr/share/apps/nepomukpimindexerutility/nepomukpimindexerutility.rc
#
%define		_state	stable
%define		qtver	4.8.1

%define		orgname	kdepim-runtime

Summary:	Runtime Personal Information Management (PIM) for KDE
Summary(pl.UTF-8):	Zarządca informacji osobistej (PIM) dla KDE
Name:		kde4-kdepim-runtime
Version:	4.14.10
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/Attic/applications/15.04.3/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	7dd2063acf9b6920920d0118f5576db6
Patch0:		no-tests.patch
Patch100:	%{name}-branch.diff
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtXmlPatterns-devel >= %{qtver}
BuildRequires:	akonadi-devel >= 1.2.80
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libaccounts-qt4-devel >= 1.11
BuildRequires:	libkfbapi-devel >= 1.0
BuildRequires:	libkgapi-devel >= 1.9.81
BuildRequires:	libkolab-devel >= 0.5.2
BuildRequires:	libkolabxml-devel >= 1.0
BuildRequires:	libsignon-qt4-devel >= 8.56
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	qjson-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel >= 2.3.70
BuildRequires:	strigi-devel >= 0.7.0
BuildRequires:	zlib-devel
BuildConflicts:	indexlib
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Provides:	kde4-kdepim-akonadi
Obsoletes:	kde4-kdepim-akonadi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl.UTF-8
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE).

%package kontact
Summary:	Kontact Personal Information Management
Summary(pl.UTF-8):	Kontact Personal Information Management
Group:		X11/Applications
Requires:	pinentry-qt4
Provides:	kde4-kontact
Obsoletes:	kde4-kontact

%description kontact
Kontact Personal Information Management.

%description kontact -l pl.UTF-8
Kontact Personal Information Management.

%package devel
Summary:	Development files for KDE pim-runtime
Summary(pl.UTF-8):	Pliki nagłówkowe do KDE pim
Summary(ru.UTF-8):	Файлы разработки для kdepim
Summary(uk.UTF-8):	Файли розробки для kdepim
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
This package contains header files needed if you wish to build
applications based on kdepimruntime.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe potrzebne do budowy aplikacji
bazujących na kdepim-runtime.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1
#%patch100 -p1

%build
export CXXFLAGS="%{rpmcxxflags} -Wno-narrowing"
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/ldconfig
%postun	-p	/sbin/ldconfig

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/accountwizard
%attr(755,root,root) %{_bindir}/akonadi_davgroupware_resource
%attr(755,root,root) %{_bindir}/akonadi_facebook_resource
%attr(755,root,root) %{_bindir}/akonadi_googlecalendar_resource
%attr(755,root,root) %{_bindir}/akonadi_googlecontacts_resource
%attr(755,root,root) %{_bindir}/akonadi_invitations_agent
%attr(755,root,root) %{_bindir}/akonadi_kdeaccounts_resource
%attr(755,root,root) %{_bindir}/akonadi_kolab_resource
%attr(755,root,root) %{_bindir}/akonadi_migration_agent
%attr(755,root,root) %{_bindir}/akonadi_mixedmaildir_resource
%attr(755,root,root) %{_bindir}/akonadi_newmailnotifier_agent
%attr(755,root,root) %{_bindir}/akonadi_openxchange_resource
%attr(755,root,root) %{_bindir}/kjotsmigrator
%attr(755,root,root) %{_bindir}/akonadi_kabc_resource
%attr(755,root,root) %{_bindir}/akonadi_kcal_resource
%attr(755,root,root) %{_bindir}/akonadi_localbookmarks_resource
%attr(755,root,root) %{_bindir}/akonadi_maildispatcher_agent
%attr(755,root,root) %{_bindir}/akonadi_mailtransport_dummy_resource
%attr(755,root,root) %{_bindir}/akonadi_nntp_resource
%attr(755,root,root) %{_bindir}/akonadi_vcarddir_resource
%attr(755,root,root) %{_bindir}/akonadi_pop3_resource
%attr(755,root,root) %{_bindir}/akonaditray
#%attr(755,root,root) %{_bindir}/akonadi2xml
%attr(755,root,root) %{_bindir}/akonadi_birthdays_resource
%attr(755,root,root) %{_bindir}/akonadi_icaldir_resource
%attr(755,root,root) %{_bindir}/akonadi_imap_resource
%attr(755,root,root) %{_bindir}/akonadi_kolabproxy_resource
%attr(755,root,root) %{_bindir}/gidmigrator
%attr(755,root,root) %{_bindir}/kaddressbookmigrator
%attr(755,root,root) %{_bindir}/kmail-migrator
%attr(755,root,root) %{_bindir}/knotes-migrator
%attr(755,root,root) %{_bindir}/kres-migrator
#%attr(755,root,root) %ghost %{_libdir}/libakonadi-xml.so.?
#%attr(755,root,root) %{_libdir}/libakonadi-xml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdepim-copy.so.?
%attr(755,root,root) %{_libdir}/libkdepim-copy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmaildir.so.?
%attr(755,root,root) %{_libdir}/libmaildir.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libakonadi-filestore.so.?
%attr(755,root,root) %{_libdir}/libakonadi-filestore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmindexreader.so.?
%attr(755,root,root) %{_libdir}/libfolderarchivesettings.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfolderarchivesettings.so.4
%attr(755,root,root) %{_libdir}/libkmindexreader.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_addressee.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_contactgroup.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_mail.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_microblog.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_kcal.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_kcalcore.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_bookmark.so
%attr(755,root,root) %{_libdir}/kde4/accountwizard_plugin.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_akonotes_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_contacts_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_ical_resource.so
#%attr(755,root,root) %{_libdir}/kde4/akonadi_knut_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_maildir_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_mbox_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_notes_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_vcard_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_kalarm_dir_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_kalarm_resource.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_kalarm.so
%attr(755,root,root) %{_libdir}/kde4/akonadi_serializer_socialnotification.so
%attr(755,root,root) %{_libdir}/kde4/kabc_akonadi.so
%attr(755,root,root) %{_libdir}/kde4/kio_akonadi.so
%attr(755,root,root) %{_libdir}/kde4/kcm_akonadi_resources.so
%attr(755,root,root) %{_libdir}/kde4/kcm_akonadi.so
%attr(755,root,root) %{_libdir}/kde4/kcm_akonadi_server.so
%attr(755,root,root) %{_libdir}/kde4/kcal_akonadi.so
%{_datadir}/autostart/kaddressbookmigrator.desktop
%dir %{_datadir}/apps/akonadi
#%{_datadir}/apps/akonadi/akonadi-xml.xsd
#%dir %{_datadir}/apps/akonadi_knut_resource
#%{_datadir}/apps/akonadi_knut_resource/knut-template.xml
%dir %{_datadir}/apps/akonadi/plugins
%dir %{_datadir}/apps/akonadi/plugins/serializer
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_mail.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_kcal.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_kcalcore.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_bookmark.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_microblog.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_kalarm.desktop
%{_datadir}/apps/akonadi/plugins/serializer/akonadi_serializer_socialnotification.desktop
%{_datadir}/apps/kconf_update/newmailnotifier.upd
%dir %{_datadir}/akonadi
%dir %{_datadir}/akonadi/agents
%{_datadir}/akonadi/agents/akonotesresource.desktop
%{_datadir}/akonadi/agents/birthdaysresource.desktop
%{_datadir}/akonadi/agents/contactsresource.desktop
%{_datadir}/akonadi/agents/davgroupwareresource.desktop
%{_datadir}/akonadi/agents/facebookresource.desktop
%{_datadir}/akonadi/agents/googlecalendarresource.desktop
%{_datadir}/akonadi/agents/googlecontactsresource.desktop
%{_datadir}/akonadi/agents/icaldirresource.desktop
%{_datadir}/akonadi/agents/icalresource.desktop
%{_datadir}/akonadi/agents/imapresource.desktop
%{_datadir}/akonadi/agents/invitationsagent.desktop
%{_datadir}/akonadi/agents/kabcresource.desktop
%{_datadir}/akonadi/agents/kcalresource.desktop
%{_datadir}/akonadi/agents/kdeaccountsresource.desktop
#%{_datadir}/akonadi/agents/knutresource.desktop
%{_datadir}/akonadi/agents/kolabproxyresource.desktop
%{_datadir}/akonadi/agents/kolabresource.desktop
%{_datadir}/akonadi/agents/localbookmarksresource.desktop
%{_datadir}/akonadi/agents/maildirresource.desktop
%{_datadir}/akonadi/agents/maildispatcheragent.desktop
%{_datadir}/akonadi/agents/mboxresource.desktop
%{_datadir}/akonadi/agents/migrationagent.desktop
%{_datadir}/akonadi/agents/mixedmaildirresource.desktop
%{_datadir}/akonadi/agents/mtdummyresource.desktop
%{_datadir}/akonadi/agents/newmailnotifieragent.desktop
%{_datadir}/akonadi/agents/nntpresource.desktop
%{_datadir}/akonadi/agents/notesresource.desktop
%{_datadir}/akonadi/agents/openxchangeresource.desktop
%{_datadir}/akonadi/agents/pop3resource.desktop
%{_datadir}/akonadi/agents/vcarddirresource.desktop
%{_datadir}/akonadi/agents/vcardresource.desktop
%{_datadir}/akonadi/agents/akonadinepomukfeederagent.desktop
%{_datadir}/akonadi/agents/kalarmdirresource.desktop
%{_datadir}/akonadi/agents/kalarmresource.desktop
%{_desktopdir}/kde4/accountwizard.desktop
%{_datadir}/apps/akonadi/accountwizard
%{_datadir}/apps/akonadi/firstrun
%{_datadir}/apps/akonadi_maildispatcher_agent
%{_datadir}/apps/akonadi_facebook_resource
%{_datadir}/apps/akonadi_kolabproxy_resource
%{_datadir}/apps/akonadi_newmailnotifier_agent
%{_datadir}/config/accountwizard.knsrc
%{_datadir}/config/kmail-migratorrc
%{_datadir}/config/kres-migratorrc
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Maildir.Settings.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.MixedMaildir.Settings.xml
%{_datadir}/kde4/services/akonadi
%{_datadir}/kde4/services/akonadi.protocol
%{_datadir}/kde4/services/kcm_akonadi.desktop
%{_datadir}/kde4/services/kcm_akonadi_resources.desktop
%{_datadir}/kde4/services/kcm_akonadi_server.desktop
%{_datadir}/kde4/services/kresources/kabc/akonadi.desktop
%{_datadir}/kde4/services/kresources/kcal/akonadi.desktop
%{_datadir}/kde4/servicetypes/davgroupwareprovider.desktop
%{_datadir}/mime/packages/accountwizard-mime.xml
%{_datadir}/mime/packages/kdepim-mime.xml
%{_datadir}/mime/packages/x-vnd.akonadi.socialnotification.xml
%{_libdir}/kde4/imports/org/kde/*.qml
%{_libdir}/kde4/imports/org/kde/*.png
%{_libdir}/kde4/imports/org/kde/qmldir
%attr(755,root,root) %{_libdir}/kde4/imports/org/kde/libkdeqmlplugin.so
%dir %{_libdir}/kde4/imports/org/kde/akonadi
%{_libdir}/kde4/imports/org/kde/akonadi/*.qml
%{_libdir}/kde4/imports/org/kde/akonadi/*.png
%{_libdir}/kde4/imports/org/kde/akonadi/qmldir
%{_desktopdir}/kde4/akonaditray.desktop
%{_iconsdir}/*/*/apps/akonaditray.png
%{_iconsdir}/*/*/apps/akonaditray.svgz
%{_iconsdir}/*/*/apps/facebookresource.png
%{_iconsdir}/*/*/apps/kolab.png
%{_iconsdir}/*/*/apps/ox.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libakonadi-filestore.so
%attr(755,root,root) %{_libdir}/libfolderarchivesettings.so
#%attr(755,root,root) %{_libdir}/libakonadi-xml.so
%attr(755,root,root) %{_libdir}/libkdepim-copy.so
%attr(755,root,root) %{_libdir}/libkmindexreader.so
%attr(755,root,root) %{_libdir}/libmaildir.so
