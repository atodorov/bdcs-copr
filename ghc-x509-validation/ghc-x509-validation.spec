# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name x509-validation
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        1.6.9
Release:        1%{?dist}
Summary:        X.509 Certificate and CRL validation

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-asn1-encoding-devel
BuildRequires:  ghc-asn1-types-devel
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-hourglass-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pem-devel
BuildRequires:  ghc-x509-devel
BuildRequires:  ghc-x509-store-devel
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif
# End cabal-rpm deps

%description
X.509 Certificate and CRL validation.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%cabal_test


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files


%changelog
* Tue Sep 12 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.6.9-1
- spec file generated by cabal-rpm-0.11.2
