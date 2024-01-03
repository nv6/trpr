Name:           trpr
Version:        2.1b11
Release:        1%{?dist}
Summary:        Trace Plot Realtime distribution 2.1b11

License:        FIXME
URL:            https://github.com/nv6/%{name}
%undefine       _disable_source_fetch
Source0:        https://github.com/nv6/%{name}/archive/refs/tags/%{version}.tar.gz
%define         SHA256SUM0 c00d09716de8cb609a33ca3dbcf9657816f3be79c113995a31d2479d487ac38b
BuildRequires:  g++ make

%description
TRace Plot Realtime (TRPR) statistical analysis tool for MGEN, TCPdump, NS-2 (from US NRL)

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%setup -q

%build
make -f Makefile.linux

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}
install -m 0755 hcat %{buildroot}/%{_bindir}

%clean
rm -rf %{_buildrootdir}
rm -rf %{_builddir}
rm -rf %{_sourcedir}

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/hcat
