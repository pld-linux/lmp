Summary:	L Math Processor
Summary(pl):	Procesor matematyczny L
Name:		lmp
Version:	0.2.99.10
Release:	1
License:	GPL
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Source0:	ftp://lmp.sourceforge.net/pub/lmp/beta/%{name}_%{version}.tar.gz
URL:		http://lmp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The L math processor (lmp) implements many basic primitives for
mathematical solution of equations and terms just like the shell
built-in 'expr'. But further lmp handles floating point numbers and
knows some more operations.

%description -l pl
Procesor matematyczny L (LMP - L Math Processor) ma zaimplementowane
wiele podstawowych sposobСw rozwi╠zywania rСwnaЯ, zachowuje siЙ
podobnie do polecenia 'expr', ale obsЁuguje liczby zmiennoprzecinkowe
i zna wiЙcej operacji.

%package devel
Summary:	LMP includes and API Manual
Summary(pl):	Pliki nagЁСwkowe LMP i dokumentacja API
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
This package contains LMP include files and other resources.

%description devel -l pl
Pliki nagЁСwkowe i inne do LMP.

%package static
Summary:	LMP static library
Summary(pl):	Biblioteka statyczna LMP
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lmp
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_infodir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
