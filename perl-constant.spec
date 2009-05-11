
%define realname   constant
%define version    1.17
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Define compile-time constants
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::More)
Provides: perl(constant)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


