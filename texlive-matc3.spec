Name:		texlive-matc3
Version:	29845
Release:	2
Summary:	Commands for MatematicaC3 textbooks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/matc3
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
