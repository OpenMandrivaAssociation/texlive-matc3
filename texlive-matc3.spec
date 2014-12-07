# revision 29845
# category Package
# catalog-ctan /macros/latex/contrib/matc3
# catalog-date 2013-04-09 15:55:17 +0200
# catalog-license lppl1.3
# catalog-version 1.0.1
Name:		texlive-matc3
Version:	1.0.1
Release:	8
Summary:	Commands for MatematicaC3 textbooks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/matc3
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for the Matematica C3 project to
produce free mathematical text books for use in Italian high
schools.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/matc3/matc3.sty
%doc %{_texmfdistdir}/doc/latex/matc3/Makefile
%doc %{_texmfdistdir}/doc/latex/matc3/README
%doc %{_texmfdistdir}/doc/latex/matc3/matc3.pdf
#- source
%doc %{_texmfdistdir}/source/latex/matc3/matc3.dtx
%doc %{_texmfdistdir}/source/latex/matc3/matc3.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
