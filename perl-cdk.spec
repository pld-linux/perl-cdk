#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Perl extensions for CDK
Summary(pl.UTF-8):   Rozszerzenie Perla dla CDK
Name:		perl-cdk
Version:	20031210
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://dickey.his.com/cdk/cdk-perl-%{version}.tgz
# Source0-md5:	d5814507d7d2b5e3e7e5ababfa9e7d86
BuildRequires:	cdk-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Perl5 extension to the CDK library written by Mike Glover.
All the copyright notices from the CDK C distribution also apply to
the extension.

%description -l pl.UTF-8
To jest rozszerzenie Perla do biblioteki CDK. Wszystkie copyrighty z
dystrybucji CDK dotyczą także tego rozszerzenia.

%prep
%setup -q -n cdk-perl-%{version}

%build
%{__perl} -pi -e 's|/local/|/|g' Makefile.PL
%{__perl} -pi -e 's|<cdk.h>|<cdk/cdk.h>|g' Cdk.xs
%{__perl} -pi -e "s|'INC'\s*=>.*|'INC'=> '-I/usr/include/ncurses',|" Makefile.PL
find demos examples fulldemo -type f | xargs perl -pi -e 's|#.*?perl|#!%{_bindir}/perl|g'

%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES demos fulldemo
%attr(755,root,root) %{perl_vendorarch}/auto/Cdk
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/Cdk
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
