Summary:	L Math Processor
Summary(pl.UTF-8):	Procesor matematyczny L
Name:		lmp
Version:	0.2.99.10
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/lmp/%{name}_%{version}.tar.gz
# Source0-md5:	8036254a8cf30ac9285fa1bd821ed51d
URL:		http://lmp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The L math processor (lmp) implements many basic primitives for
mathematical solution of equations and terms just like the shell
built-in 'expr'. But further lmp handles floating point numbers and
knows some more operations.

%description -l pl.UTF-8
Procesor matematyczny L (LMP - L Math Processor) ma zaimplementowane
wiele podstawowych sposobów rozwiązywania równań, zachowuje się
podobnie do polecenia 'expr', ale obsługuje liczby zmiennoprzecinkowe
i zna więcej operacji.

%package devel
Summary:	LMP includes and API Manual
Summary(pl.UTF-8):	Pliki nagłówkowe LMP i dokumentacja API
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains LMP include files and other resources.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do LMP.

%package static
Summary:	LMP static library
Summary(pl.UTF-8):	Biblioteka statyczna LMP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
LMP static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne LMP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lmp
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_infodir}/*.info*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
