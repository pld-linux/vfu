%define	name	vfu
%define	version	1.46
%define	release	1
%define	serial	1

Summary:	VFU is console (text mode) file manager for UNIX/Linux.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		Shells
URL:		http://www.biscom.net/~cade/vfu
Vendor:		Vladi Belperchinov-Shabanski "Cade" <cade@biscom.net>
Source:		%{name}-%{version}-source.tgz
Distribution:	Freshmeat RPMs
Packager:	Ryan Weaver <ryanw@infohwy.com>
BuildRoot:	/tmp/%{name}-%{version}-root

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

%build
./build

cp -p ftparc/README ftparc/README-ftparc

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/{etc,usr/bin}
install    -m 644 vfu.conf	$RPM_BUILD_ROOT/etc
install -s -m 755 vfu/vfu	$RPM_BUILD_ROOT%{_bindir}
install -s -m 755 ftparc/ftparc	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc vfu/COPYING vfu/README README.DOS  vfu/CONFIG vfu/HISTORY vfu/INSTALL
%doc vfu/VFU.txt XWINDOW ftparc/README-ftparc

%{_bindir}/vfu
%{_bindir}/ftparc
%config /etc/vfu.conf
