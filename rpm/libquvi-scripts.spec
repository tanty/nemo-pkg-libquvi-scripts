Name:           libquvi-scripts
Version:        0.9.0
Release:        1
Summary:        Library for parsing video download links (Lua scripts)
Group:          Development/Libraries
License:        LGPLv2+
URL:            http://quvi.sourceforge.net/
Source0:        http://heanet.dl.sourceforge.net/project/quvi/0.4/%{name}/%{name}-%{version}.tar.xz
Patch0:         do-not-dist-man.patch

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

%patch0 -p1

%build
echo v%{version} > VERSION
./bootstrap.sh
%configure --without-manual --disable-static
cp VERSION share/version
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
%{_libdir}/pkgconfig/%{name}-0.9.pc
