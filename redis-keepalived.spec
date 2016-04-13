%define RedisKeepalived         redis-keepalived
%define RedisKeepalivedMaster   redis-keepalived-master
%define RedisKeepalivedSlave    redis-keepalived-slave
%define RKVersion               1.0.0

Name: %{RedisKeepalived}
Version: %{RKVersion}
Release: 1%{?dist}
Summary: The Redis Keepalived
License: GPL
Group: Development/System
URL: 	https://github.com/ChenVsGuo/RedisKeepalived
Source: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: %__cp %__mv %__chmod %__grep %__mkdir %__install %__id

%description
This package provides Redis Keepalived

%package -n %{RedisKeepalivedMaster}
Requires: redis
Requires: keepalived
Summary: This package provides Redis Keepalived Master

%package -n %{RedisKeepalivedSlave}
Requires: redis
Requires: keepalived
Summary: This package provides Redis Keepalived Slave

%description -n %{RedisKeepalivedMaster}
This package is config of Redis Keepalived Master

%description -n %{RedisKeepalivedSlave}
This package is config of Redis Keepalived Slave

%prep
%setup -q

%build
# FIXME: I need to fix the upstream Makefile to use LIBDIR et al. properly and
# send the upstream maintainer a patch.
# add DOCDIR to the configure part

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/keepalived

cp -rf config %{buildroot}/etc/redis-keepalived
cp -rf scripts %{buildroot}/etc/keepalived/

%post -n %{RedisKeepalivedMaster}
sudo mv -f /etc/redis-keepalived/redis.conf /etc/
sudo mv -f /etc/redis-keepalived/keepalived.master /etc/keepalived/keepalived.conf
sudo rm -rf /etc/redis-keepalived

%post -n %{RedisKeepalivedSlave}
sudo mv -f /etc/redis-keepalived/redis.conf /etc/
sudo mv -f /etc/redis-keepalived/keepalived.slave /etc/keepalived/keepalived.conf
sudo rm -rf /etc/redis-keepalived

%postun

%clean
#rm -rf %{buildroot}

%files -n %{RedisKeepalivedMaster}
%defattr(-,root,root,-)
/etc/redis-keepalived/redis.conf
/etc/redis-keepalived/keepalived.master
/etc/keepalived/scripts/*

%files -n %{RedisKeepalivedSlave}
%defattr(-,root,root,-)
/etc/redis-keepalived/redis.conf
/etc/redis-keepalived/keepalived.slave
/etc/keepalived/scripts/*

%changelog
* Mon Jun 23 2014  Fuqiang Chen<evk55@126.com>
- first RPM release (1.0)
