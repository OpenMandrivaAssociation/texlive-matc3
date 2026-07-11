%global tl_name matc3
%global tl_revision 29845

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Commands for MatematicaC3 textbooks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/matc3
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matc3.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for the Matematica C3 project to produce
free mathematical text books for use in Italian high schools.

