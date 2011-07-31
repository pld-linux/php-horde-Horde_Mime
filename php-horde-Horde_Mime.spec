# TODO
# - use system locale location
%define		status		stable
%define		pearname	Horde_Mime
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde MIME Library
Name:		php-horde-Horde_Mime
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	d02e1ab98d5b10290a41584e5d2a463a
URL:		https://github.com/horde/horde/tree/master/framework/Mime/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Mail < 2.0.0
Requires:	php-horde-Horde_Stream_Filter < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Text_Flowed < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Nls
Suggests:	php-horde-Horde_Text_Filter
Suggests:	php-pear-Net_DNS2
Suggests:	php-pecl-idn
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Nls.*) pear(Horde/Text/Filter.*) pear(Net/DNS2.*) pear(idn.*)

%description
Provides methods for dealing with MIME (RFC 2045) and related e-mail
(RFC 822/2822/5322) standards.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Mime.php
%{php_pear_dir}/Horde/Mime
%{php_pear_dir}/data/Horde_Mime
