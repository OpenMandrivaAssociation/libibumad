Summary:	OpenFabrics Alliance InfiniBand umad (user MAD) library
Name:		libibumad
Version:	1.3.10.2
Release:	1
License:	GPLv2 or BSD
Url:		http://www.openfabrics.org
Source:		http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc

%description
libibumad provides the user MAD library functions which sit on top of
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM.

%files
%{_libdir}/libibumad*.so.*
%{_mandir}/man3/*
%doc AUTHORS COPYING ChangeLog

#---------------------------------------------------------------------------

%package devel
Summary: Development files for the libibumad library
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the libibumad library.

%files devel
%{_libdir}/libibumad.so
%{_includedir}/infiniband/*.h

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
export CC=gcc
export CXX=g++
%configure
%make_build

%install
%make_install

# remove unpackaged files from the buildroot
find %{buildroot} -name '*.la' -delete \;

