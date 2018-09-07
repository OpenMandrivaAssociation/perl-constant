%define upstream_name    constant
%define upstream_version 1.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Define compile-time constants
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//constant-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
Provides:	perl(constant)
BuildArch:	noarch

%description
This pragma allows you to declare constants at compile-time.

When you declare a constant such as 'PI' using the method shown above, each
machine your script runs upon can have as many digits of accuracy as it can
use. Also, your program will be easier to read, more likely to be
maintained (and maintained correctly), and far less likely to send a space
probe to the wrong planet because nobody noticed the one equation in which
you wrote '3.14195'.

When a constant is used in an expression, Perl replaces it with its value
at compile time, and may then optimize the expression further. In
particular, any code in an 'if (CONSTANT)' block will be optimized away if
the constant is false.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.210.0-1mdv2011.0
+ Revision: 659889
- update to new version 1.21

* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.200.0-1
+ Revision: 653998
- update to new version 1.20

* Mon Sep 14 2009 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2010.0
+ Revision: 439421
- update to 1.19

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-3mdv2010.0
+ Revision: 420986
- rebuild
- rebuild
- update to 1.18

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2010.0
+ Revision: 418638
- update to 1.18

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2010.0
+ Revision: 401700
- rebuild using %%perl_convert_version
- fixed license field

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.17-1mdv2010.0
+ Revision: 374343
- import perl-constant


* Mon May 11 2009 cpan2dist 1.17-1mdv
- initial mdv release, generated with cpan2dist


