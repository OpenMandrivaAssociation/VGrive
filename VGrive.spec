Name:           VGrive
Version:        1.0.10
Release:        1
Summary:        Google Drive client with automatic synchronization for Linux
License:        GPLv3
Group:          Graphical desktop/GNOME
URL:            https://appcenter.elementary.io/com.github.bcedu.vgrive/
Source0:        https://github.com/bcedu/VGrive/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  vala

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
