# generated by cabal-rpm-0.11.1
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name authenticate-oauth
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.6
Release:        4%{?dist}
Summary:        Library to authenticate with OAuth for Haskell web applications

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-RSA-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-crypto-pubkey-types-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
Authentication methods for Haskell web applications.

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


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md


%changelog
* Tue Nov 14 2017 David Shea <dshea@redhat.com> - 1.6-4
- Replace the %%description

* Tue Oct 24 2017 David Shea <dshea@redhat.com> - 1.6-3
- Rebuild against the Fedora version of asn1-encoding

* Tue Sep 12 2017 David Shea <dshea@redhat.com> - 1.6-2
- Rebuild against various rebuilt dependencies

* Thu Aug  3 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.6-1
- spec file generated by cabal-rpm-0.11.1
