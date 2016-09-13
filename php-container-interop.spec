%define		pkgname container-interop
%define		php_min_version 5.3.0
Summary:	Promoting the interoperability of container objects (DIC, SL, etc.)
Name:		php-%{pkgname}
Version:	1.1.0
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/container-interop/container-interop/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	53c1d92cbfdf5e1ede5d173a41ea4b19
Source1: 	autoload.php
URL:		https://github.com/container-interop/container-interop
Requires:	php(core) >= %{php_min_version}
Requires:	php-symfony2-ClassLoader >= 2.7.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
container-interop tries to identify and standardize features in
container objects (service locators, dependency injection containers,
etc.) to achieve interopererability.

Through discussions and trials, we try to create a standard, made of
common interfaces but also recommendations.

If PHP projects that provide container implementations begin to adopt
these common standards, then PHP applications and projects that use
containers can depend on the common interfaces instead of specific
implementations. This facilitates a high-level of interoperability and
flexibility that allows users to consume any container implementation
that can be adapted to these interfaces.

The work done in this project is not officially endorsed by the
PHP-FIG [1], but it is being worked on by members of PHP-FIG and other
good developers. We adhere to the spirit and ideals of PHP-FIG, and
hope this project will pave the way for one or more future PSRs.

Autoloader: %{php_data_dir}/Interop/Container/autoload.php

[1] http://www.php-fig.org/

%prep
%setup -qn container-interop-%{version}

cp -p %{SOURCE1} src/Interop/Container/autoload.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE  composer.json docs
%dir %{php_data_dir}/Interop
%{php_data_dir}/Interop/Container
