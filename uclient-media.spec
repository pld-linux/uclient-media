Summary:	Media files for uclient
Summary(pl):	Pliki medialne dla uclient
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

%description -l pl
UCLIENT to izometryczny klient WorldForge z przedmiotami i kaflami
bazującymi na perspektywie iso 2:1.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

tar xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/forge
