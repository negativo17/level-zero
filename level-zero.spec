Name:           level-zero
Version:        1.8.5
Release:        0%{?dist}
Summary:        oneAPI Level Zero Loader
License:        MIT
URL:            https://spec.oneapi.io/level-zero/latest/index.html

Source0:        https://github.com/oneapi-src/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  devtoolset-9-gcc-c++
BuildRequires:  devtoolset-9-gcc

%description
API Headers, Loader, & Validation Layer based on oneAPI Level Zero
Specification.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
. /opt/rh/devtoolset-9/enable
%cmake3
%cmake3_build

%install
%cmake3_install

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md SECURITY.md
%{_libdir}/libze_loader.so.1
%{_libdir}/libze_loader.so.1.8.0
%{_libdir}/libze_tracing_layer.so.1
%{_libdir}/libze_tracing_layer.so.1.8.0
%{_libdir}/libze_validation_layer.so.1
%{_libdir}/libze_validation_layer.so.1.8.0

%files devel
%{_includedir}/level_zero
%{_libdir}/libze_loader.so
%{_libdir}/libze_tracing_layer.so
%{_libdir}/libze_validation_layer.so
%{_libdir}/pkgconfig/level-zero.pc
%{_libdir}/pkgconfig/libze_loader.pc

%changelog
* Thu Sep 29 2022 Simone Caronni <negativo17@gmail.com> - 1.8.5-1
- First build.
