# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name foundation
%global pkgver %{pkg_name}-%{version}

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.0.13
Release:        1%{?dist}
Summary:        Alternative prelude with batteries and no dependencies

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif
# End cabal-rpm deps

%description
A custom prelude with no dependencies apart from base.

This package has the following goals:

* provide a base like sets of modules that provide a consistent set of features
and bugfixes across multiple versions of GHC (unlike base).

* provide a better and more efficient prelude than base's prelude.

* be self-sufficient: no external dependencies apart from base.

* provide better data-types: packed unicode string by default, arrays.

* Better numerical classes that better represent mathematical thing (No more
all-in-one Num).

* Better I/O system with less Lazy IO

* Usual partial functions distinguished through type system.


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
%doc CHANGELOG.md README.md


%changelog
* Tue Jul 25 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.0.13-1
- spec file generated by cabal-rpm-0.11.1