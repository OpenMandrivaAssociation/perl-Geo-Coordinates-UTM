%define upstream_name    Geo-Coordinates-UTM
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Translation between  Lat Lon and UTM Coords
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module will translate latitude longitude coordinates to Universal
Transverse Mercator(UTM) coordinates and vice versa.

Mercator Projection
    The Mercator projection was first invented to help mariners. They
    needed to be able to take a course and know the distance traveled, and
    draw a line on the map which showed the day's journey. In order to do
    this, Mercator invented a projection which preserved length, by
    projecting the earth's surface onto a cylinder, sharing the same axis
    as the earth itself. This caused all Latitude and Longitude lines to
    intersect at a 90 degree angle, thereby negating the problem that
    longitude lines get closer together at the poles.

Transverse Mercator Projection
    A Transverse Mercator projection takes the cylinder and turns it on its
    side. Now the cylinder's axis passes through the equator, and it can be
    rotated to line up with the area of interest. Many countries use
    Transverse Mercator for their grid systems.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


