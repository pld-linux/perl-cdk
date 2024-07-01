#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	Perl extensions for CDK
Summary(pl.UTF-8):	Rozszerzenie Perla dla CDK
Name:		perl-cdk
Version:	20150928
Release:	6
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.invisible-island.net/cdk/cdk-perl-%{version}.tgz
# Source0-md5:	28bb44e50b15c94f0f6f6e86c5a69c96
URL:		http://invisible-island.net/cdk/
BuildRequires:	cdk-devel >= 5
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
%configure

%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -DNCURSES_INTERNALS"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES demos fulldemo
%{perl_vendorarch}/Cdk.pm
%{perl_vendorarch}/Cdk
%dir %{perl_vendorarch}/auto/Cdk
%attr(755,root,root) %{perl_vendorarch}/auto/Cdk/Cdk.so
%{perl_vendorarch}/auto/Cdk/autosplit.ix
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
