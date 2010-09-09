#
# NOTE:
# - see "URL:" for download links
# - if you want to build 32-bit version, you don't have to download Source1.
#   Just comment it out.
# - if you want to build 64-bit version, comment out Source0

%define		i386rel		0.1
%define		x8664rel	0.1.0-1
Summary:	JDBC Supplement for Oracle Database Instant Client
Name:		oracle-instantclient-jdbc
Version:	11.2
Release:	0.1
License:	OTN (proprietary, non-distributable)
Group:		Applications
Source0:	instantclient-jdbc-linux32-%{version}.%{i386rel}.zip
# NoSource0-md5:	e4ef505b542eb4dec665d659a6830e9d
Source1:	oracle-instantclient%{version}-jdbc-%{version}.%{x8664rel}.x86_64.zip
# NoSource1-md5:	5bb71717e0ff6f9e98eb874b1d72abe1
NoSource:	0
NoSource:	1
URL:		http://www.oracle.com/technology/software/tech/oci/instantclient/index.html
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		srcdir	instantclient_%(echo %{version} | tr . _)

%description
Oracle Database Instant Client Package - JDBC Supplement.
Additional support for XA, Internationalization, and RowSet
operations under JDBC  

%prep
%ifarch %{ix86}
%setup -q -c -T -b 0
%endif

%ifarch %{x8664}
%setup -q -c -T -b 1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/sqlplus,%{_javadir}}

install %{srcdir}/*.jar $RPM_BUILD_ROOT%{_javadir}
install %{srcdir}/*.so* $RPM_BUILD_ROOT%{_libdir}
install %{srcdir}/genezi $RPM_BUILD_ROOT%{_bindir}/genezi
install %{srcdir}/adrci $RPM_BUILD_ROOT%{_bindir}/adrci

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
%attr(755,root,root) %{_libdir}/*.so*
%attr(755,root,root) %{_bindir}/genezi
%attr(755,root,root) %{_bindir}/adrci
%doc %{srcdir}/BASIC_README
