%define upstream_name    Test-Pod-Spelling-CommonMistakes
%define upstream_version 1.000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Checks POD for common spelling mistakes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Spell::CommonMistakes)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module checks your POD for common spelling errors. This differs than
the Test::Spelling manpage because it doesn't use your system spellchecker
and instead uses the Pod::Spell::CommonMistakes manpage for the heavy
lifting. Using it is the same as any standard Test::* module, as seen here.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 657472
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1
+ Revision: 643495
- update to new version 1.000

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 573215
- import perl-Test-Pod-Spelling-CommonMistakes

