%global sname tripleo-ui

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{?dlrn: %global tarsources %{sname}-%{upstream_version}}
%{!?dlrn: %global tarsources package}

Name:           openstack-%{sname}
Version:        8.3.0
Release:        1%{?dist}
Summary:        TripleO UI --- GUI for the TripleO project
License:        ASL 2.0
URL:            http://tripleo.org
# Source0 is created by running "npm pack"
Source0:        http://tarballs.openstack.org/tripleo-ui/tripleo-ui-%{upstream_version}.tar.gz
Source1:        tripleo-ui.conf

BuildRequires:  nodejs
BuildRequires:  git
BuildRequires:  %{name}-deps >= 7
BuildRequires:  /usr/bin/npm
BuildArch:      noarch

%description

%prep
%autosetup -n %{tarsources} -S git

%build
rm -rf node_modules
ln -s /opt/%{name}-deps/node_modules .
npm run build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/var/www/%{name}
mkdir -p %{buildroot}/etc/httpd/conf.d/
cp -rf dist %{buildroot}/var/www/%{name}/
cp -rf %{SOURCE1} %{buildroot}/etc/httpd/conf.d/%{name}.conf

%files
%{_localstatedir}/www/%{name}
%config(noreplace)  %{_sysconfdir}/httpd/conf.d/%{name}.conf
%license LICENSE
%doc README.md

%changelog
* Thu Mar 08 2018 RDO <dev@lists.rdoproject.org> 8.3.0-1
- Update to 8.3.0

