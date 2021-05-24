#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-Bluetooth
Version  : 0.41
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/A/AD/ADDUTKO/Net-Bluetooth-0.41.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AD/ADDUTKO/Net-Bluetooth-0.41.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0+
Requires: perl-Net-Bluetooth-perl = %{version}-%{release}
BuildRequires : bluez-dev
BuildRequires : buildreq-cpan

%description
INSTALL
TO INSTALL RUN:

perl Makefile.PL
make
make test
make install

If you would like to use the prebuilt Windows XP version,
you can find the most recent ppd file at:
http://www.conditor.com/Net-Bluetooth.ppd

Usually to install the prebuilt Windows XP version you would run:
ppm install http://www.conditor.com/Net-Bluetooth.ppd

%package dev
Summary: dev components for the perl-Net-Bluetooth package.
Group: Development
Provides: perl-Net-Bluetooth-devel = %{version}-%{release}
Requires: perl-Net-Bluetooth = %{version}-%{release}

%description dev
dev components for the perl-Net-Bluetooth package.


%package perl
Summary: perl components for the perl-Net-Bluetooth package.
Group: Default
Requires: perl-Net-Bluetooth = %{version}-%{release}

%description perl
perl components for the perl-Net-Bluetooth package.


%prep
%setup -q -n Net-Bluetooth-0.41
cd %{_builddir}/Net-Bluetooth-0.41

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::Bluetooth.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Net/Bluetooth.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Net/Bluetooth/Bluetooth.so
