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
