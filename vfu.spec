Summary:	VFU is console (text mode) file manager for UNIX/Linux.
Name:		vfu
Version:	1.51
Release:	1
Copyright:	GPL
Group:		Shells
URL:		http://www.biscom.net/~cade/vfu
Vendor:		Vladi Belperchinov-Shabanski "Cade" <cade@biscom.net>
Source:		http://www.biscom.net/~cade/away/%{name}-%{version}-source.tgz
Patch0:		vfu-ncurses.patch
Patch1:		vfu-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VFU is console (text mode) file manager for UNIX/Linux.
Main features are:

 Console/Text mode! ( yes -- repeat that :) )
 Fast One-Key Commands.
 Copy/Move/Erase of selected files/single file/single file while
        selection exists.
 Overwrite prompt when copy/move (Yes/No/Always/Never/...).
 Filename completion (incl. extended completion: `*some[az].zip' ).
 Powerfull ChangeDir function (w. History, Preset favorite dirs...).
 Directory Tree (with sizes).
 Directory(ies) size calculation (single dir/all dirs).
 Run-Time dirs' sizes calculation! (cached from dir tree as option).
 Extensive user-defined external support/utils!
 Interactive/octal chmod and chown (for selected files/single/...).
 File-type colorization (user defined by file type and or extension).
 Incremental search/masking in all file lists.
 Recursive and External rescanning ( Panelize ).
 Archives support (storage/directory) incl. view/browse/extract:
       TAR, TGZ, BZ2, ZIP, UC2, ARJ, JAR, RAR, LIM, LHA, HA,
 FTP support! (archive-like interface)
 Internal Text/Hex file Viewer incl. Hex Editor!
 Internal Text Editor! (Small one:))
 Automount feature (optional).
 Works fine under xterm, rxvt, kvt (with colors etc.)
 + much more...

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
./build

cp -p ftparc/README ftparc/README-ftparc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,%{_bindir}}
install vfu.conf	$RPM_BUILD_ROOT/etc
install vfu/vfu	$RPM_BUILD_ROOT%{_bindir}
install ftparc/ftparc	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf vfu/README README.DOS CONFIG HISTORY \
	VFU.txt XWINDOW ftparc/README-ftparc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {vfu/README,README.DOS,CONFIG,HISTORY}.gz
%doc {VFU.txt,XWINDOW,ftparc/README-ftparc}.gz
%attr(755,root,root) %{_bindir}/vfu
%attr(755,root,root) %{_bindir}/ftparc
%config /etc/vfu.conf
