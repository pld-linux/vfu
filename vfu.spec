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
BuildRoot:	/var/tmp/%{name}-%{version}

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

%changelog
* Mon Mar 22 1999 Ryan Weaver <ryanw@infohwy.com>
  [vfu-1.46-1]
- 1.46: 19.Mar.99
- Support for /etc/DIR_COLORS (for file-type colorization)
  See Option/UseEtcDirColors.
- Small internal Text editor added! (can be used as
  emergency editor if no other available)
  See Option/UseInternalEditor.
- Added Lynx-like arrow keys navigation:
  UpArrow/DownArrow    -- scroll list
  LeftArrow/RightArrow -- enter/exit/cdup
  See Options/AltArrowsNavigate.
- Separate histories to all input lines. Use
  PageUp/PageDown to recall.
- Now SymLink references can be edited in-place.
  See EditEntry(key TAB)/EditSymLinkReference(key L).
- File Find results can be panelized now.
- The usual bugfixes ( not important really ).
- Changed location for personal config and other related files,
  now default place is `$HOME/.vfu'. Changed VFU config file
  name from `vfurc' to `vfu.conf'.
  Please read CONFIG file!
- Now the internal Viewer and Editor (See/Seed) have separate
  options files. The `see(d).options' location is
  `$HOME/$RC_PREFIX/.see(d)/see(d).options'.

* Thu Mar  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [vfu-1.45-2]
- Bugfix....

* Thu Mar  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [vfu-1.45-1]
- 1.45: 03.Mar.99
- `%i' and `%n' macros added. (See abov for details)
- Now VFU won't expand masks if you enter external scan/panelize
  command in the file mask field.
- Now VFU will remember internal file viewer options during the
  same session.
- GlobalSelect/SelectSame/Type(TP) function added.
- HexEditor added! See the help in the internal file viewer
  ( press `I' in the HEX mode of the internal file viewer )
- Fixed pattern searching function ( it didn't work before with
  patterns that contains char codes >128 sometimes )
- FTP support! See above for details.
- Few bugfixes as usual...

* Wed Feb 17 1999 Ryan Weaver <ryanw@infohwy.com>
  [vfu-1.44-1]
- 1.44: 14.Feb.98
- Auto mounting on change directory added.
  ( see Options/AutoMount )
  If you chdir to a directory which contains only
  one file named `automount', then VFU will try to
  mount this directory automatically. After mounting
  `automount' file won't be visible. You can create
  file with `echo > automount' command.
- Unmount feature added to the `JumpToMountpoint'
  menu ( key `j' ).
- PreserveSelection option added. If this option is
  enabled VFU will preserve selected files after
  rescanning files list. ( see Options menu )
- Added Ctrl+Z key to the Directory Tree View for
  update the current (under cursor) directory size.
- Fixed tilde `~' expansion -- now standalone
  `~' or `~username' are expanded properly.
- RecursiveRescanning can be canceled with ESC now.
- Options(Toggles) separators bug fixed.
- User External Utilities are enabled in InArchive mode
  as it should be. (considered bug)
- Dotfiles `.filename' colorization fixed.

- 1.43: 12.Feb.98
- Now VFU supports properly screens >80x25
  (fixed bug with 80-columns filename view)
- ENTER has priority now for entering into archives
  than executing user external program.
- Added option for handling .TGZ equally to .tgz, i.e.
  case insensitive archive extension detection.
- RenameTools added to the tools menu (key `T')
- Added one more location for global vfurc file: `/etc/'
  it is searched first. Can be changed through VFU_RCPATH0
  define.
- Now $HOME/.vfurc is primary if exists ( before global
  vfurc's as it should be ) considered as bug :)
- ENTER key behavior changed:
  If not defined for user external utility, ENTER works
  as browse/view. It also assumed equal to '+' or '=' for
  archives ( i.e. cannot be redefined for archives,
  there's INSERT and Fx alternatives, however if someone
  needs ENTER for this I probably can change it ).
- MenuBorders option added. It can improve menu visibility
  on mono/colorless terminals.

* Thu Feb  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [vfu-1.42-1]
- First RPM Build
- 1.42: 03.Feb.98
- + feature add
    1. External scanning ( panelize ).
       Just enter `command |' in the files masks input line
       to use it ( i.e. instead of "*.txt" enter
       "find / -name '*.txt'" ).
- ! bugfix
    2. The problem with files/dirs' sizes >2GB is now fixed!
