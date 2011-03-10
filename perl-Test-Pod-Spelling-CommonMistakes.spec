%define upstream_name    Test-Pod-Spelling-CommonMistakes
%define upstream_version 1.000

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Checks POD for common spelling mistakes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Pod::Spell::CommonMistakes)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module checks your POD for common spelling errors. This differs than
the Test::Spelling manpage because it doesn't use your system spellchecker
and instead uses the Pod::Spell::CommonMistakes manpage for the heavy
lifting. Using it is the same as any standard Test::* module, as seen here.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


