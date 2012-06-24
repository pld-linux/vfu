Summary:	VFU is console (text mode) file manager for UNIX/Linux
Summary(pl):	VFU - tekstowy zarz�dca plik�w dla uniksa/Linuksa
Name:		vfu
Version:	1.51
Release:	1
License:	GPL
Group:		Applications/Shells
Vendor:		Vladi Belperchinov-Shabanski "Cade" <cade@biscom.net>
Source0:	http://www.biscom.net/~cade/away/%{name}-%{version}-source.tgz
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-opt.patch
URL:		http://www.biscom.net/~cade/vfu/
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

%description -l pl
VFU jest konsolowym (tekstowym) zarz�dc� plik�w dla uniksa/Linuksa.
G��wne jego zalety to:
- tryb tekstowy (tak!)
- szybkie polecenia jednoklawiszowe
- kopiowanie/przenoszenie/usuwanie wybranych plik�w/jednego
  pliku/jednego pliku kiedy wi�cej jest wybranych
- pytanie o nadpianie przy kopiowaniu/przenoszeniu
  (tak/nie/zawsze/nigdy)
- uzupe�nianie nazw (tak�e rozszerzone, np. '*some[az].zip')
- u�yteczna funkcja zmiany katalogu (z histori� i ulubionymi
  katalogami)
- drzewo katalog�w (z rozmiarami)
- obliczanie rozmiar�w katalog�w (jednego/wszystkich)
- obliczanie rozmiar�w katalog�w w locie (cache jako opcja)
- obs�uga zewn�trznych narz�dzi konfigurowalna przez u�ytkownika
- interaktywne/�semkowe chmod i chown (dla wybranych plik�w/jednego
  pliku)
- kolor zale�ny od rodzaju pliku (konfigurowalny)
- przeszukiwanie przyrostowe i maski we wszystkich listach plik�w
- rekurencyjne przeszukiwanie
- obs�uga archiw�w: tar, tgz, bz2, zip, uc2, arj, jar, rar, lim, lha,
  ha
- obs�uga FTP (podobna do archiw�w)
- wbudowana przegl�darka tekstu i szesnastkowa z edytorem
  heksadecymalnym
- wbudowany edytor tekstu
- automatyczne montowanie (opcjonalnie)
- dzia�a dobrze pod xtermem, rxvt, kvt (z kolorami itp.)
- i wiele innych...

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
./build

cp -p ftparc/README ftparc/README-ftparc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}

install vfu.conf	$RPM_BUILD_ROOT%{_sysconfdir}
install vfu/vfu		$RPM_BUILD_ROOT%{_bindir}
install ftparc/ftparc	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc vfu/README README.DOS CONFIG HISTORY VFU.txt XWINDOW ftparc/README-ftparc
%attr(755,root,root) %{_bindir}/vfu
%attr(755,root,root) %{_bindir}/ftparc
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vfu.conf
