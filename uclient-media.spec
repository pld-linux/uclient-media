Summary:	Media files for uclient
Name:		uclient-media
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UCLIENT is an isometric WorldForge client with items and tiles based
on a 2:1 iso perspective.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share

cd $RPM_BUILD_ROOT/usr/share
tar zxvf %{SOURCE0} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/usr/share/forge
