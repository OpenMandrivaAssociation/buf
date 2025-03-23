
%define libname %mklibname buf

%global debug_package %{nil}

Name:		buf
Version:	1.50.1
Release:	1
URL:		https://github.com/bufbuild/buf
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    buf-1.50.1-vendor.tar.gz
Summary:	The best way of working with Protocol Buffers.
Group:      System/Libraries
License:	Apache-2.0

BuildRequires:	go

%description
%summary

%package -n %{libname}
Summary:    %{summary}
Group:      System/Libraries
Provides:   %{libname} = %{EVRD}

%description -n %{libname}

%prep
%autosetup -p1
tar -xzf %{SOURCE1}

%build
cd cmd/buf
go build


%install
install -Dpm755 cmd/buf/buf %{buildroot}%{_bindir}/buf

%files -n %{libname}
%{_bindir}/*
