Summary:	VFU is console (text mode) file manager for UNIX/Linux
Summary(pl.UTF-8):	VFU - tekstowy zarządca plików dla Uniksa/Linuksa
Name:		vfu
Version:	4.05
Release:	0.1
License:	GPL
Group:		Applications/Shells
Source0:	http://www.ibiblio.org/pub/Linux/utils/file/managers/%{name}-%{version}.tar.gz
# Source0-md5:	63e822f9d61f1c9430867a115141a5a3
URL:		http://soul.datamax.bg/~cade/vfu/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VFU is console (text mode) file manager for UNIX/Linux. Main features
are:
- Console/Text mode! (yes -- repeat that :))
- Fast One-Key Commands.
- Copy/Move/Erase of selected files/single file/single file while
  selection exists.
- Overwrite prompt when copy/move (Yes/No/Always/Never/...).
- Filename completion (incl. extended completion: `*some[az].zip').
- Powerfull ChangeDir function (w. History, Preset favorite dirs...).
- Directory Tree (with sizes).
- Directory(ies) size calculation (single dir/all dirs).
- Run-Time dirs' sizes calculation! (cached from dir tree as option).
- Extensive user-defined external support/utils!
- Interactive/octal chmod and chown (for selected files/single/...).
- File-type colorization (user defined by file type and or extension).
- Incremental search/masking in all file lists.
- Recursive and External rescanning ( Panelize ).
- Archives support (storage/directory) incl. view/browse/extract: TAR,
  TGZ, BZ2, ZIP, UC2, ARJ, JAR, RAR, LIM, LHA, HA,
- FTP support! (archive-like interface)
- Internal Text/Hex file Viewer incl. Hex Editor!
- Internal Text Editor! (Small one:))
- Automount feature (optional).
- Works fine under xterm, rxvt, kvt (with colors etc.)
- and much more...

%description -l pl.UTF-8
VFU jest konsolowym (tekstowym) zarządcą plików dla Uniksa/Linuksa.
Główne jego zalety to:
- tryb tekstowy (tak!)
- szybkie polecenia jednoklawiszowe
- kopiowanie/przenoszenie/usuwanie wybranych plików/jednego
  pliku/jednego pliku kiedy więcej jest wybranych
- pytanie o nadpisanie przy kopiowaniu/przenoszeniu
  (tak/nie/zawsze/nigdy)
- uzupełnianie nazw (także rozszerzone, np. '*some[az].zip')
- użyteczna funkcja zmiany katalogu (z historią i ulubionymi
  katalogami)
- drzewo katalogów (z rozmiarami)
- obliczanie rozmiarów katalogów (jednego/wszystkich)
- obliczanie rozmiarów katalogów w locie (cache jako opcja)
- obsługa zewnętrznych narzędzi konfigurowalna przez użytkownika
- interaktywne/ósemkowe chmod i chown (dla wybranych plików/jednego
  pliku)
- kolor zależny od rodzaju pliku (konfigurowalny)
- przeszukiwanie przyrostowe i maski we wszystkich listach plików
- rekurencyjne przeszukiwanie
- obsługa archiwów: tar, tgz, bz2, zip, uc2, arj, jar, rar, lim, lha,
  ha
- obsługa FTP (podobna do archiwów)
- wbudowana przeglądarka tekstu i szesnastkowa z edytorem
  heksadecymalnym
- wbudowany edytor tekstu
- automatyczne montowanie (opcjonalnie)
- działa dobrze pod xtermem, rxvt, kvt (z kolorami itp.)
- i wiele innych...

%prep
%setup -q

%build
./build
mv rx/README rx/README.rx

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}

install vfu/vfu rx/rx_* $RPM_BUILD_ROOT%{_bindir}
install vfu.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONFIG FAQ HISTORY NOTES README README.DOS THANKS.TO TODO XWINDOW.NOTES rx/README.rx
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
