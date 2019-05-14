%global sname tripleo-ui

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{?dlrn: %global tarsources %{sname}-%{upstream_version}}
%{!?dlrn: %global tarsources package}

Name:           openstack-%{sname}
Version:        7.4.10
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
* Tue May 14 2019 RDO <dev@lists.rdoproject.org> 7.4.10-1
- Update to 7.4.10

* Mon Jan 08 2018 RDO <dev@lists.rdoproject.org> 7.4.7-1
- Update to 7.4.7

* Sat Dec 09 2017 RDO <dev@lists.rdoproject.org> 7.4.6-1
- Update to 7.4.6

* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 7.4.5-1
- Update to 7.4.5

* Tue Nov 14 2017 RDO <dev@lists.rdoproject.org> 7.4.4-1
- Update to 7.4.4

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 7.4.3-1
- Update to 7.4.3

* Tue Oct 10 2017 rdo-trunk <javier.pena@redhat.com> 7.4.2-1
- Update to 7.4.2

* Wed Oct 04 2017 rdo-trunk <javier.pena@redhat.com> 7.4.1-1
- Update to 7.4.1

* Sun Sep 10 2017 rdo-trunk <javier.pena@redhat.com> 7.4.0-1
- Update to 7.4.0

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 7.3.0-1
- Update to 7.3.0

