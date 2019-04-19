# TODO: sukija (both malaga and vfst)
Summary:	Description of Finnish morphology written in Malaga
Summary(pl.UTF-8):	Opis morfologii języka fińskiego napisany w języku Malaga
Name:		voikko-fi
Version:	2.3
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/voikko/corevoikko/releases
Source0:	https://github.com/voikko/corevoikko/archive/rel-voikko-fi-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	446ff56fb26feafdcfa97694a211d930
URL:		https://voikko.puimula.org/
BuildRequires:	foma
BuildRequires:	libstdc++-devel
BuildRequires:	libvoikko
BuildRequires:	python3 >= 1:3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Description of Finnish morphology written in Malaga.

%description -l pl.UTF-8
Opis morfologii języka fińskiego napisany w języku Malaga.

%package vfst
Summary:	Finish dictionary for voikko spellchecker/hyphenator
Summary(pl.UTF-8):	Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów voikko
Group:		Applications/Text
Requires:	libvoikko >= 4.0
Provides:	voikko-fi = %{version}
Obsoletes:	voikko-fi < %{version}
# malaga libvoikko interface is obsolete
Obsoletes:	voikko-fi-malaga < 2.2

%description vfst
Finish dictionary for voikko spellchecker/hyphenator.

%description vfst -l pl.UTF-8
Słownik fiński dla narzędzia sprawdzania pisowni/przenoszenia wyrazów
voikko.

#package -n sukija-fi

%prep
%setup -q -n corevoikko-rel-voikko-fi-%{version}

%build
%{__make} -C voikko-fi

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C voikko-fi vvfst-install \
	DESTDIR=$RPM_BUILD_ROOT%{_datadir}/voikko

%clean
rm -rf $RPM_BUILD_ROOT

%files -n voikko-fi-vfst
%defattr(644,root,root,755)
%doc voikko-fi/{CONTRIBUTORS,ChangeLog,README.md}
%{_datadir}/voikko/5/mor-standard/autocorr.vfst
%{_datadir}/voikko/5/mor-standard/index.txt
%{_datadir}/voikko/5/mor-standard/mor.vfst

#files -n sukija-fi
