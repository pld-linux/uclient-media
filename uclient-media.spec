Summary:	Media files for uclient
Summary(pl):	Pliki medialne dla uclient
Name:		uclient-media
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
#Source0:	ftp://ftp.un.pl/pub/worldforge/media/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source-md5:	a11978398dd01953bf4019c5465dfe57
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UCLIENT is an isometric WorldForge client with items and tiles based
on a 2:1 iso perspective.

%description -l pl
UCLIENT to izometryczny klient WorldForge z przedmiotami i kaflami
bazuj±cymi na perspektywie iso 2:1.

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
