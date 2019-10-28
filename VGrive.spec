Name:           VGrive
Version:        1.0.10
Release:        1
Summary:        Google Drive client with automatic synchronization for Linux
License:        GPLv3
Group:          Graphical desktop/GNOME
URL:            https://appcenter.elementary.io/com.github.bcedu.vgrive/
Source0:        https://github.com/bcedu/VGrive/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
VGrive is a client (back-end and front-end) for Google Drive made in Vala. 
Automatically detects changes in local and remote files and syncs them.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
