# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name RSA
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Implementation of RSA, using the padding schemes of PKCS#1 v2.1

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-crypto-pubkey-types-devel
BuildRequires:  ghc-pureMD5-devel
%if %{with tests}
BuildRequires:  ghc-DRBG-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif
# End cabal-rpm deps

%description
This library implements the RSA encryption and signature algorithms for
arbitrarily-sized ByteStrings. While the implementations work, they are not
necessarily the fastest ones on the planet. Particularly key generation.
The algorithms included are based of RFC 3447, or the Public-Key Cryptography
Standard for RSA, version 2.1 (a.k.a, PKCS#1 v2.1).


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


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
* Thu Aug  3 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.2.0-1
- spec file generated by cabal-rpm-0.11.1
