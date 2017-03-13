%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name is-equal-shallow

Summary:       Does a shallow comparison of two objects
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.1.3
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/is-equal-shallow
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Does a shallow comparison of two objects, returning false if 
the keys or values differ.

The purpose of this lib is to do the fastest comparison possible 
of two objects when the values will predictably be primitives.

 - only compares objects.
 - only compares the first level of each object
 - values must be primitives. 
     If a value is not a primitive, even if the values are the same, 
     false is returned.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.3-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.3-3
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.3-2
- Enable scl macros, fix license macro for el6

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 0.1.3-1
- Initial package
