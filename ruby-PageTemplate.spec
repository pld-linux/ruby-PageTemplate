Summary:	Ruby PageTemplate library
Summary(pl.UTF-8):	Biblioteka PageTemplate dla języka Ruby
Name:		ruby-PageTemplate
Version:	2.1.2
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5403/PageTemplate-%{version}.tar.gz
# Source0-md5:	2295464231d1b38be94441b9d98accae
Source1:	setup.rb
URL:		http://coolnamehere.com/products/pagetemplate/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
#BuildArch: noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PageTemplate is a Ruby package which allows you to utilize text
templates for your Web projects. It is mainly intended for use in a
CGI environment, but has been designed to be useful in a broad range
of similar applications. It is inspired by, yet almost entirely
unlike, the HTML::Template package available for Perl. It has many
features in common with other templating engines.

%description -l pl.UTF-8
PageTemplate to pakiet dla języka Ruby umożliwiający wykorzystywanie
szablonów tekstowych dla projektów WWW. Jest przeznaczony głównie do
używania w środowisku CGI, ale został zaprojektowany także by był
użyteczny w szerokim zakresie podobnych zastosowań. Jest zainspirowany
jednak prawie całkowicie odmiennym pakietem perlowym HTML::Template.
Ma wiele możliwości wspólnych z innymi silnikami szablonów.

%prep
%setup -q -n PageTemplate
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib --inline-source
rdoc --ri lib -o ri
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_rubylibdir}/PageTemplate.rb
%{ruby_rubylibdir}/PageTemplate
%{ruby_ridir}/*
