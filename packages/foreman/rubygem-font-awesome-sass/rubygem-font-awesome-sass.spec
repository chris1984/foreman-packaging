# template: default
%global gem_name font-awesome-sass

Name: rubygem-%{gem_name}
Version: 4.6.2
Release: 10%{?dist}
Summary: Font-Awesome SASS
License: MIT
URL: https://github.com/FortAwesome/font-awesome-sass
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/FortAwesome/font-awesome-sass/commit/8c85abf355cfdb81bd87a0e1d11dc3876e71a5c6
Patch0: 0001-Update-to-use-either-sass-or-sassc-gem.patch

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Font-Awesome SASS gem for use in Ruby projects.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -p1 -n %{gem_name}-%{version}

# Foreman relies on the Rails integration and that pulls in sass
%gemspec_remove_dep -g sass

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/assets
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/font-awesome-sass.gemspec

%changelog
* Fri Feb 14 2025 Adam Ruzicka <aruzicka@redhat.com> - 4.6.2-10
- Do not use obsolete form of patch macro

* Fri Jul 29 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.6.2-9
- Use upstream patch to make sass optional

* Wed Jul 27 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.6.2-8
- Correctly replace sass dependency with sassc

* Wed Jul 27 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.6.2-7
- Replace deprecated sass dependency with sassc

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.6.2-6
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.6.2-5
- Bump to release for EL8

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.6.2-4
- Update spec to remove the ror scl

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.6.2-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.6.2-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 4.6.2-1
- Update font-awesome-sass to 4.6.2 (dominic@cleal.org)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 4.3.2.1-3
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 4.3.2.1-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Thu Dec 31 2015 Daniel Lobato <elobatocs@gmail.com> 4.3.2.1-1
- Initial package
