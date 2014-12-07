%global git 60eff04
%global uuid panel-osd@berend.de.schouwer.gmail.com
%global github ozonos-atom-notify
%global checkout git%{git}

Name:           atom-notify
Version:        1
Release:        0.2.%(date +%Y%m%d).%{checkout}%{?dist}
Summary:        An extension to show the notification messages below the top-panel instead of above the message tray

Group:          User Interface/Desktops
License:        GPLv3+
URL:            https://github.com/ozonos/atom-notify
Source0:        https://github.com/ozonos/atom-notify/tarball/master/%{github}-%{git}.tar.gz
BuildArch:      noarch

BuildRequires:  autoconf >= 2.53, automake >= 1.9, glib2-devel, gnome-common >= 3.6.0, intltool >= 0.25
Requires:       gnome-shell >= 3.6.0

Obsoletes: gnome-shell-extension-top-notification
Provides: gnome-shell-extension-top-notification

%description
Atom Notify is an extension to show the notification
messages below the top-panel instead of above the message tray

%prep
%setup -q -n %{github}-%{git}

%build
NOCONFIGURE=1 ./autogen.sh
%configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%postun
if [ $1 -eq 0 ] ; then
        %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS COPYING README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.panel-osd.gschema.xml
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Sun Dec 7 2014 Joshua Fogg <joshua.h.fogg@gmail.com>
- Forked gnome-shell-extension-panel-osd for Ozon OS.

