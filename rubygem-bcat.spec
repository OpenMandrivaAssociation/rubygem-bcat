%define oname bcat

Name:       rubygem-%{oname}
Version:    0.6.1
Release:    %mkrel 1
Summary:    CLI Steps for Cucumber, hand-crafted for you in Aruba
Group:      Development/Ruby
License:    MIT
URL:        http://rtomayko.github.com/bcat
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(cucumber) >= 0.9.4
Requires:   rubygem(rack) >= 1.1.2
Requires:   rubygem(background_process)
#Requires:   rubygem(aruba) >= 0.4.2
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{oname}) = %{version}

%description
CLI Steps for Cucumber, hand-crafted for you in Aruba

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

# remove vcs files
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.gitignore

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{_bindir}/a2h
%{_bindir}/btee
%{_bindir}/bcat
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%{ruby_gemdir}/gems/%{oname}-%{version}/contrib/

#% files doc
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/man/
%{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%{ruby_gemdir}/gems/%{oname}-%{version}/INSTALLING
%{ruby_gemdir}/gems/%{oname}-%{version}/RELEASING
%{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%{ruby_gemdir}/gems/%{oname}-%{version}/CONTRIBUTING

%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
