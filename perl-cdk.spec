%include	/usr/lib/rpm/macros.perl
Summary:	Perl extensions for CDK
Summary(pl):	Rozszerzenie Perl dla CDK
Name:		perl-cdk
Version:	20010107
Release:	4
License:	distributable 
Group:		Development/Languages/Perl
Source0:	ftp://dickey.his.com/cdk/cdk-perl-%{version}.tgz
Patch0:		%{name}-bugfix.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	cdk-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Perl5 extension to the Cdk library written by Mike Glover.
All the copyright notices from the Cdk C distribution also apply to
the extension.

%description -l pl
To jest rozszerzenie Perla do biblioteki Cdk. Wszystkie copyrighty z
dystrybucji Cdk dotycz± tak¿e tego rozszerzenia.

%prep
%setup -q -n cdk-perl-%{version}
%patch0 -p1

%build
perl -pi -e 's|/local/|/|g' Makefile.PL
perl -pi -e 's|<cdk.h>|<cdk/cdk.h>|g' Cdk.xs
perl -pi -e "s|'INC'\s*=>.*|'INC'=> '-I%{_includedir}/ncurses',|" Makefile.PL
find demos examples fulldemo -type f | xargs perl -pi -e 's|#.*?perl|#!%{_bindir}/perl|g'

perl Makefile.PL 
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

gzip -9nf README BUGS CHANGES NOTES

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz demos examples fulldemo
%attr(755,root,root) %{perl_sitearch}/auto/Cdk
%{perl_sitearch}/*.pm
%{perl_sitearch}/Cdk
