# generated by cabal-rpm-0.11.2
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name gi-gio
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        2.0.14
Release:        1%{?dist}
Summary:        Gio bindings

License:        LGPLv2+
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-gi-glib-devel
BuildRequires:  ghc-gi-gobject-devel
BuildRequires:  ghc-haskell-gi-base-devel
BuildRequires:  ghc-haskell-gi-devel
BuildRequires:  ghc-haskell-gi-overloading-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  pkgconfig(gio-2.0)
# End cabal-rpm deps

%description
Bindings for Gio, autogenerated by haskell-gi.


%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
# Begin cabal-rpm deps:
Requires:       pkgconfig(gio-2.0)
# End cabal-rpm deps

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build_without_haddock


%install
%ghc_lib_install
mv %{buildroot}%{_ghcdocdir}{,-devel}


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files devel -f %{name}-devel.files
%license LICENSE
%doc ChangeLog.md README.md


%changelog
* Tue Sep 12 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.0.14-1
- spec file generated by cabal-rpm-0.11.2

%files -f %{name}.files
%license LICENSE
