# TODO: sukija (both malaga and vfst)
#
# Conditional build:
%bcond_without	vfst	# dictionaries for VFST backend

Summary:	Description of Finnish morphology written in Malaga
Summary(pl.UTF-8):	Opis morfologii języka fińskiego napisany w języku Malaga
Name:		voikko-fi
Version:	2.1
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/voikko/corevoikko/releases
Source0:	https://github.com/voikko/corevoikko/archive/rel-voikko-fi-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d92d85476f5e841e46a179408e6ab450
URL:		http://voikko.puimula.org/
%{?with_vfst:BuildRequires:	foma}
BuildRequires:	libstdc++-devel
BuildRequires:	malaga >= 7.8
BuildRequires:	python3 >= 1:3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Description of Finnish morphology written in Malaga.

%description -l pl.UTF-8
Opis morfologii języka fińskiego napisany w języku Malaga.

%package malaga
Summary:	Finish dictionary for voikko spellchecker/hyphenator
Summary(pl.UTF-8):	Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów voikko
Group:		Applications/Text
Requires:	libvoikko >= 2.2
Provides:	voikko-fi = %{version}
Obsoletes:	voikko-fi < %{version}

%description malaga
Finish dictionary for voikko spellchecker/hyphenator.

%description malaga -l pl.UTF-8
Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów
voikko.

%package vfst
Summary:	Finish dictionary for voikko spellchecker/hyphenator
Summary(pl.UTF-8):	Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów voikko
Group:		Applications/Text
Requires:	libvoikko >= 4.0
Provides:	voikko-fi = %{version}
Obsoletes:	voikko-fi < %{version}

%description vfst
Finish dictionary for voikko spellchecker/hyphenator.

%description vfst -l pl.UTF-8
Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów
voikko.

#package -n sukija-fi

%prep
%setup -q -n corevoikko-rel-voikko-fi-%{version}

%build
%{__make} -C voikko-fi all %{?with_vfst:vvfst}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C voikko-fi voikko-install \
	DESTDIR=$RPM_BUILD_ROOT%{_libdir}/voikko

%if %{with vfst}
%{__make} -C voikko-fi vvfst-install \
	DESTDIR=$RPM_BUILD_ROOT%{_datadir}/voikko
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n voikko-fi-malaga
%defattr(644,root,root,755)
%doc voikko-fi/{CONTRIBUTORS,ChangeLog,README}
%lang(fi) %doc voikko-fi/README.fi
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.pro
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.lex_*
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.mor_*
%{_libdir}/voikko/2/mor-standard/voikko-fi_FI.sym_*

%files -n voikko-fi-vfst
%defattr(644,root,root,755)
%doc voikko-fi/{CONTRIBUTORS,ChangeLog,README}
%lang(fi) %doc voikko-fi/README.fi
%{_datadir}/voikko/5/mor-standard/autocorr.vfst
%{_datadir}/voikko/5/mor-standard/index.txt
%{_datadir}/voikko/5/mor-standard/mor.vfst

#files -n sukija-fi
