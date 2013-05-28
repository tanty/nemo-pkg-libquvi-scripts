Name:           libquvi-scripts
Version:        0.4.9
Release:        1
Summary:        Library for parsing video download links (Lua scripts)
Group:          Development/Libraries
License:        LGPLv2+
URL:            http://quvi.sourceforge.net/
Source0:        http://heanet.dl.sourceforge.net/project/quvi/0.4/%{name}/%{name}-%{version}.tar.xz

%description
 Library to parse Adobe flash video download links. It supports Youtube
 and other similar video websites. It provides access to functionality and
 data through an API, and does not enable or require the use of the
 flash technology.
 This package contains the Lua scripts used to parse documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%autogen 
%configure --disable-static
./gen-ver.sh > VERSION
cp VERSION share/lua/version
touch ChangeLog
make %{?jobs:-j%jobs} dist
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/share/libquvi-scripts/*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man7/libquvi-scripts.7.gz
