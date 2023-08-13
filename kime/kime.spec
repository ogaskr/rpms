Summary:	KIME 한글입력기 
Name:		kime
Version:	3.0.2
Release:	%autorelease
Group:		System/Internalization
Vendor:		fedora
License:	GPLv3
URL:		https://github.com/Riey/kime/
Source0:	v%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	x86_64
BuildRequires:	rust

%define kime_conf_dir %{_sysconfdir}/xdg/%{name}
%define kime_inc_dir %{_includedir}
%define kime_lib_dir %{_libdir}
%define kime_gtk3_dir %{_libdir}/gtk-3.0/3.0.0/immodules
%define kime_qt5_dir %{_libdir}/qt5/plugins/platforminputcontexts
%define kime_qt6_dir %{_libdir}/qt6/plugins/platforminputcontexts
%define kime_icons_dir %{_datadir}/icons/hicolor/64x64/apps
%define kime_build_dir build/out
%define kime_autostart_dir %{_sysconfdir}/xdg/autostart


%description

GTK및 QT5,QT6 대부분 프로그램에서 한글을 입력할 수 있는 새로운 한글 입력기

%prep

%setup

%build
scripts/build.sh -ar

%install
rm -rf %{buildroot}
install -d -p  %{buildroot}%{_bindir}
install -d -p  %{buildroot}%{kime_lib_dir}
install -d -p  %{buildroot}%{kime_qt5_dir}
install -d -p  %{buildroot}%{kime_qt6_dir}
install -d -p  %{buildroot}%{kime_gtk3_dir}
install -d -p  %{buildroot}%{kime_inc_dir}
install -d -p  %{buildroot}%{kime_icons_dir}
install -d -p  %{buildroot}%{kime_conf_dir}
install -d -p  %{buildroot}%{_datadir}/im-config/data
install -d -p  %{buildroot}%{kime_autostart_dir}

install -Dm 0755 %{kime_build_dir}/kime %{buildroot}%{_bindir}
install -Dm 0755 %{kime_build_dir}/kime-* %{buildroot}%{_bindir}
install -Dm 0755 %{kime_build_dir}/libkime-gtk3.so %{buildroot}%{kime_gtk3_dir}/im-kime.so
install -Dm 0755 %{kime_build_dir}/libkime-qt5.so %{buildroot}%{kime_qt5_dir}/libkimeplatforminputcontextplugin.so
install -Dm 0755 %{kime_build_dir}/libkime-qt6.so %{buildroot}%{kime_qt6_dir}/libkimeplatforminputcontextplugin.so
install -Dm 0755 %{kime_build_dir}/libkime_engine.so %{buildroot}%{kime_lib_dir}/
install -Dm 0755 %{kime_build_dir}/*.desktop %{buildroot}%{kime_autostart_dir}/
install -Dm 0644 %{kime_build_dir}/icons/64x64/*.png %{buildroot}%{kime_icons_dir}/
install -Dm 0644 %{kime_build_dir}/default_config.yaml %{buildroot}%{kime_conf_dir}/config.yaml
install -Dm 0644 %{kime_build_dir}/kime_engine.hpp %{buildroot}%{kime_inc_dir}/
install -Dm 0644 %{kime_build_dir}/kime_engine.h %{buildroot}%{kime_inc_dir}/
install -Dm 0644 %{kime_build_dir}/LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE


		    
%clean
rm -rf %{buildroot}

%post
gtk-query-immodules-3.0-64 --update-cache

%postun
gtk-query-immodules-3.0-64 --update-cache

%files


%defattr(-,root,root) 
%doc LICENSE
%{_bindir}/*
%{kime_icons_dir}/*
%{kime_conf_dir}/config.yaml
%{kime_gtk3_dir}/im-kime.so
%{kime_qt5_dir}/libkimeplatforminputcontextplugin.so
%{kime_qt6_dir}/libkimeplatforminputcontextplugin.so
%{kime_lib_dir}/libkime_engine.so
%{_includedir}/kime*
%{kime_autostart_dir}/*


%changelog
* Sun Aug 13 2023 ogaskr 3.0.2-2
- add Qt6 support
- change Source file name
- change files
- remove i18n settings
* Sat Aug 12 2023 ogaskr 3.0.2-1
- make rpm spec
