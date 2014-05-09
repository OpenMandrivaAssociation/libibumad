Summary: OpenFabrics Alliance InfiniBand umad (user MAD) library
Name:    libibumad
Version: 1.3.9
Release: 1%{?dist}
License: GPLv2 or BSD

Url:     http://www.openfabrics.org
Source:  http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Source1: %{name}.rpmlintrc

BuildRequires: libtool, automake, autoconf, glibc-static-devel
ExcludeArch: s390 s390x

%description
libibumad provides the user MAD library functions which sit on top of 
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM. 

%package devel
Summary: Development files for the libibumad library

Requires: %{name} = %{version}-%{release}

%description devel
Development files for the libibumad library.

%package static
Summary: Static version of the libibumad library

Requires: %{name}-devel = %{version}-%{release}

%description static
Static version of the libibumad library.

%prep
%setup -q

%build
%configure2_5x
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%{_libdir}/libibumad*.so.*
%{_mandir}/man3/*
%doc AUTHORS COPYING ChangeLog 

%files devel
%{_libdir}/libibumad.so
%{_includedir}/infiniband/*.h

%files static
%{_libdir}/libibumad.a
