Name:           python-rpm-macros
Version:        3
Release:        45%{?dist}
Summary:        The unversioned Python RPM macros

License:        MIT
Source0:        macros.python
Source1:        macros.python-srpm
Source2:        macros.python2
Source3:        macros.python3
Source4:        macros.pybytecompile

BuildArch:      noarch
# For %%python3_pkgversion used in %%python_provide
Requires:       python-srpm-macros
Obsoletes:      python-macros < 3
Provides:       python-macros = %{version}-%{release}

%description
This package contains the unversioned Python RPM macros, that most
implementations should rely on.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package -n python-srpm-macros
Summary:        RPM macros for building Python source packages

%description -n python-srpm-macros
RPM macros for building Python source packages.

%package -n python2-rpm-macros
Summary:        RPM macros for building Python 2 packages
# For %%py_setup
Requires:       python-rpm-macros = %{version}-%{release}

%description -n python2-rpm-macros
RPM macros for building Python 2 packages.

%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
# Older versions have old pathfix.py without -ka options support
Conflicts:      platform-python-devel < 3.6.8-35
# For %%py_setup
Requires:       python-rpm-macros = %{version}-%{release}
# For %%_python3_pkgversion_with_dot needed by %%__pytest
Requires:       python-srpm-macros = %{version}-%{release}

%description -n python3-rpm-macros
RPM macros for building Python 3 packages.


%prep

%build

%install
mkdir -p %{buildroot}/%{rpmmacrodir}
install -m 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
  %{buildroot}/%{rpmmacrodir}/


%files
%{rpmmacrodir}/macros.python
%{rpmmacrodir}/macros.pybytecompile

%files -n python-srpm-macros
%{rpmmacrodir}/macros.python-srpm

%files -n python2-rpm-macros
%{rpmmacrodir}/macros.python2

%files -n python3-rpm-macros
%{rpmmacrodir}/macros.python3


%changelog
* Wed Feb 22 2023 Miro Hrončok <mhroncok@redhat.com> - 3-45
- Fix %%python3_version macros for Python 3.10+
Resolves: rhbz#2169780

* Fri Oct 14 2022 Charalampos Stratakis <cstratak@redhat.com> - 3-44
- Backport the %%python_wheel_pkg_prefix and the %%python_wheel_dir macros from Fedora
Resolves: rhbz#2143991

* Tue Jul 26 2022 Tomas Orsava <torsava@redhat.com> - 3-43
- Make %%pytest macro respect %%python3_pkgversion
Resolves: rhbz#2091462

* Wed May 25 2022 Miro Hrončok <mhroncok@redhat.com> - 3-42
- Make %%py3_dist respect %%python3_pkgversion
Resolves: rhbz#2090007

* Mon Feb 01 2021 Lumír Balhar <lbalhar@redhat.com> - 3-41
- Fix dependencies between subpackages
Resolves: rhbz#1892797

* Thu Jan 14 2021 Lumír Balhar <lbalhar@redhat.com> - 3-40
- New macros backported from Fedora/EPEL
Resolves: rhbz#1892797

* Tue Jun 16 2020 Charalampos Stratakis <cstratak@redhat.com> - 3-39
- Strip tildes from %%version in %%pypi_source by default
- Resolves: rhbz#1844902

* Mon Oct 14 2019 Charalampos Stratakis <cstratak@redhat.com> - 3-38
- Fix the %%py_build macro to respect the global definition of %%__python
- Resolves: rhbz#1757833

* Fri Dec 14 2018 Miro Hrončok <mhroncok@redhat.com> - 3-37
- Workaround leaking buildroot PATH in %py_byte_compile
- Resolves: rhbz#1644455

* Fri Dec 14 2018 Miro Hrončok <mhroncok@redhat.com> - 3-36
- Make %%py_byte_compile terminate build on SyntaxErrors
- Resolves: rhbz#1620168

* Mon Sep 17 2018 Tomas Orsava <torsava@redhat.com> - 3-35
- Disable the python_provide macro for `python2-` prefixed packages
- Resolves: rhbz#1636029

* Mon Jul 16 2018 Tomas Orsava <torsava@redhat.com> - 3-34
- macros.pybytecompile: Macro was not line-continued properly and thus didn't work

* Wed Jul 11 2018 Tomas Orsava <torsava@redhat.com> - 3-33
- macros.pybytecompile: Detect Python version through sys.version_info instead
  of guessing from the executable name

* Tue Jul 10 2018 Tomas Orsava <torsava@redhat.com> - 3-32
- Merging: (Tue Jul 10 2018 Tomas Orsava <torsava@redhat.com> - 3-32)
  - Fix %%py_byte_compile macro: when invoked with a Python 2 binary it also
    mistakenly ran py3_byte_compile
- Merging: (Tue Jul 03 2018 Miro Hrončok <mhroncok@redhat.com> - 3-31)
  - Add %%python3_platform useful for PYTHONPATH on arched builds
- Merging: (Mon Jun 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3-30)
  - Add %%pypi_source macro, as well as %%__pypi_url and
    %%_pypi_default_extension.
- Merging: (Wed Apr 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3-29)
  - move macros.pybytecompile from python3-devel

* Wed Jun 27 2018 Tomas Orsava <torsava@redhat.com> - 3-31
- Remove RHEL_ALLOW_PYTHON2_FOR_BUILD=1 from build and install macros,
  as that is where the user needs to set it themself

* Thu Jun 21 2018 Tomas Orsava <torsava@redhat.com> - 3-30
- Explicitly enable Python 2 when invoking Python 2 macros
  See: https://url.corp.redhat.com/rhel8-py2

* Wed May 09 2018 Tomas Orsava <torsava@redhat.com> - 3-29
- Switch the Python 3 executable to /usr/libexec/platform-python
- Update macros using pip or easy_install to be invoked through the main
  executable

* Fri Apr 06 2018 Tomas Orsava <torsava@redhat.com> - 3-28
- Fix the %%py_dist_name macro to not convert dots (".") into dashes, so that
  submodules can be addressed as well
Resolves: rhbz#1564095

* Fri Mar 23 2018 Miro Hrončok <mhroncok@redhat.com> - 3-27
- make LDFLAGS propagated whenever CFLAGS are

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3-25
- Add %%python_enable_dependency_generator

* Tue Nov 28 2017 Tomas Orsava <torsava@redhat.com> - 3-24
- Remove platform-python macros (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Oct 26 2017 Ville Skyttä <ville.skytta@iki.fi> - 3-23
- Use -Es/-I to invoke macro scriptlets (#1506355)

* Wed Aug 02 2017 Tomas Orsava <torsava@redhat.com> - 3-22
- Add platform-python macros (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Michal Cyprian <mcyprian@redhat.com> - 3-20
- Revert "Switch %%__python3 to /usr/libexec/system-python"
  after the Fedora Change https://fedoraproject.org/wiki/Changes/Making_sudo_pip_safe
  was postponed

* Fri Feb 17 2017 Michal Cyprian <mcyprian@redhat.com> - 3-19
- Switch %%__python3 to /usr/libexec/system-python

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michal Cyprian <mcyprian@redhat.com> - 3-17
- Add --no-deps option to py_install_wheel macros

* Tue Jan 17 2017 Tomas Orsava <torsava@redhat.com> - 3-16
- Added macros for Build/Requires tags using Python dist tags:
  https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Nov 24 2016 Orion Poplawski <orion@cora.nwra.com> 3-15
- Make expanded macros start on the same line as the macro

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> 3-14
- Fix %%py3_install_wheel (bug #1395953)

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> 3-13
- Add missing sleeps to other build macros
- Fix build_egg macros
- Add %%py_build_wheel and %%py_install_wheel macros

* Tue Nov 15 2016 Orion Poplawski <orion@cora.nwra.com> 3-12
- Add %%py_build_egg and %%py_install_egg macros
- Allow multiple args to %%py_build/install macros
- Tidy up macro formatting

* Wed Aug 24 2016 Orion Poplawski <orion@cora.nwra.com> 3-11
- Use %%rpmmacrodir

* Tue Jul 12 2016 Orion Poplawski <orion@cora.nwra.com> 3-10
- Do not generate useless Obsoletes with %%{?_isa}

* Fri May 13 2016 Orion Poplawski <orion@cora.nwra.com> 3-9
- Make python-rpm-macros require python-srpm-macros (bug #1335860)

* Thu May 12 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 3-8
- Add single-second sleeps to work around setuptools bug.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Orion Poplawski <orion@cora.nwra.com> 3-6
- Fix typo in %%python_provide

* Thu Jan 14 2016 Orion Poplawski <orion@cora.nwra.com> 3-5
- Handle noarch python sub-packages (bug #1290900)

* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> 3-4
- Fix python2/3-rpm-macros package names

* Thu Jan 7 2016 Orion Poplawski <orion@cora.nwra.com> 3-3
- Add empty %%prep and %%build

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> 3-2
- Combined package

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> 3-1
- Initial package
