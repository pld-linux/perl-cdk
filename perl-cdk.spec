#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Perl extensions for CDK
Summary(pl):	Rozszerzenie Perla dla CDK
Name:		perl-cdk
Version:	20020728
Release:	2
License:	distributable 
Group:		Development/Languages/Perl
Source0:	ftp://dickey.his.com/cdk/cdk-perl-%{version}.tgz
BuildRequires:	cdk-devel
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%build
%{__perl} -pi -e 's|/local/|/|g' Makefile.PL
%{__perl} -pi -e 's|<cdk.h>|<cdk/cdk.h>|g' Cdk.xs
%{__perl} -pi -e "s|'INC'\s*=>.*|'INC'=> '-I%{_includedir}/ncurses',|" Makefile.PL
find demos examples fulldemo -type f | xargs perl -pi -e 's|#.*?perl|#!%{_bindir}/perl|g'

%{__perl} Makefile.PL 
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README CHANGES demos fulldemo
%attr(755,root,root) %{perl_sitearch}/auto/Cdk
%{perl_sitearch}/*.pm
%{perl_sitearch}/Cdk
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
