# Note that this is NOT a relocatable package
%define ver      @VERSION@
%define rel      1
%define prefix   /usr

Summary:   L Math Processor
Name:      lmp
Version:   %ver
Release:   %rel
Copyright: GPL
Group:     Utilities/Console
Source0:   @PACKAGE@-%{PACKAGE_VERSION}.tar.gz
URL:       http://lmp.sourceforge.net
BuildRoot: /tmp/@PACKAGE@-%{PACKAGE_VERSION}-root
Packager:  Bernhard J. Pietsch <bjtp@gmx.net>
Docdir: %{prefix}/doc

%description
The L math processor (lmp) implements many basic primitives
for mathematical solution of equations and terms just like
the shell built-in 'expr'. But further lmp handles floating
point numbers and knows some more operations.

%package devel
Summary: Library, includes and API Manual
Group: Development/Libraries
Requires: %{name}

%description devel
The L math processor (lmp) implements many basic primitives
for mathematical solution of equations and terms just like
the shell built-in 'expr'. But further lmp handles floating
point numbers and knows some more operations.

This is the libraries, include files and other resources.

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup -q

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix --disable-debug
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --disable-debug
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc CHANGES COPYING README
%{prefix}/bin/lmp
%{prefix}/lib/lib*.so.*
%{prefix}/man/man1/*

%files devel
%defattr(-, root, root)
%doc CHANGES COPYING README
%{prefix}/include/*
%{prefix}/info/*
%{prefix}/man/man3/*
%{prefix}/lib/lib*.a
%{prefix}/lib/lib*.so

%changelog
* Sun Nov  5 2000 Bernhard J. Pietsch <bjtp@gmx.net>
- Resplit package again (can't decide really :-)
* Sat Nov  4 2000 Bernhard J. Pietsch <bjtp@gmx.net>
- Unsplit package from development and runtime packages
