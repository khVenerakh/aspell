Summary:	GNU Aspell is an Open Source spell checker
Summary(pl.UTF-8):	GNU Aspell jest kontrolerem pisowni
Summary(pt_BR.UTF-8):	Verificador ortográfico
Name:		aspell
Version:	0.60.6
Release:	3
Epoch:		3
License:	LGPL v2 or v2.1
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
# Source0-md5:	bc80f0198773d5c05086522be67334eb
Patch0:		%{name}-info.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-mk-static-filter.pl.patch
URL:		http://aspell.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.16.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	texinfo
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	pspell = %{epoch}:%{version}-%{release}
Obsoletes:	libaspell15
Obsoletes:	pspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Aspell is a Free and Open Source spell checker designed to
eventually replace Ispell. It can either be used as a library or as an
independent spell checker. Its main feature is that it does a much
better job of coming up with possible suggestions than just about any
other spell checker out there for the English language, including
Ispell and Microsoft Word. It also has many other technical
enhancements over Ispell such as using shared memory for dictionaries
and intelligently handling personal dictionaries when more than one
Aspell process is open at once.

%description -l pl.UTF-8
GNU Aspell jest kontrolerem pisowni zaprojektowanym tak, by móc
zastąpić ispella. Dodatkowo zawiera wsparcie dla innych języków niż
angielski. Interfejs aspella napisany został w C++, a interfejsy w
Perlu i C są aktualnie rozwijane.

%description -l pt_BR.UTF-8
GNU Aspell é um verificador ortográfico criado para substituir o
antigo "ispell". Sua principal vantagem (sobre o Ispell) é uma melhor
sugestão de correções. Aspell inclui suporte a vários idiomas e pode
fazer a checagem de arquivos LaTeX e HTML.

%package libs
Summary:	aspell libraries
Summary(pl.UTF-8):	Biblioteki aspella
Group:		Libraries
Conflicts:	aspell < 0.60.4-1.2

%description libs
aspell/pspell libraries

%description libs -l pl.UTF-8
Biblioteki aspell/pspell.

%package devel
Summary:	Header files for aspell development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających aspella
Summary(pt_BR.UTF-8):	Arquivos para desenvolvimento usando Aspell
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel
Provides:	pspell-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libaspell15-devel
Obsoletes:	pspell-devel

%description devel
Aspell is an Open Source spell checker. This package contains header
files for aspell development.

%description devel -l pl.UTF-8
Aspell jest kontrolerem pisowni. Ten pakiet zawiera pliki nagłówkowe
dla programistów używających bibliotek aspella.

%description devel -l pt_BR.UTF-8
Aspell é um corretor ortográfico. O pacote -devel inclui bibliotecas
dinâmicas e arquivos de inclusão necessários para o desenvolvimento
utilizando o aspell.

%package static
Summary:	Static libraries for aspell development
Summary(pl.UTF-8):	Biblioteki statyczne aspella
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento usando Aspell
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	pspell-static = %{epoch}:%{version}-%{release}
Obsoletes:	pspell-static

%description static
Aspell is an Open Source spell checker. This package contains static
aspell libraries.

%description static -l pl.UTF-8
Aspell jest kontrolerem pisowni. Pakiet ten zawiera biblioteki
statyczne aspella.

%description static -l pt_BR.UTF-8
Aspell é um corretor ortográfico. O pacote -devel-static inclui as
bibliotecas estáticas necessárias para o desenvolvimento utilizando o
aspell.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static \
	--enable-pkgdatadir=%{_datadir}/aspell \
	--enable-pkglibdir=%{_libdir}/aspell

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README manual/aspell.html
%{_infodir}/aspell.info*
%attr(755,root,root) %{_bindir}/aspell
%attr(755,root,root) %{_bindir}/aspell-import
%attr(755,root,root) %{_bindir}/pre*
%attr(755,root,root) %{_bindir}/run-with-aspell
%attr(755,root,root) %{_bindir}/word-list-compress
%dir %{_datadir}/aspell
%attr(755,root,root) %{_datadir}/aspell/ispell
%attr(755,root,root) %{_datadir}/aspell/spell
%{_datadir}/aspell/*.cmap
%{_datadir}/aspell/*.cset
%{_datadir}/aspell/*.kbd
%{_mandir}/man1/aspell.1*
%{_mandir}/man1/aspell-import.1*
%{_mandir}/man1/pre*.1*
%{_mandir}/man1/run-with-aspell.1*
%{_mandir}/man1/word-list-compress.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaspell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaspell.so.15
%attr(755,root,root) %{_libdir}/libpspell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpspell.so.15
%{_libdir}/aspell

%files devel
%defattr(644,root,root,755)
%doc manual/aspell-dev.html
%attr(755,root,root) %{_bindir}/pspell-config
%attr(755,root,root) %{_libdir}/libaspell.so
%attr(755,root,root) %{_libdir}/libpspell.so
%{_libdir}/libaspell.la
%{_libdir}/libpspell.la
%{_includedir}/pspell
%{_includedir}/aspell.h
%{_mandir}/man1/pspell-config.1*
%{_infodir}/aspell-dev.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libaspell.a
%{_libdir}/libpspell.a
