# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name haskell-gi-base
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        0.20.3
Release:        1%{?dist}
Summary:        Foundation for libraries generated by haskell-gi

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-text-devel
BuildRequires:  pkgconfig(gobject-2.0)
# End cabal-rpm deps

%description
Foundation for libraries generated by haskell-gi.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gobject-2.0)
# End cabal-rpm deps

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc ChangeLog.md


%changelog
* Tue Jul 25 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.20.3-1
- spec file generated by cabal-rpm-0.11.1